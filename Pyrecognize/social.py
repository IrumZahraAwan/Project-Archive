import os, time,select,aiml,sys

def prompt() :
 sys.stdout.write('\r> ')
 sys.stdout.flush()


def speak(response):
 print(response)
 os.system('say "%s" '%response)


def think(timee, nupeople, listpeeople, comfirm, current, recent):

 for person in listpeople:
  
  if person in comfirm:
   comfirm[person]+=1
   if comfirm[person]==5:
    speak('Hello, %s.'%person)
    current[person]=0
    del comfirm[person]
    break
  elif person in current:
   current[person]+=1
  elif person in recent:
   current[person]=0
   del recent[person]
  else:
   comfirm[person]=0

 delete=[]
 for person in comfirm:
  if person not in listpeople:
   comfirm[person]-=2
   if comfirm[person]<0:
    delete.append(person)
 for dl in delete:
  del comfirm[dl]



 delete=[]
 for person in current:
  if person not in listpeople:
   recent[person]=0
   delete.append(person)
 for dl in delete:
  del current[dl]
   



 delete=[]
 for person in recent:
  recent[person]+=1
  if recent[person]>50:
   delete.append(person)
 for dl in delete:
  del recent[dl]


 #print(comfirm, current, recent)

 return comfirm, current, recent
 
######### CHAT ########## 
mia = aiml.Kernel()
for fil in os.listdir('Alice'):
 if fil[0]!='.':
  mia.learn("Alice/%s"%fil)
for fil in os.listdir('Mia'):
 if fil[0]!='.':
  mia.learn("Mia/%s"%fil)
mia.setBotPredicate("name", "Mia")
prompt()
#########################

comfirm={}
current={}
recent={}
listpeople=[]

while True:
 read, write, errors = select.select([sys.stdin], [], [], 0.001)
 for chat in read:
  #print(chat)
  say = sys.stdin.readline()[:-1]
  response=mia.respond(say, (listpeople+['Sir'])[0])
  speak(response)
  prompt()
 with open('people.txt', 'r') as f:
  people=f.read().split('\n')
  if len(people)<2:
   continue
  people = people[-2]
 #21:14:10 2.0: ['Noah Ingham', 'Sophie Ingham']
 timee=people[:8]
 nupeople=people[9:12]
 listpeople=eval(people[14:])
 comfirm, current, recent = think(timee, nupeople, listpeople, comfirm, current,recent)
 time.sleep(1)



