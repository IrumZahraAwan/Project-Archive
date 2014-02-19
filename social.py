import os, random

names = {}
colours={}
id=0
for subdir in os.listdir('faces'):
 if subdir[0]=='.':
  continue
 names[id]=subdir
 colours[id]=(random.randrange(256),random.randrange(256),random.randrange(256))
 subjectpath=os.path.join('faces', subdir)
 for filename in os.listdir(subjectpath+'/Faces'):
  if filename[0]=='.':
   continue
  path=subjectpath + '/Faces/' + filename 
  lable=id
 id+=1

last10=[]
greeted={}
def newp(people):
 global last10
 global greeted
 last10.append([people[p][-1][0] for p in people])
 if len(last10)>10:
  last10.pop(0)
 ids=[inner for outer in last10 for inner in outer]
 for people in ids:
  if people in greeted:
   greeted[people]=greeted[people]-1
   print(greeted[people])
   if greeted[people]<1:
    del greeted[people]
  else:
   inall=True
   for x in last10:
    if people not in x:
     inall=False
   if inall:
    greet(people)
    greeted[people]=10000000

def greet(idn):
 name = names[idn]
 os.system('say "Hello, %s. How are you?" '%name)
 
 

i=0
while True:
 last=0
 if not i%100:
  with open('people.txt', 'r') as f:
   people=f.read().split('\n')[-2]
   timestop = people.find('{')
   lastt,people=int(people[:timestop]), people[timestop:]
   if lastt>last:
    people=people.replace('array(', '')
    people=people.replace(', dtype=int32)', '')
    people=eval(people)
    newp(people)
 i+=1


 
