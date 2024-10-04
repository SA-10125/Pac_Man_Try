from tkinter import*
import turtle
from time import*
from random import*

#initialising stuff
wow=turtle.Screen()
wow.title("Pac man try.")
draw=turtle.Turtle()
M1=turtle.Turtle()
M2=turtle.Turtle()
M3=turtle.Turtle()
M4=turtle.Turtle()
Wallpellet=turtle.Turtle()
Mpellet=turtle.Turtle()
Apple=turtle.Turtle()
you=turtle.Turtle()
count=1
lives=3
level=1
wallpellets=0
Mpellets=0
Apples=0
tempdont=0
compspeed=5#Change this based on your computer speed. #1000 = slowest comp, 5=fastest comp, keep it divisible by 10 please, do not exceed 1000, program will not work.
started=0
nodiction=5
#after ok pressed, game starts.
def Run():
    #Game begins
    draw.hideturtle()
    for i in wow.turtles():
        i.up()
        i.color("red")
        i.speed(0.5)
        i.shape("square")
    Wallpellet.color("blue")
    Apple.color("green")
    Wallpellet.shape("circle")
    Mpellet.shape("circle")
    Apple.shape("circle")
    Wallpellet.shapesize(0.5,0.5)
    Mpellet.shapesize(0.5,0.5)
    Apple.shapesize(0.5,0.5)
    draw.color("blue")
    you.color("green")
    draw.speed(0)
    you.shape("turtle")
    draw.setpos(500,300)
    draw.down()
    #drawing boundaries
    for i in range(0,2):
        draw.right(90)
        draw.forward(600)
        draw.right(90)
        draw.forward(1000)
    draw.down()
    wallver=[]
    wallhor=[]
    for i in range(0,nodiction):
        wallver.append({})
        wallhor.append({})
    #initializing walls
    tempb=randint((level*10),((level+1)*10))
    for i in range(0,tempb):#no of walls = random from level*10 to (level+1)*10
        direction=randint(0,1)#vertical/horizontal
        if direction==0:#vertical
            n=0
            draw.up()
            x=50*(randint(1,9))
            draw.setx(x)#random x position
            for j in range(0,nodiction):
                if x in wallver[j]:
                    pass
                else:
                    n=j
            wallver[n][x]=[]
            y=50*(randint(-5,3))
            draw.sety(y)
            wallver[n][x].append(y)
            draw.down()
            leng=randint(1,2)#length of wall
            for j in range(0,leng):
                y+=50
                draw.sety(y)
                wallver[n][x].append(y)
        else:#horizontal
            n=0
            draw.up()
            y=50*(randint(-4,4))
            draw.sety(y)#random y position
            for j in range(0,nodiction):
                if y in wallhor[j]:
                    pass
                else:
                    n=j
            wallhor[n][y]=[]
            x=50*(randint(-10,8))
            draw.setx(x)
            wallhor[n][y].append(x)
            draw.down()
            leng=randint(1,2)#length of wall
            for j in range(0,leng):
                x+=50
                draw.setx(x)
                wallhor[n][y].append(x)
    draw.up()
    draw.color("white")
    draw.home()
    #random movement function
    def Random(x):
        rand=randint(1,3)
        if rand==1:
            x.forward(50)
        elif rand==2:
             x.right(90)
             x.forward(50)
        elif rand==3:
             x.left(90)
             x.forward(50)
        Checking(x)
    #checking if it is on a wall or a boundary
    def Checking(i):
        global wallpellets
        global level
        global nodiction
        x,y=i.pos()
        x=round(x)
        y=round(y)
        #checking for wall
        for n in range(0,nodiction):
            if x in wallver[n]:
                if y in wallver[n][x]:
                    if i==you:
                        if wallpellets>(level-1):
                            temp=wallver[n][x].index(y)
                            del wallver[n][x][temp]
                            wallpellets-=level
                            bluepellet.config(text=f"Blue pellets = {wallpellets}.")
                        else:
                            if i.heading()==0:
                                i.setx(x-50)
                            elif i.heading()==180:
                                i.setx(x+50)
                            elif i.heading()==90:
                                i.sety(y-50)
                            elif i.heading()==270:
                                i.sety(y+50)
                    else:
                        if i.heading()==0:
                            i.setx(x-50)
                        elif i.heading()==180:
                            i.setx(x+50)
                        elif i.heading()==90:
                            i.sety(y-50)
                        elif i.heading()==270:
                            i.sety(y+50)
            if y in wallhor[n]:
                if x in wallhor[n][y]:
                    if i==you:
                        if wallpellets>(level-1):
                            temp=wallhor[n][y].index(x)
                            del wallhor[n][y][temp]
                            wallpellets-=level
                            bluepellet.config(text=f"Blue pellets = {wallpellets}.")
                        else:
                            if i.heading()==0:
                                i.setx(x-50)
                            elif i.heading()==180:
                                i.setx(x+50)
                            elif i.heading()==90:
                                i.sety(y-50)
                            elif i.heading()==270:
                                i.sety(y+50)
                    else:
                        if i.heading()==0:
                            i.setx(x-50)
                        elif i.heading()==180:
                            i.setx(x+50)
                        elif i.heading()==90:
                            i.sety(y-50)
                        elif i.heading()==270:
                            i.sety(y+50)
        #checking for boundary
        #X=[500,-500]
        #Y=[300,-300]
        if x >500:
            i.setx(500)
            if i==you:
                pass
            else:
                Random(i)
        elif x<-500:
            i.setx(-500)
            if i==you:
                pass
            else:
                Random(i)
        if y >300:
            i.sety(300)
            if i==you:
                pass
            else:
                Random(i)
        elif y<-300:
            i.sety(-300)
            if i==you:
                pass
            else:
                Random(i)
    def Create(i):
        i.hideturtle()
        i.setpos((randrange(-500,500,50)),(randrange(-300,300,50)))
        x,y=i.pos()
        x=round(x)
        y=round(y)
        #checking for wall
        for n in range(0,nodiction):
            if x in wallver[n]:
                if y in wallver[n][x]:
                    Create(i)
            if y in wallhor[n]:
                if x in wallhor[n][y]:
                    Create(i)
        i.showturtle()
    def Dead():
        global lives
        global started
        global wallpellets
        global Mpellets
        global tempdont
        global Apples
        global level
        global count
        if started==1:
            for i in wow.turtles():
                if i==you or i==draw:
                    pass
                elif i==Wallpellet:
                    if i.distance(you)<=1:
                        wallpellets+=1
                        bluepellet.config(text=f"Blue pellets = {wallpellets}.")
                        Create(i)
                        tempdont=1
                elif i==Mpellet:
                    if i.distance(you)<=1:
                        Mpellets+=1
                        redpellet.config(text=f"Red pellets = {Mpellets}.")
                        Create(i)
                        tempdont=1
                elif i==Apple:
                    if i.distance(you)<=1:
                        Apples+=1
                        score.config(text=f"Score = {Apples}.")
                        Create(i)
                        tempdont=1
                        if Apples%(5*level)==0:
                            Apples=0
                            score.config(text=f"Score = {Apples}.")
                            level+=1
                            wallpellets=0
                            Mpellets=0
                            bluepellet.config(text=f"Blue pellets = {wallpellets}.")
                            redpellet.config(text=f"Red pellets = {Mpellets}.")
                            for i in wow.turtles():
                                i.clear()
                                i.home()
                            wallver.clear()
                            wallhor.clear()
                            check.destroy()
                            count=1
                            tempdont=0
                            started=0
                            Run()
                            levels.config(text=f"Level {level}.")
                            
                else:
                    if i.distance(you)<=1:
                        if Mpellets>(level-1):
                            i.home()
                            Mpellets-=level
                            redpellet.config(text=f"Red pellets = {Mpellets}.")
                        else:
                            lives-=1
                            life.config(text=f"Lives = {lives}.")
                            you.home()
    #Clock to keep chcecking the stuff and moving the Ms
    def Check():
        global count
        global lives
        global tempdont
        global compspeed
        Checking(you)
        Dead()
        #checking if dead
        if lives<1:
            wow.bye()
            bye=Label(root,text=f"GAME OVER.",font=("tahoma",25)).pack()
        if(count%(1000//compspeed)==0):
            Random(M1)
            Random(M2)
            Random(M3)
            Random(M4)
            Checking(M1)
            Checking(M2)
            Checking(M3)
            Checking(M4)
            Dead()
        if count==3*(1000//compspeed):
            if tempdont==0:
                Create(Wallpellet)
                Create(Mpellet)
                Create(Apple)
            else:
                tempdont=0
            count=1
        count+=1
        check.after(compspeed,Check)
    #for motion, w,a,d,(no s)
    def a():
        you.left(90)
    def w():
        global started
        started=1
        you.forward(50)
    def d():
        you.right(90)

    wow.onkeypress(a,"a")
    wow.onkeypress(w,"w")
    wow.onkeypress(d,"d")
    wow.listen()
    #defining check for the clock and calling Check to start the clock.
    check=Label()
    Check()
#First instructions
root=Tk()
root.title("Pac man try.")
def OK():
    hi.config(text="",font=("tahoma",1))#cant destroy() labels.
    ok.destroy()
    score.pack()
    life.pack()
    levels.pack()
    redpellet.pack()
    bluepellet.pack()
    Run()
hi=Label(root,text=f"Welcome.\nAvoid red boxes and collect as many apples as you can.\nControls - w=forward,a=left,d=right\nCircles - \nred = pellets to kill red boxes.\nblue = pellets to destroy walls.\ngreen = apples.\nYou have 3 lives.\n All The Best.",font=("tahoma",25),)
hi.pack()#not using grid cause I want it in the center
score=Label(root,text=f"Score = {Apples}",font=("tahoma",25),)
levels=Label(root,text=f"Level {level}.",font=("tahoma",25),)
redpellet=Label(root,text=f"Red pellets =  {Mpellets}.",font=("tahoma",25),)
bluepellet=Label(root,text=f"Blue pellets = {wallpellets}.",font=("tahoma",25),)
life=Label(root,text=f"Lives = {lives}.",font=("tahoma",25),)
ok=Button(root,text="OK",font=("tahoma",25),command=OK)
ok.pack()
