# ----- To Do -------

# 1.    Look at doubles. Eg, double Hs add worse scoring.
# 1.5   Look at Qs etc - Q followed by not U adds a worse scoring.
# 2.    Look at special characters. Count E` as E.
# 3.    Add a likelyhood
# 4.    Use a dictionary, do word count, divide likelihood by it? - with option -w (incase there are no spaces)
# 5.    Option to use uppercase, numbers and symbols (just list all 26?)
# 6.    -k <0 or -k thisisthekey or -k 10 or -k 4<k<10

import sys, frequencylib
from vigenerelib import decipher as vigenere

#Note to self: http://www.cryptogram.org/cdb/words/frequency.html
english = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15, 'q': 0.10, 'z': 0.07}

def usage():
    print ("""

Cipher 1.0 (https://github.com/noahingham/...)

Usage: cipher.py [-l language] [-n number of results] [-f path/to/file] [-k Key length] [-km Min key length]

Languages available:    english
                        italian
			french
			latin
			spanish
			portuguese

    """)

def guess(cipher, language, amount, minKey, Key):
    wList = shift(cipher, language) + [x for x in vigenere(cipher, language, minKey, Key)]
    wList.sort(key=lambda x: x[0])
    for plainText in wList[:amount]:
        print('\n\t%s:  %s' %(plainText[2], plainText[1]))
    print('')

def shift(cipher, language=english):
    cipherLower = list(cipher.lower())
    return frequencylib.shiftAnalysis(cipherLower, language)

if __name__ == '__main__':
    amount, cipher, minKey, Key = 1, None, 5, []

    # Check for arguments
    for x in range(len(sys.argv)):
        language = english
        if sys.argv[x] == '-l':
            from languages import *
            language = eval(sys.argv[x+1])
        elif sys.argv[x] == '-n':
            amount = eval(sys.argv[x+1])
        elif sys.argv[x] == '-h' or sys.argv[x] == '--help':
            usage()
            break
        elif sys.argv[x] == '-f':
            with open(sys.argv[x+1], 'r') as f:
                cipher = f.read()
        elif sys.argv[x] == '-k':
            Key = int(sys.argv[x+1])
        elif sys.argv[x] == '-km':
            minKey = [int(sys.argv[x+1])]

    else: # We break if -h wasn't called.
        if not cipher:
            if sys.version_info >= (3,0):
                cipher = input(' >>> ')
            else:
                cipher = raw_input(' >>> ')
        guess(cipher, language, amount, minKey,Key)
