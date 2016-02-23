import pygame
import mainp
import cv2

class LBox: # Represents the fractal within itself.
    def __init__(self,color,vertices,pos):
        self.color=color
        self.lastpos=pos
        self.vertices=vertices
        self.target=False
        self.v1, self.v2, self.v3, self.v4=vertices
    
    def render(self,screen):
        pygame.draw.polygon(screen,self.color,(self.v1.pos, self.v2.pos, self.v3.pos, self.v4.pos))
        #if self.target:
        #    pygame.draw.polygon(screen,(145,45,45),(self.v1.pos, self.v2.pos, self.v3.pos, self.v4.pos))
        #    pygame.draw.polygon(screen,self.color,(self.v1+(6,6), self.v2+(-6,6), self.v3+(-6,-6), self.v4+(6,-6)))

           

class Vertice: #Each LBox has four vertices
    def __init__(self,color,pos,size): # initialze the properties of the object
        self.color=color
        self.pos=pos
        self.size=size
        self.lastpos=pos
        self.nb=[]

    def __add__(self, other):
        return (self.pos[0] + other[0], self.pos[1] + other[1])
    
    def render(self,screen):
        self.v1=( self.pos[0]-self.size, self.pos[1]-self.size )
        self.v2=( self.pos[0]+self.size, self.pos[1]-self.size )
        self.v3=( self.pos[0]+self.size, self.pos[1]+self.size )
        self.v4=( self.pos[0]-self.size, self.pos[1]+self.size )
        pygame.draw.polygon(screen,self.color,(self.v1, self.v2, self.v3, self.v4))
        #pygame.draw.circle(screen,self.color,self.pos,self.size)

def plotter(screen,squareList,generations):
    sid=0
    save=''
    for square in squareList:
        i=0
        verts = [vertice.pos for vertice in square.vertices]
        save += str([verts[0]] + [verts[1]] + [verts[3]] + [verts[2]])+ ',\\\n'
        sid+=1
    with open('tmat.py', 'w') as f:
     f.write(save)
    if save:
     img=mainp.plot(eval(save) + (), generations)
     filename='Fractal.png'
     cv2.imwrite(filename, img)
    else:
     filename='Splash.png'
    img=pygame.image.load(filename)
    screen.blit(img,(610,0))
    pygame.display.flip() # update the display
     #screen.tick(1) # only three images per second


def main():
    screen=pygame.display.set_mode((1210,600))
    pygame.display.set_caption('IFS Fractals')
    running=True
    squareList=[]
    mousePressed=False
    mouseDown=False
    rightDown=False
    shiftDown=False
    mouseReleased=False
    generations=4
    target=None
    lasttarget=None
    cols={}
    cid=0
    last=False
    img=pygame.image.load('Splash.png')
    screen.blit(img,(610,0))
    pygame.display.flip() # update the display
    target = special(cols,cid,squareList)
    while running:
        pos=pygame.mouse.get_pos()
        #pos = ( pos[0]-pos[0]%20, pos[1]-pos[1]%20)  #GRID?
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                running=False
                break # get out now
            
            if Event.type == pygame.MOUSEBUTTONDOWN:
                mousePressed=True
                if Event.button==3:
                     rightDown=True
                else:
                     if Event.button==2:
                          shiftDown=True
                     mouseDown=True 
               
            if Event.type == pygame.MOUSEBUTTONUP:
                mouseReleased=True
                mouseDown=False
                rightDown=False
                shiftDown=False
                plotter(screen,squareList,generations)
                last=False

            if Event.type==pygame.KEYDOWN:
                if Event.key in range(49, 58):
                 generations=(Event.key-48)*1
                 plotter(screen,squareList,generations)
                if Event.key==8:
                 squareList=[obj for obj in squareList if obj != lasttarget]
                 if squareList:
                  lasttarget=squareList[-1]
                 else:
                  lasttarget=None
                 plotter(screen,squareList,generations)

             
        if mousePressed==True and pos[0]<=600:
            col=screen.get_at(pos)
            if col[:2]==(0,0):
             if lasttarget:
              lasttarget.target=False
             target=cols[col[2]]
             lasttarget=target
                
            for square in squareList: # search all items
                vertices=square.vertices
                for vertice in vertices:
                    if (pos[0]>=(vertice.pos[0]-vertice.size) and 
                        pos[0]<=(vertice.pos[0]+vertice.size) and 
                        pos[1]>=(vertice.pos[1]-vertice.size) and 
                        pos[1]<=(vertice.pos[1]+vertice.size) ): # inside the bounding box
                        if lasttarget:
                         lasttarget.target=False
                        target=vertice
                        lasttarget=square

            if rightDown and target:
                lasttarget=None
                squareList=[obj for obj in squareList if obj != target]
                plotter(screen,squareList,generations)

            elif target is None:
                x,y=pos
                x = max(min(x, 560),40)
                y = max(min(y, 560),40)
                r=8
                vert1=Vertice((60,80,100),(x-40, y-40),r) # create a new one
                vert2=Vertice((60,80,100),(x+40, y-40),r) # create a new one
                vert3=Vertice((60,80,100),(x+40, y+40),r) # create a new one
                vert4=Vertice((60,80,100),(x-40, y+40),r) # create a new one
                vert1.nb=[vert2, vert4]
                vert2.nb=[vert1, vert3]
                vert3.nb=[vert4, vert2]
                vert4.nb=[vert3, vert1]
                target=LBox((0,0,0+cid), (vert1, vert2, vert3, vert4), pos) # create a new one
                if lasttarget:
                    lasttarget.target=False
                lasttarget=target
                cols[cid]=target
                cid+=1
                squareList.append(target) # add to list of things to draw
            
        if mouseDown and target is not None: # if we are dragging something
            pos=( max(min(pos[0], 600),0),  max(min(pos[1],600),0))
            if target in squareList:
                if not last:
                 last = True
                 target.lastpos=pos # move the target with us
                else:
                 lastpos=target.lastpos
                 mx,my=[pos[0]-lastpos[0], pos[1]-lastpos[1]]
                 for vertice in target.vertices:
                     vpos=vertice.pos
                     mx=600-vpos[0] if vpos[0]+mx >600 else -vpos[0] if vpos[0]+mx<0 else mx
                     my=600-vpos[1] if vpos[1]+my >600 else -vpos[1] if vpos[1]+my<0 else my
                 for vertice in target.vertices:
                     vpos=vertice.pos
                     vertice.pos=[vpos[0]+mx, vpos[1]+my]
                     vertice.lastpos=[vpos[0]+mx, vpos[1]+my]
                 target.lastpos=pos # move the target with us
            elif not shiftDown:
                lastpos=target.lastpos
                mx,my=[pos[0]-lastpos[0], pos[1]-lastpos[1]]

                vertice=target.nb[0]
                newy = 600 if vertice.pos[1]+my >= 599 else 0 if vertice.pos[1]+my < 0 else vertice.pos[1]+my
                vertice.pos=[vertice.pos[0], newy]
                vertice.lastpos=[vertice.pos[0], newy]

                vertice=target.nb[1]
                newx = max(min(vertice.pos[0]+mx,600),0)
                vertice.pos=[newx, vertice.pos[1]]
                vertice.lastpos=[newx, vertice.pos[1]]

                vertice=target
                vertice.pos=(newx, newy)
                vertice.lastpos=pos
            else:
                target.pos=pos
                target.lastpos=pos
        
        if mouseReleased or (mousePressed and pos[0]>600):
            target=None
            
        if lasttarget:
            lasttarget.target=True
            if squareList[-1]!=lasttarget:
                squareList.append(squareList.pop(squareList.index(lasttarget)))

        #screen.fill((255,255,255)) # clear screen
        pygame.draw.polygon(screen, (255,255,255), ((0,0), (600,0), (600, 600), (0, 600)))
        pygame.draw.lines(screen,(145,45,45),1,((95,95), (495,95), (495,495), (95,495)),10)
        for square in squareList:
            square.render(screen)
            for vertice in square.vertices:
                vertice.render(screen)
        pygame.draw.polygon(screen, (145,45,45), ((600,0), (610,0), (610, 600), (600, 600)))
        #pygame.draw.polygon(screen, (255,255,0), ((600,0), (1200,0), (1200, 600), (600, 600)))
            
        mousePressed=False
        mouseReleased=False
        pygame.display.flip()
    return # End of function

def special(cols, cid, squareList):
    r=8
    pos=[0,0]

    vert1=Vertice((60,80,200),(175, 0),r) # create a new one
    vert2=Vertice((60,180,100),(453, 0),r) # create a new one
    vert4=Vertice((60,80,100),(175, 198),r) # create a new one
    vert3=Vertice((60,80,100),(453, 198),r) # create a new one
    vert1.nb=[vert2, vert4]
    vert2.nb=[vert1, vert3]
    vert3.nb=[vert4, vert2]
    vert4.nb=[vert3, vert1]
    target=LBox((0,0,0+cid), (vert1, vert2, vert3, vert4), pos) # create a new one
    cols[cid]=target
    cid+=1
    squareList.append(target) # add to list of things to draw

    vert1=Vertice((60,80,200),(396, 439),r) # create a new one
    vert2=Vertice((60,180,100),(232, 439),r) # create a new one
    vert4=Vertice((60,80,100),(396, 150),r) # create a new one
    vert3=Vertice((60,80,100),(232, 150),r) # create a new one
    vert1.nb=[vert2, vert4]
    vert2.nb=[vert1, vert3]
    vert3.nb=[vert4, vert2]
    vert4.nb=[vert3, vert1]
    target=LBox((0,0,0+cid), (vert1, vert2, vert3, vert4), pos) # create a new one
    cols[cid]=target
    cid+=1
    squareList.append(target) # add to list of things to draw

    vert1=Vertice((60,80,200),(312, 307),r) # create a new one
    vert2=Vertice((60,180,100),(0, 307),r) # create a new one
    vert4=Vertice((60,80,100),(312, 0),r) # create a new one
    vert3=Vertice((60,80,100),(0, 0),r) # create a new one
    vert1.nb=[vert2, vert4]
    vert2.nb=[vert1, vert3]
    vert3.nb=[vert4, vert2]
    vert4.nb=[vert3, vert1]
    target=LBox((0,0,0+cid), (vert1, vert2, vert3, vert4), pos) # create a new one
    cols[cid]=target
    cid+=1
    squareList.append(target) # add to list of things to draw

    [[311, 310], (600, 310), [311, 0], [600, 0]],\

    vert1=Vertice((60,80,200),(311, 310),r) # create a new one
    vert2=Vertice((60,180,100),(600, 310),r) # create a new one
    vert4=Vertice((60,80,100),(311, 0),r) # create a new one
    vert3=Vertice((60,80,100),(600, 0),r) # create a new one
    vert1.nb=[vert2, vert4]
    vert2.nb=[vert1, vert3]
    vert3.nb=[vert4, vert2]
    vert4.nb=[vert3, vert1]
    target=LBox((0,0,0+cid), (vert1, vert2, vert3, vert4), pos) # create a new one
    cols[cid]=target
    cid+=1
    squareList.append(target) # add to list of things to draw

    return target
    
if __name__ == '__main__': # Are we RUNNING from this module?
    main() # Execute our main function

