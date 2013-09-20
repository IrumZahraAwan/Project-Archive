import sys
from skimage import filter, io

im = io.imread(sys.argv[1], as_grey=True)
edges2 = filter.canny(im, sigma=1).tolist()
iml = [['1' if x==True else ' ' for x in y] for y in edges2]
height = len(iml) #Used to flip

def fpx(letter): #Returns the top pixels equal to a given letter
    for y in range(height):
        for x in range(len(iml[y])):
            if iml[y][x]==letter and countSurr(x,y,'4')==0:
                return (x,y)
    return False
#Counts number of surrounding pixels equal to a given letter, given an x and y
def countSurr(x, y, letter):
    count = 0
    surrPixels = [[y-1, x-1], [y-1, x], [y-1, x+1], [y, x-1], [y, x+1], [y+1, x-1], [y+1, x], [y+1, x+1]]
    for x in surrPixels:
        if iml[x[0]][x[1]]==letter:
            count += 1
    return count

allPx = []
# Finds the surrounding pixels
def surPx(x,y,direction, newN, save, counter=0, inverting=False):
    iml[y][x]= newN #Changes the pixel value.
    if save:
        global allPx
        allPx.append([x,y])
        save[0].append(x)
        save[1].append(height-y)
    if inverting and iml[y+direction[0]][x] not in [' ', '4']:
        return surPx(x, y+direction[0], direction, newN, save,counter+1)
    if iml[y+direction[0]][x+direction[1]] not in [' ', '4']:
        return surPx(x+direction[1], y+direction[0], direction, newN, save, counter+1)
    if iml[y+direction[0]][x] not in [' ', '4']:
        return surPx(x, y+direction[0], direction, newN, save,counter+1)
    if iml[y][x+direction[1]] not in [' ', '4']:
        return surPx(x+direction[1],y,direction, newN, save,counter+1)
    return (x,y,direction,counter)

xrs,yrs=[],[]
while True:
    onepx = fpx('1') # Finds a starting pixel
    if not onepx:
        break
    (xn, yn, dir, counter) = surPx(onepx[0],onepx[1],[+1,-1], '2', False) #Finds the beginning of that line
    direction=[-1, +1]
    restart = 0
    for x in range(20):
        (xn,yn, dir, counter) = surPx(xn, yn, direction, '4', [xrs, yrs])
        direction = [direction[0]*-1, direction[1]]
        if counter == 0:
            restart+=1
            direction = [direction[0], direction[1]*-1]
        else:
            restart=0
        if restart == 2:
            break
""" Plot
print('Plotting...')
xs = []
ys = []
for y in range(height):
    for x in range(len(iml[y])):
        if iml[y][x] != " ":
            xs.append(x)
            ys.append(height-y)
import matplotlib.pyplot as plt
plt.plot([xs], [ys], '-bo')
plt.plot([xrs],[yrs], '-ro')
plt.show()
"""

# Day 4
# The program can spit out line qeuations, given a series of points.
# Next up is turning an image into a series of points, which can then be plugged into what I have so far.
# This program uses a Threshold, meaning that the points don't have to be exactly on the line of the points before it, but almost on it.

pixels = allPx
from sympy import *

def eqPar(listof3, vert=True): # Given three points, this returns the (unique) equation of the parabola that passes through them.
    (x1,y1),(x2,y2),(x3,y3) = listof3
    if vert:
        equations = [ # Uses simultanous equations
                Eq(S('('+str(x1)+'-h)**2'), S('4*a*('+str(y1)+'-k)')),
                Eq(S('('+str(x2)+'-h)**2'), S('4*a*('+str(y2)+'-k)')),
                Eq(S('('+str(x3)+'-h)**2'), S('4*a*('+str(y3)+'-k)'))]
    else:
        equations = [ # Uses simultanous equations
                Eq(S('('+str(y1)+'-k)**2'), S('4*a*('+str(x1)+'-h)')),
                Eq(S('('+str(y2)+'-k)**2'), S('4*a*('+str(x2)+'-h)')),
                Eq(S('('+str(y3)+'-k)**2'), S('4*a*('+str(x3)+'-h)'))]
    eqs = solve(equations)
    if eqs == []:
        return {}
    eqs=eqs[0]
    return(eqs)

def eqLine(listof2):
    (x1,y1),(x2,y2) = listof2
    if x1!=x2:
        a = (y2-y1)/(x2-x1)
        return {'a':a, 'h':x1, 'k':y1}, 2
    else:
        return{'h':x1}, 3


def evalPar(point,eqD, line, lineType): # Given an x value and an equation, returns the y-value
    x = point[0]
    if lineType==0: # Vertical Parabola
        a,h,k=eqD[Symbol('a')], eqD[Symbol('h')], eqD[Symbol('k')]
        return ((x-h)**2)/(4*a) + k
    if lineType==1: #Horizontal Parabola
        a,h,k=eqD[Symbol('a')], eqD[Symbol('h')], eqD[Symbol('k')]
        return (4*a*(x - h))**0.5 + k
    if lineType==2:
        a,h,k=eqD['a'],eqD['h'],eqD['k']
        return a*(x-h) + k
    if x==eqD['h']:
        return point[1]
    return -10000000

def prettyPar(eqs, lineType): # Prints equations in the classic form.
    if lineType==0:
        print( '(x-%s)^2 = 4 * %s * (y - %s)' %(eqs[Symbol('h')], eqs[Symbol('a')], eqs[Symbol('k')]))
    if lineType==1:
        print( '(y-%s)^2 = 4 * %s * (x - %s)' %(eqs[Symbol('k')], eqs[Symbol('a')], eqs[Symbol('h')]))
    if lineType==2:
        print('y=%s(x-%s) + %s' %(eqs['a'], eqs['h'], eqs['k']))
    if lineType==3:
        print('x=%s' %(eqs['h']))

def eqGeneral(listof3):
    eq = eqVertPar(listof3)
    lineType=0
    if eq == {}:
        eq = eqVertPar(listof3, False)
        lineType=1
    if eq == {}:
        eq,lineType = eqLine([listof3[0], listof3[2]])
    return eq, lineType

notdone,count,lines,thresh,setOfLines=False,3,1,5,[]
eq,lineType = eqGeneral([pixels[0],pixels[1],pixels[2]])
prettyPar(eq, lineType)
while True:
    if len(pixels)<=3:
        print("I'm being used!")
        break
    if abs(evalPar(pixels[3],eq, line, lineType)-pixels[3][1]) > thresh:
        print( str(pixels[0]) +  " to " + str(pixels[2]) + "  Pixels: " + str(count) + "\n")
        pixels = pixels[3:]
        if len(pixels) <3:
            notdone=len(pixels)>0
            break
        eq,lineType = eqGeneral([pixels[0],pixels[1],pixels[2]])
        prettyPar(eq, lineType)
        count = 3
        lines += 1
        continue
    eq,lineType = eqGeneral([pixels[0],pixels[1],pixels[2]])
    pixels.pop(1)
    count += 1
print(pixels[0], " to ", pixels[-1])
if notdone:
    print(pixels)
    print('Straightline')
print(lines)
