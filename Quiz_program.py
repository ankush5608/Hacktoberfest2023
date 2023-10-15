# Create a Quiz game like Kaun Banega Crorepati(KBC) using lists
name=input("Please tell us your name\n")
print("\nLets welcome our participant",name)

questions=["1. Which is the biggest continent in the world?","2. Which bank is called bankers bank of India?","3. Which is largest animal in the world?","4. Which is largest animal on land","5. Which state has the longest coastal line in India","6. Which Indian state has a separate constitution","7. Which metal is the lightest metal in world","8. LED stands for what"]
answers=["Asia","Reserve Bank of India","Blue whale","African Elephant","Gujarat","Jammu and Kashmir","Lithium","Light Emitting Diode"]
options=[['North America','Asia','Africa','Australia'],['Reserve Bank of India','Punjab National Bank','State Bank of India','ICICI Bank'],['Shark','Blue whale','Elephant','Giraffe'],['Tiger','White Elephant','African Elephant','Crocodile'],['Gujarat','Kerala','Karnataka',
'West Bengal'],['Jammu and Kashmir','West Bengal','Haryana','Goa'],['Zinc','Lithium','Platinum','Gold'],['Light emitting Device','Low emitting Diode','Light electronic Diode','Light Emitting Diode']]
optindex=['b','a','b','c','a','a','b','d']


def optionsavailable(quest,options):
  opop=['a','b','c','d']
  for v in range(4):
    print(opop[v],".",options[quest][v])



def correctans(i,answers,optindex):
  print("\nThe correct answer is",answers[i])
  if correct==0:
    print("\nThe correct answer is option",optindex[i])



correct=1
amount=0
c=1
j=1
quest=0
# while(c!=0):
for i in range(0,len(questions)):
  print("\n\nQuestion number",quest+1,"on your screen\n\n")
  print(questions[i])
  print("\nand the options are\n")
  optionsavailable(quest,options)
  op=input("\nPlease select your option: ")
  if op == optindex[i]:
    amount=2*amount+500*(i+1)
    correctans(i,answers,optindex)
    print("\nCongrats you won",amount)
    quest=quest+1
  elif i==7 and op==optindex[i]:
    print("\ncongrats you take home the amount",amount)
  else:
    correct=0
    print("\nSorry you selected the wrong option")
    correctans(i,answers,optindex)
    if amount==0:
      print("\nSorry you didnt earn anything today \n")
    else:
      print("\ncongrats you take home the amount",amount)
    break





