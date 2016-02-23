#!/usr/bin/python
# -*- coding: utf-8 -*-

# Draws a representation (argand diagram) of the positive integers of a given complex (interger) base, after converting it to base 10.

import pygame, sys, cmath

__author__ = 'Noah Ingham'
__email__ = 'noah@ingham.com.au'

pygame.init()
xsize=1280
ysize=800
values = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

def decToBase(whole, base):
    start,fract,neg,end=['']*4
    #Ignore sign until later
    if whole and str(whole)[0]=='-':
        whole=whole*-1
        neg='-'
    #Split up into whole part and not
    if str(whole).find('.')!=-1:
        fract=int(str(whole)[str(whole).find('.')+1])/10.0
        whole=int(whole)
    while whole:
        whole, value = whole/base,int(whole - (whole/base)*base)
        start += values[value]
    while fract and len(end)<30:
        up=str(fract*(base+0.0))
        fract, value = int(up[up.find('.')+1:])/10.0 , int(float(up))
        end+=values[value]
        if fract==0:
            break
    if end!='':
        end='.'+end
    if start+end=='':
        start='0'
    return neg + start[::-1] + end

def baseToDec(n,base):
    total=0
    whole=n
    fract=''
    neg=0
    if n and n[0]=='-':
        n=n[1:]
        neg=1
    if n.find('.')!=-1:
        whole=n[:n.find('.')]
        fract=n[n.find('.')+1:]
    for x in range(len(whole)):
        total+=values.index(whole[-x-1])*base**x
    for x in range(len(fract)):
        total+=values.index(fract[x])*base**(-x-1)
    if neg:
        return -1*total
    return total

def argand(base,save):
    screen=pygame.display.set_mode([xsize,ysize])
    if base.imag==0:
        absv=int(abs(base.real)+0.5)
    else:
        absv= int(abs(base.real)**2+0.5) + int(abs(base.imag)**2+0.5)
    if absv>96:
        return
    if absv==1:
        raise Exception("No support for Base 1.")
    limit=int(absv**(int(cmath.log(2**19,absv).real)))
    checklist=[]

    screen.fill((0,0,0))
    maxlen=len(decToBase(limit,absv))

    for n in range(0,limit):
        oddBase=decToBase(n,absv)
        new=baseToDec(oddBase,base)
        #if new in checklist:
        #    raise Exception('Too many digits! Repeated at %s'%new)
        #checklist+=[new]
        #print("%s \t = %s"%(oddBase, new))
        l=len(decToBase(n,absv))
        x,y=int(new.real), int(new.imag)
        cRatio=int((l+0.0)/maxlen*200)+55
        screen.set_at((1*x+xsize/2,-1*y+ysize/2), (0,cRatio,cRatio))
        new = "%s \t %s"%(new.real,new.imag)

    pygame.display.flip()
    if save:
        pygame.image.save(screen, "<%s + %si>[0,%s^%s].jpeg"%(base.real, base.imag, absv,cmath.log(limit,absv).real))

if __name__=='__main__':
    argand(1.1 + cmath.e/(2**0.5) * 1j,1)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
