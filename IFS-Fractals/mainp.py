import cv2, numpy as np, sys,os
dim=600


def plot(els, gens):
 plain= np.zeros([dim,dim], dtype=np.uint8)
 #plain[:]=100
 for gen in range(gens):

  pts1 = np.float32([[0,0],[dim,0],[0,dim],[dim,dim]])

  warplist = []
  for el in els:
   M=cv2.getPerspectiveTransform(pts1,np.float32(el))
   print(M)
   empty = cv2.warpPerspective(plain,M,(dim,dim),borderValue=(255,255,255))
   warplist.append(empty)

  comb= np.zeros([dim,dim], dtype=np.uint8)
  comb[:]=255
  for warp in warplist: 
   comb = cv2.bitwise_and(comb, warp)
  plain=comb
  if __name__=='__main__':
   cv2.imshow('a', comb)
   cv2.waitKey(0)

 return(comb)

if __name__=='__main__':
 with open('tmat.py', 'r') as f:
  els = eval(f.read())
 comb=plot(els,int(sys.argv[1]))
# tid=max([int(x[:x.find('+')]) for x in os.listdir('Data/Gen') if x[0]!='.']+[1])+1
# cv2.imwrite('Data/Gen/%s.png'%tid, comb)
