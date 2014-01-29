#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

#export PATH=\$PATH:~/.xmonad/bin
export EDITOR=vim

UNDER="\[\033[1;4m\]"    # white
FLASH="\[\033[1;5m\]"    # white
ANTI="\[\033[1;7m\]"    # white


color0="\033[0;30m"
color8="\033[1;30m"

color1="\033[0;31m"
color9="\033[1;31m"

color2="\033[0;32m"
color10="\033[1;32m"

color3="\033[0;33m"
color11="\033[1;33m"

color4="\033[0;34m"
color12="\033[1;34m"

color5="\033[0;35m"
color13="\033[1;35m"

color6="\033[0;36m"
color14="\033[1;36m"

color7="\033[1;37m"
color15="\033[0;37m"

noc="\033[0;0m"

#HERE/
colorf=${color1}
colorb=${color2}
#REST033[40m"
BGR="\033[41m"
BGG="\033[42m"
BGY="\033[43m"
BGB="\033[44m"
BGM="\033[45m"
BGC="\033[46m"
BGW="\033[47m"

function wholelines {
  echo -e "${colorf}${BGR}"
  eval printf %.0s- '{1..'"${COLUMNS:-$(tput cols)}"\}; echo
  echo -e "${noc}"
}
function lines {
  echo -e "${colorf}"
  eval printf %.0s- '{1..'"${COLUMNS:-$(tput cols)}"\}; echo
  echo -e "${noc}"
}


export PS1=" \h \e${colorf}\w\e\n\n${colorf} >>${noc} "

trap 'echo -e "\n$(lines)\n"' DEBUG





HISTFILESIZE=
HISTSIZE=
HISTCONTROL=ignoreboth



# All my aliases!
alias bashrc='vim ~/.bashrc && source ~/.bashrc'
alias ls='ls -la --color'
alias firefox-aurora='firefox-aurora &'
alias syn='synergyc -n localhost.local 10.0.1.166'

function sha1 {
    echo -n $1 | openssl sha1
}

function swap()         
{
  if [ $# -ne 2 ]; then
    echo "Usage: swap file1 file2"
  else
    local TMPFILE=$(mktemp)
    mv "$1" $TMPFILE && mv "$2" "$1" && mv $TMPFILE "$2"
  fi
}

clear
