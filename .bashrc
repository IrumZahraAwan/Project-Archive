#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

#export PATH=\$PATH:~/.xmonad/bin
export EDITOR=vim


# colors
BLACK="\[\033[1;30m\]"    # black
RED="\[\033[1;31m\]"    # red
GREEN="\[\033[1;32m\]"    # green
YELLOW="\[\033[1;33m\]"    # yellow
BLUE="\[\033[1;34m\]"    # blue
MAGENTA="\[\033[1;35m\]"    # magenta
CYAN="\[\033[1;36m\]"    # cyan
WHITE="\[\033[1;37m\]"    # white
OFF="\[\033[0m\]"
UNDER="\[\033[1;4m\]"    # white
FLASH="\[\033[1;5m\]"    # white
ANTI="\[\033[1;7m\]"    # white

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
  echo  "\033[1;31m"
  eval printf %.0s- '{1..'"${COLUMNS:-$(tput cols)}"\}; echo
  echo  "\033[0m"
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
export PS1=" \h \e${BLACK}\w\e\n\n${RED} >>${OFF} "

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
