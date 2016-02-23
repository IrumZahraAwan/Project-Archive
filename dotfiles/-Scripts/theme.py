HOME = '/home/arch'
import os, sys, colorsys
import re

from themes.newhat import *

#color1=sys.argv[1]
#color2=sys.argv[2]

colorb=eval(colorbl)
colorf=eval(colorfl)

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
XTerm*Background: #%s\n\
XTerm*Foreground: #%s\n\
XTerm*font: 6x10\n\
XTerm*saveLines: 100000\n\
XTerm*HiBackColor: #%s\n\
XTerm*HiForeColor: #%s\n\
XTerm*geometry: +50+100\n\
XTerm*allowBoldFonts: false\n\
*xterm*background: #%s\n\
*xterm*foreground: #%s\n\
*xterm*cursorColor: #%s\n\
\
! Black\n\
*xterm*color0: #%s\n\
*xterm*color8: #%s\n\
! Red\n\
*xterm*color1: #%s\n\
*xterm*color9: #%s\n\
! Green\n\
*xterm*color2: #%s\n\
*xterm*color10: #%s\n\
! Yellow\n\
*xterm*color3: #%s\n\
*xterm*color11: #%s\n\
! Blue\n\
*xterm*color4: #%s\n\
*xterm*color12: #%s\n\
! Magenta\n\
*xterm*color5: #%s\n\
*xterm*color13: #%s\n\
! Cyan\n\
*xterm*color6: #%s\n\
*xterm*color14: #%s\n\
! White\n\
*xterm*color7: #%s\n\
*xterm*color15: #%s\
\
' %(background, foreground, background, foreground, background, foreground, foreground, color0, color8, color1, color9, color2, color10, color3, color11, color4, color12, color5, color13, color6, color14, color7, color15)) 

with open(HOME+'/XTerm', 'w+') as f:
    f.write(xterm)


# ------- XMonad ------------------------------------------------

insert = ('\
--HERE\n\
colorf = "#%s"\n\
colorb = "#%s"\n\
-- Black\n\
color0 = "#%s"\n\
color8 = "#%s"\n\
-- Red\n\
color1 = "#%s"\n\
color9 = "#%s"\n\
-- Green\n\
color2 = "#%s"\n\
color10 = "#%s"\n\
-- Yellow\n\
color3 = "#%s"\n\
color11 = "#%s"\n\
-- Blue\n\
color4 = "#%s"\n\
color12 = "#%s"\n\
-- Magenta\n\
color5 = "#%s"\n\
color13 = "#%s"\n\
-- Cyan\n\
color6 = "#%s"\n\
color14 = "#%s"\n\
-- White\n\
color7 = "#%s"\n\
color15 = "#%s"\n\
-- Red\n\
colorfg="#%s"\n\
colorbg="#%s"\n\
--REST\n\
\
' %(foreground, background, color0, color8, color1, color9, color2, color10, color3, color11, color4, color12, color5, color13, color6, color14, color7, color15, colorf, colorb)) 

#insert = ('--HERE\ncolor1 = "#%s"\ncolor2 = "#%s"\n--REST' %(color1, color2))

with open (HOME + '/.xmonad/xmonad.hs', 'r') as f:
    hl = f.read()


hl = re.sub("dmenu_run -nf '#......' -nb '#......' -sf '#......' -sb '#......'", "dmenu_run -nf '#%s' -nb '#%s' -sf '#%s' -sb '#%s' "%(foreground,background,background,colorf),hl)


start = hl[:hl.find('--HERE')]
rest = hl[hl.find('--REST')+7:]


with open (HOME + '/.xmonad/xmonad.hs', 'w') as f:
    f.write(start)
    f.write(insert)
    f.write(rest)

# ------- XMobar ------------------------------------------------

insert = ('"-h","#%s","-l","#%s"' %(colorb, colorf))

with open (HOME + '/.xmonad/xmobar.hs', 'r') as f:
    hl = f.read()


hl = re.sub('"-h","#......","-l","#......"',insert,hl) 
hl = re.sub('bgColor = "#......",','bgColor = "#%s",'%background,hl)
hl = re.sub('fgColor = "#......",','fgColor = "#%s",'%foreground,hl)

with open (HOME + '/.xmonad/xmobar.hs', 'w') as f:
    f.write(hl)


# ------- Homepage -----------------------------------------------


with open(HOME + '/html/style.css', 'r') as f: 
    css = f.read()


inserta = ('/*HERE*/\nbackground-color: #%s;\n/*REST*/' %(background))

starta = css[:css.find('/*HERE*/')]
resta = css[css.find('/*REST*/')+8:]

insert = ('/*HERE*/\ncolor: #%s;\n/*REST*/' %(colorf))

start = resta[:resta.find('/*HERE*/')]
rest = resta[resta.find('/*REST*/')+8:]

reststart = rest[:rest.find('/*HERE*/')]
restrest = rest[rest.find('/*REST*/')+8:]


with open(HOME + '/html/style.css', 'w') as f: 
    f.write(starta)
    f.write(inserta)
    f.write(start)
    f.write(insert)
    f.write(reststart)
    f.write(insert)
    f.write(restrest)


# ------- Firefox -----------------------------------------------

insert = ('/*HERE*/\ncolor:#%s !important;\n/*REST*/' %(colorf))

with open(HOME + '/.mozilla/firefox/irr3wx17.default/chrome/userChrome.css', 'r') as f: 
    css = f.read()

reinsert=('background: #%s !important;' %background)

css = re.sub('background: #...... !important;',reinsert,css) 

start = css[:css.find('/*HERE*/')]
rest = css[css.find('/*REST*/')+8:]



with open(HOME + '/.mozilla/firefox/irr3wx17.default/chrome/userChrome.css', 'w') as f: 
    f.write(start)
    f.write(insert)
    f.write(rest)


# ------- bashrc ------------------------------------------------

insert = ('#HERE/\ncolorf=${%s}\ncolorb=${%s}\n#REST' %(colorfl, colorbl))

with open(HOME + '/.bashrc', 'r') as f: 
    text = f.read()


start = text[:text.find('#HERE')]
rest = text[text.find('#REST')+8:]


with open(HOME + '/.bashrc', 'w') as f: 
    f.write(start)
    f.write(insert)
    f.write(rest)



# ------- Archey3 -----------------------------------------------

colors=['black','red','green','yellow','blue','magenta','cyan','white']


with open (HOME + '/.archey3.cfg', 'r') as f:
    txt = f.read()
print(colors[int(colorfl[5:])%8])
txt = re.sub('color = .*','color = %s'%(colors[int(colorfl[5:])%8]),txt) 

with open (HOME + '/.archey3.cfg', 'w') as f:
    f.write(txt)

# ------- Background --------------------------------------------

os.system('convert -size 100x100 xc:#%s ~/.xmonad/wallpaper.png'%colorb)


# ------- Apply changes -----------------------------------------

os.system('cd ~/.xmonad; ghc -threaded xmonad.hs; mv xmonad xmonad-x86_64-linux; xmonad --restart;')
os.system('feh --bg-fill ~/.xmonad/wallpaper.png')

os.system('killall firefox-aurora')
os.system('xterm -hold -e tty-clock -cs -C %s&' %(int(colorfl[5:])%8))
os.system('xterm -hold -e ~/-Scripts/colors.sh &')
os.system('xterm -hold -e archey3 &')
os.system('xterm -hold -e htop &')
os.system('firefox-aurora &')
