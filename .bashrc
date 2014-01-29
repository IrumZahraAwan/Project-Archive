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



blue="\033[0;34m"
lblue="\033[1;34m"
green="\033[0;32m"
lgreen="\033[1;32m"
cyan="\033[0;36m"
lcyan="\033[1;36m"
red="\033[0;31m"
lred="\033[1;31m"
purple="\033[0;35m"
lpurple="\033[1;35m"
orange="\033[0;33m"
lorange="\033[1;33m"
black="\033[0;30m"
white="\033[1;37m"
gray="\033[1;30m"
lgray="\033[0;37m"
noc="\033[0;0m"



EXITSTATUS="$?"
BOLD="\[\033[1m\]"

# background colors
BGK="\[\033[40m\]"
BGR="\[\033[41m\]"
BGG="\[\033[42m\]"
BGY="\[\033[43m\]"
BGB="\[\033[44m\]"
BGM="\[\033[45m\]"
BGC="\[\033[46m\]"
BGW="\[\033[47m\]"

function lines {
  echo -e "${green}"
  eval printf %.0s- '{1..'"${COLUMNS:-$(tput cols)}"\}; echo
  echo -e "${noc}"
}

function exitstatus {

    if [ "${EXITSTATUS}" -eq 0 ]
    then
       PROMPT="${BOLD}${GREEN}+${OFF}"
    else
       PROMPT="${BOLD}${RED}ERROR\n\nX${OFF}"
    fi
    PS1="\n\n${PROMPT} [${BLUE}\W${OFF}]  ${RED}>>${OFF}  "

    PS2="${BOLD}>${OFF} "
}

#exitstatus

#PS1="$(lines) ${RED}>>${OFF} "

#smiley () { echo -e ":\\$(($??50:51))"; }
export PS1=" \h \e${green}\w\e\n\n${green} >>${noc} "

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
