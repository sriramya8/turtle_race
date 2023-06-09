import random
from turtle import Turtle,Screen
tur_lst=[]
colors=["violet","Blue","Green","Yellow","Orange","red"]
s=Screen()
flag=0
ans=""
s.setup(500,400)
inp=s.textinput("Make your bet","Which turtle will win?")
print(inp)

for i in range(0,6):
    t=Turtle("turtle")
    t.penup()
    t.color(colors[i])
    t.goto(-230,-60+20*i)
    tur_lst.append(t)
while(flag==0):

    for tur in tur_lst:
        tur.forward(random.randint(1,100))
        if(tur.xcor()>=230):
            flag=1
            ans=tur.color()[0]
            print("Turtle of color ",tur.color()[0]," is winner")
            break;
if(inp.lower()==ans.lower()):
    print("Your prediction is right!!")
else:
    print("oh!! you lost")
s.exitonclick()


