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

xterm = ('XTerm*Background: #1f1f1f\n\
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
*xterm*color0: #101010\n\
! Red
*xterm*color1: #%s\n\
! Green
*xterm*color2: #%s\n\
! 
*xterm*color3: #c47f2c\n\
*xterm*color4: #30309b\n\
*xterm*color5: #7e40a5\n\
*xterm*color6: #3579a8\n\
*xterm*color7: #9999aa\n\
*xterm*color8: #303030\n\
*xterm*color9: #ff0090\n\
*xterm*color10: #80ff00\n\
*xterm*color11: #ffba68\n\
*xterm*color12: #5f5fee\n\
*xterm*color13: #bb88dd\n\
*xterm*color14: #4eb4fa\n\
*xterm*color15: #d0d0d0' %(color1, color2)) 

with open(HOME+'/XTerm', 'w+') as f:
    f.write(xterm)


# ------- XMonad ------------------------------------------------

insert = ('-- HERE\ncolor1 = "#%s"\ncolor2 = "#%s"\n-- DONE' %(color1, color2))

with open (HOME + '/.xmonad/xmonad.hs', 'r') as f:
    hl = f.read()

start = hl[:hl.find('-- HERE')]
rest = hl[hl.find('-- DONE')+7:]


with open (HOME + '/.xmonad/xmonad.hs', 'w') as f:
    f.write(start)
    f.write(xmonad)
    f.write(rest)


# ------- Homepage -----------------------------------------------

insert = ('/*HERE*/\ncolor=#%s\n/*REST*/' %(color1))

with open(HOME + '/html/style.css', 'r') as f: 
    css = f.read()


start = css[:css.find('/*HERE*/')]
rest = css[css.find('/*REST*/')+8:]


with open(HOME + '/html/style.css', 'w') as f: 
    f.write(start)
    f.write(insert)
    f.write(rest)


# ------- Firefox -----------------------------------------------

insert = ('/*HERE*/\ncolor=#%s !important\n/*REST*/' %(color1))

with open(HOME + '/.mozilla/firefox/*.default/chrome/userChrome.css', 'r') as f: 
    css = f.read()


start = css[:css.find('/*HERE*/')]
rest = css[css.find('/*REST*/')+8:]


with open(HOME + '/.mozilla/firefox/*.default/chrome/userChrome.css', 'w') as f: 
    f.write(start)
    f.write(insert)
    f.write(rest)


os.system('cd ~/.xmonad; ghc -threaded xmonad.hs; mv xmonad xmonad-x86_64-linux; xmonad --restart;')
os.system('convert -size 100x100 xc:#%s ~/.xmonad/wallpaper.png'%color1)
os.system('feh --bg-fill ~/.xmonad/wallpaper.png &')
