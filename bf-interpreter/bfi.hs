module Bfi where

import Data.Char
import System.Console.Readline
import System.IO
import System.Exit

data Tape a = Tape [a] a [a]

data Control = Move_Left
             | Move_Right
             | Increment
             | Decrement
             | Loop
             | End_Loop
             | Input
             | Output

             | EOF
             | IGNORE

type Program = Tape Char

--one_way_tape :: Tape Int
-- one_way_tape = Tape [] 0 [0,0..]

two_way_tape :: Tape Int
two_way_tape = Tape [0,0..] 0 [0,0..]

control :: Char -> Control
control readin = case readin of
  '>'  -> Move_Left
  '<'  -> Move_Right
  '+'  -> Increment
  '-'  -> Decrement
  '['  -> Loop
  ']'  -> End_Loop
  ','  -> Input
  '.'  -> Output
  '\0' -> EOF
  _    -> IGNORE

step :: Program -> Tape Int -> IO (Tape Int)
step program@(Tape _ readin _) tape@(Tape left headin right) = case control readin of 
      Move_Left  -> step (move_right program) $move_right tape
      Move_Right -> step (move_right program) $move_left tape
      Increment  -> step (move_right program) $increment tape
      Decrement  -> step (move_right program) $decrement tape
      Loop       -> case headin of
               0 -> step (move_to_right_bracket (move_right program)) tape
               _ -> step (move_right program) tape
      End_Loop   -> case headin of
               0 -> step (move_right program) tape
               _ -> step (move_to_left_bracket (move_left program)) tape
      Input      -> do
               char <- getChar
               case ord char of
                 -- FIX EOF's value of 4
                 4 -> step (move_right program) (Tape left 0 right)
                 _ -> step (move_right program) $Tape left (ord char) right
      Output     -> do 
               putChar $chr headin
               step (move_right program) tape
      EOF        -> return tape
      IGNORE     -> step (move_right program) tape

increment :: Tape Int -> Tape Int
increment (Tape left center right) = Tape left (center+1) right

decrement :: Tape Int -> Tape Int
decrement (Tape left center right) = Tape left (center-1) right

move_right :: Tape a -> Tape a
move_right (Tape left center right) = Tape (center:left) (head right) (tail right)

move_left :: Tape a -> Tape a
move_left (Tape [] _ _) = error "ERROR: Reached tape's left-bound."
move_left (Tape left center right) = Tape (tail left) (head left) (center:right)

move_to_left_bracket :: Program -> Program
move_to_left_bracket program@(Tape _ readin _) = case readin of
  '[' -> program
  ']' -> move_to_left_bracket (move_left (move_to_left_bracket (move_left program)))
  _   -> move_to_left_bracket (move_left program)

move_to_right_bracket :: Program -> Program
move_to_right_bracket program@(Tape _ readin _) = case readin of
  ']' -> move_right program
  '[' -> move_to_right_bracket $move_to_right_bracket $move_right program
  _   -> (move_to_right_bracket . move_right) program

{-# ANN module ("HLint: ignore Use camelCase" :: String) #-}
main :: IO()
main = do
          m_program <- readline "$ "
          case m_program of 
            Nothing     -> return () -- EOF \/ control-d
            Just "" -> exitSuccess
            Just program -> do
              addHistory program
              hSetBuffering stdin  NoBuffering
              hSetBuffering stdout NoBuffering
              hSetEcho stdin False
              step (Tape [] (head program) (tail program++"\0") ) two_way_tape
              hSetBuffering stdin  LineBuffering
              hSetBuffering stdout LineBuffering
              hSetEcho stdin True
              putStrLn ""
          main
