HOME = '/home/arch'
import os, sys, colorsys

color1=sys.argv[1]
color2=sys.argv[2]

if color1=='-h':
    print('Usage:\n\t\tpython abcdef\n\nwhere #abcdef is the hex-value of the desired color.')



def hex_to_rgb(hex):
    if len(hex)==6:
        return [ int('0x'+hex[:2], 0), int('0x'+hex[2:4], 0), int('0x'+hex[4:6], 0) ]
    if len(hex)==3:
        return [ int('0x'+hex[0]*2, 0), int('0x'+hex[1]*2, 0), int('0x'+hex[2]*2, 0) ]

def rgb_to_hex(rgb):
    print(rgb)
    r, g, b = rgb
    return hex(r)[2:4] + hex(g)[2:4] + hex(b)[2:4]

def inverse(rgb):
    r, g, b = rgb
    h, l, s = colorsys.rgb_to_hls(r,g,b)
    l = 360 - l
    print([h,l,s])
    r1,g1,b1= colorsys.hls_to_rgb(h,l,s)
    return [int(r1), int(g1), int(b1)]



# ------- XTerm -------------------------------------------------

xterm = ('\
\
XTerm*Background: #1f1f1f\n\
XTerm*Foreground: white\n\
XTerm*font: 6x10\n\
XTerm*saveLines: 100000\n\
XTerm*HiForeColor: white\n\
XTerm*HiBackColor: #c06077\n\
XTerm*geometry: +50+100\n\
XTerm*allowBoldFonts: false\n\
*xterm*background: #101010\n\
*xterm*foreground: #d0d0d0\n\
*xterm*cursorColor: #d0d0d\n\

! Black\n\
*xterm*color0: #101010\n\
*xterm*color8: #303030\n\
! Red\n\
*xterm*color1: #%s\n\
*xterm*color9: #ff0090\n\
! Green\n\
*xterm*color2: #%s\n\
*xterm*color10: #80ff00\n\
! Yellow\n\
*xterm*color3: #c47f2c\n\
*xterm*color11: #ffba68\n\
! Blue\n\
*xterm*color4: #30309b\n\
*xterm*color12: #5f5fee\n\
! Magenta\n\
*xterm*color5: #7e40a5\n\
*xterm*color13: #bb88dd\n\
! Cyan\n\
*xterm*color6: #3579a8\n\
*xterm*color14: #4eb4fa\n\
! White\n\
*xterm*color7: #9999aa\n\
*xterm*color15: #d0d0d0\
\
' %(color1, color2)) 

with open(HOME+'/XTerm', 'w+') as f:
    f.write(xterm)


# ------- XMonad ------------------------------------------------

insert = ('\
colorf = "#d0d0d0"\n\
colorb = "#101010"\n\
-- Black\n\
color0 = "#d0d0d0"\n\
color8 = "#303030"\n\
-- Red\n\
color1 = "#%s"\n\
color9 = "#ff0090"\n\
-- Green\n\
color2 = "#%s"\n\
color10 = "#80ff00"\n\
-- Yellow\n\
color3 = "#c47f2c"\n\
color11 = "#ffba68"\n\
-- Blue\n\
color4 = "#30309b"\n\
color12 = "#5f5fee"\n\
-- Magenta\n\
color5 = "#7e40a5"\n\
color13 = "#bb88dd"\n\
-- Cyan\n\
color6 = "#3579a8"\n\
color14 = "#4eb4fa"\n\
-- White\n\
color7 = "#9999aa"\n\
color15 = "#d0d0d0"\n\
-- Red\n\
colorfg=color2\n\
colorbg=color1\n\
\
')

insert = ('-- HERE\ncolor1 = "#%s"\ncolor2 = "#%s"\n-- DONE' %(color1, color2))

with open (HOME + '/.xmonad/xmonad.hs', 'r') as f:
    hl = f.read()

start = hl[:hl.find('-- HERE')]
rest = hl[hl.find('-- DONE')+7:]


with open (HOME + '/.xmonad/xmonad.hs', 'w') as f:
    f.write(start)
    f.write(insert)
    f.write(rest)

# ------- XMobar ------------------------------------------------

insert = ('"-h","#%s","-l","#%s"' %(color1, color2))

with open (HOME + '/.xmonad/xmobar.hs', 'r') as f:
    hl = f.read()

import re

hl = re.sub('"-h","#......","-l","#......"',insert,hl) 

with open (HOME + '/.xmonad/xmobar.hs', 'w') as f:
    f.write(hl)


# ------- Homepage -----------------------------------------------

insert = ('/*HERE*/\ncolor: #%s;\n/*REST*/' %(color2))

with open(HOME + '/html/style.css', 'r') as f: 
    css = f.read()



start = css[:css.find('/*HERE*/')]
rest = css[css.find('/*REST*/')+8:]

reststart = rest[:rest.find('/*HERE*/')]
restrest = rest[rest.find('/*REST*/')+8:]


with open(HOME + '/html/style.css', 'w') as f: 
    f.write(start)
    f.write(insert)
    f.write(reststart)
    f.write(insert)
    f.write(restrest)


# ------- Firefox -----------------------------------------------

insert = ('/*HERE*/\ncolor:#%s !important;\n/*REST*/' %(color2))

with open(HOME + '/.mozilla/firefox/irr3wx17.default/chrome/userChrome.css', 'r') as f: 
    css = f.read()


start = css[:css.find('/*HERE*/')]
rest = css[css.find('/*REST*/')+8:]


with open(HOME + '/.mozilla/firefox/irr3wx17.default/chrome/userChrome.css', 'w') as f: 
    f.write(start)
    f.write(insert)
    f.write(rest)


# ------- Background --------------------------------------------

os.system('convert -size 100x100 xc:#%s ~/.xmonad/wallpaper.png'%color1)




# ------- Apply changes -----------------------------------------

os.system('cd ~/.xmonad; ghc -threaded xmonad.hs; mv xmonad xmonad-x86_64-linux; xmonad --restart;')
os.system('feh --bg-fill ~/.xmonad/wallpaper.png')

os.system('killall firefox-aurora')
os.system('xterm -hold -e tty-clock -cs &')
os.system('xterm -hold -e ~/-Scripts/colors.sh &')
os.system('xterm -hold -e archey3 &')
os.system('firefox-aurora &')
