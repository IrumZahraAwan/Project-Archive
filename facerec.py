import cv2,sys,numpy,csv,random
import os

def main():
 fn_haar='haar-face.xml'
 fn_dir='faces'
 
 images = []
 lables = []

 downsize = 4

 names = {}
 colours={}
 id=0
 for subdirs, dirs, files in os.walk(fn_dir):
  for subdir in dirs:
   names[id]=subdir
   colours[id]=(random.randrange(256),random.randrange(256),random.randrange(256))
   subjectpath=os.path.join(fn_dir, subdir)
   for filename in os.listdir(subjectpath):
    path=subjectpath + '/' + filename 
    lable=id
    images.append(cv2.imread(path,0))
    lables.append(int(lable))
   id+=1

 im_width=images[0].shape[0]
 im_height=images[0].shape[1]


 images = numpy.array(images)
 lables = numpy.array(lables)

 model = cv2.createFisherFaceRecognizer()
 model.train(images, lables)

 haar_cascade = cv2.CascadeClassifier(fn_haar)
 webcam = cv2.VideoCapture(0)

 while True:
  rval, frame = webcam.read()
  frame=cv2.flip(frame,1,0)
  gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  minigray = cv2.resize(gray, (gray.shape[1]/downsize,gray.shape[0]/downsize))
  faces = haar_cascade.detectMultiScale(minigray)
  for i in range(len(faces)):
   face_i=faces[i]
   x,y,w,h=[v*downsize for v in face_i]
   face=gray[y:y+h, x:x+w]
   face_resize=cv2.resize(face,(im_width, im_height)) 
   prediction=model.predict(face_resize)
   cv2.rectangle(frame, (x,y), (x+w, y+h), colours[prediction[0]], 3)
   pos_x=x-10
   pos_y=y-10
   cv2.putText(frame, '%s - %.0f'%(names[prediction[0]], 100*(1500-prediction[1])/1500) + '%', (pos_x, pos_y), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255))
  cv2.imshow("faces", frame)
  key=cv2.waitKey(10)
  if key==27:
   break


main()

