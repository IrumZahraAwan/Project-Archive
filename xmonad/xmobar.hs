-- xmobar config used by Vic Fryzel
-- Author: Vic Fryzel
-- http://github.com/vicfryzel/xmonad-config

-- This is setup for dual 1920x1080 monitors, with the right monitor as primary
Config {
    font = "xft:Fixed-8",
    bgColor = "#101010",
    fgColor = "#d0d0d0",
    position = Static { xpos = 0, ypos = 0, width = 1280, height = 16 },
    lowerOnStart = True,
    commands = [
        Run Weather "YSCB" ["-t","<tempC>C <skyCondition>","-L","64","-H","77","-n","#CEFFAC","-h","#f5f2df","-l","#f5f2df"] 18000,
        Run MultiCpu ["-t","Cpu: <total0> <total1> <total2> <total3>","-L","30","-H","60","-h","#f5f2df","-l","#f5f2df","-n","#FFFFCC","-w","3"] 10,
        Run Memory ["-t","Mem: <usedratio>%","-H","8192","-L","4096","-h","#f5f2df","-l","#f5f2df","-n","#FFFFCC"] 10,
        Run Swap ["-t","Swap: <usedratio>%","-H","1024","-L","512","-h","#f5f2df","-l","#f5f2df","-n","#FFFFCC"] 10,
        Run Network "eth0" ["-t","Net: <rx>, <tx>","-H","200","-L","10","-h","#f5f2df","-l","#f5f2df","-n","#FFFFCC"] 10,
        Run Date "%a %b %_d %l:%M" "date" 10,
        Run StdinReader
    ],
    sepChar = "%",
    alignSep = "}{",
    template = "%StdinReader% }{ %multicpu% %memory% %swap% %eth0% <fc=#FFFFCC>%date%</fc> %YSCB%"
}
