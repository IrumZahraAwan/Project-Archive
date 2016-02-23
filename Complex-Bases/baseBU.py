# Draws a representation (argand diagram) of the positive integers of a given complex (interger) base, after converting it to base 10.


import pygame, sys, cmath
pygame.init()
xsize=1280
ysize=800


"""

< 2+0j, 2 >
< 1+1j, 2 >
< 0+2j, 4 >
< 2+2j, 8 >

"""

#def decToBase(integer, base):
#    values = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
#    array = []
#    decimal=integer
#    while integer:
#        integer, value = integer/base,int(integer - (integer/base)*base)
#        array.append(values[value])
#    return ''.join(reversed(array))

def decToBase(integer, base):
    values = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    array = []
    while integer:
        integer, value = integer/base,int(integer - (integer/base)*base)
        array.append(values[value])
    return ''.join(reversed(array))


def baseToDec(n,base):
    values = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    total=0
    for x in range(len(n)):
        total+=values.index(n[-x-1])*base**x
    return total


def argand(base,save):

    screen=pygame.display.set_mode([xsize,ysize])
    if base.imag==0:
        absv=int(abs(base.real))
    else:
        absv=int(  base.real**2 + base.imag**2  )
    if absv>96:
        return
    limit=int(abs(absv**(int(cmath.log(2**16,absv).real))))
    checklist=[]

    screen.fill((0,0,0))
    maxlen=len(decToBase(limit,absv))

    for n in range(limit):
        oddBase=decToBase(n,absv)
        new=baseToDec(oddBase,base)
        #print("%s:  %s"%(oddBase,new))
        #if new in checklist:
        #    raise Exception("Two many digits")
        #checklist+=[new]
        l=len(decToBase(n,absv))
        x,y=int(new.real), int(new.imag)
        #Represent complex point as 2x2 box on argand diagram
        pygame.draw.rect(screen,[0,int((l+0.0)/maxlen*200)+55,int((l+0.0)/maxlen*200)+55],[2*x+xsize/2,-2*y+ysize/2,2,2],0)
        new = "%s \t %s"%(new.real,new.imag)

    pygame.display.flip()
    if save:
        pygame.image.save(screen, "<%s + %si>[0,%s^%s].jpeg"%(base.real, base.imag, absv,cmath.log(limit,absv).real))


if __name__=='__main__':
    for r in range(10):
        for i in range(10):
            if r+i<2:
                continue
            #for rp in [-1, 1]:
            #    for ip in [-1, 1]:
            argand( r + i*1j, 1)
    sys.exit()
    """
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
    """
