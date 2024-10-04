from tkinter import*
import turtle
from time import*
from random import*

#initialising stuff
wow=turtle.Screen()
wow.title("Pac man try.")
#wow.bgcolor("black")
wow.bgpic('dispng.png') # image should be PNG or GIF
#wow.tracer(0)
screenTk=wow.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
draw=turtle.Turtle()
thesemany=2
Wallpellet=turtle.Turtle()
Mpellet=turtle.Turtle()
Apple=turtle.Turtle()
you=turtle.Turtle()
track=turtle.Turtle()
H0=turtle.Turtle()
H1=turtle.Turtle()
H2=turtle.Turtle()
H0.hideturtle()
H1.hideturtle()
H2.hideturtle()
H0.up()
H1.up()
H2.up()
wow.addshape('smolheart.gif')
count=1
lives=3
level=1
wallpellets=0
Mpellets=0
Apples=0
tempdont=0
compspeed=10
started=0
nodiction=5
itsdone=0
dontcheckthese=[draw,Wallpellet,Mpellet,Apple,you,track,H0,H1,H2]
Str=f"Welcome. Avoid skulls and collect as many apples as you can. Controls: w=forward,a=left,d=right\nPellets: \nblue= to destroy walls.\nred= to kill red boxes.\nYou have 3 lives.\nAll The Best."
for i in range(thesemany+1):
        s=f"M{i}=turtle.Turtle()"
        exec(s)
#after ok pressed, game starts.
def Run():
    global thesemany
    global started
    #Game begins
    started=0
    you.home()
    for i in range(level):
        thesemany+=1
        s=f"M{thesemany}=turtle.Turtle()"
        exec(s)
    draw.hideturtle()
    wow.addshape("smolskull.gif")
    for i in wow.turtles():
        i.up()
        i.speed(0.5)
        i.shape("smolskull.gif")
    H0.shape('smolheart.gif')
    H1.shape('smolheart.gif')
    H2.shape('smolheart.gif')
    Wallpellet.color("blue")
    Mpellet.color("red")
    Wallpellet.shape("circle")
    Mpellet.shape("circle")
    wow.addshape("smolaple.gif")
    Apple.shape("smolaple.gif")
    Wallpellet.shapesize(0.5,0.5)
    Mpellet.shapesize(0.5,0.5)
    Apple.shapesize(0.5,0.5)
    draw.color("#0096FF")
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
    track.home()
    track.backward((wow.window_width() / 2) - 10)
    track.left(90)
    track.forward((wow.window_height() / 4) - 20)
    if level==1:
            track.hideturtle()
            track.up()
            track.color("magenta")
            track.write(arg=Str,move=False,align='left',font=("tahoma",20))
            x,y=track.pos()
            track.color('green')
            track.backward(100)
            track.write(arg="(Press 'w' to start.)\n(Can also use arrow\n  keys.)",move=False,align='left',font=("tahoma",20))
    else:
            x,y=track.pos()
    H0.setpos(x+90,y+115)
    H1.setpos(x+120,y+115)
    H2.setpos(x+150,y+115)
    #track.setpos(-760,225)
    track.home()
    track.backward((wow.window_width() / 2) - 10)
    track.left(90)
    track.forward((wow.window_height() / 4) - 20)
    def Keeptrack():
        track.clear()
        track.color('magenta')
        S=f"Level {level}.\nLives: \nScore = {Apples}.\nBlue pellet = {wallpellets}.\nRed pellets = {Mpellets}."
        H0.ht()
        H1.ht()
        H2.ht()
        for i in range(lives):
            s=f"H{i}.showturtle()"
            exec(s)
        track.write(arg=S,move=False,align='left',font=("tahoma",20))
    def Flicker(i):
            for _ in range(20):
                sleep(0.01)
                i.st()
                i.ht()
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
    for i in wow.turtles():
        if i not in dontcheckthese:
            Create(i)
    Create(Mpellet)
    Create(Apple)
    Create(Wallpellet)
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
                            Keeptrack()
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
                            Keeptrack()
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
            i.setx(-500)
            if i==you:
                pass
            else:
                Random(i)
        elif x<-500:
            i.setx(500)
            if i==you:
                pass
            else:
                Random(i)
        if y >300:
            i.sety(-300)
            if i==you:
                pass
            else:
                Random(i)
        elif y<-300:
            i.sety(300)
            if i==you:
                pass
            else:
                Random(i)
    def Dead():
        global lives
        global started
        global wallpellets
        global Mpellets
        global tempdont
        global Apples
        global level
        global count
        global thesemany
        global itsdone
        if started>0:
            if itsdone==0:
                Keeptrack()
                itsdone=1
            for i in wow.turtles():
                if i==you or i==draw or i==track or i==H0 or i==H1 or i==H2:
                    pass
                elif i==Wallpellet:
                    if i.distance(you)<=1:
                        wallpellets+=1
                        track.clear()
                        Keeptrack()
                        Create(i)
                        tempdont=1
                elif i==Mpellet:
                    if i.distance(you)<=1:
                        Mpellets+=1
                        Keeptrack()
                        Create(i)
                        tempdont=1
                elif i==Apple:
                    if i.distance(you)<=1:
                        Apples+=1
                        Keeptrack()
                        Create(i)
                        tempdont=1
                        if Apples%(5*level)==0:
                            Apples=0
                            Keeptrack()
                            level+=1
                            wallpellets=0
                            Mpellets=0
                            Keeptrack()
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
                            Keeptrack()
                            
                else:
                    if i.distance(you)<=1:
                        if Mpellets>(level-1):
                            i.home()
                            Mpellets-=level
                            Keeptrack()
                        else:
                            lives-=1
                            Keeptrack()
                            a=H0
                            if lives==2:
                                a=H2
                            elif lives==1:
                                a=H1
                            Flicker(a)
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
            wow.addshape('gameover.gif')
            draw.home()
            draw.showturtle()
            draw.shape('gameover.gif')
            bye=Label(text=f"GAME OVER.",font=("tahoma",25),background="red").pack()
            compspeed=10000
            lives-=1
            if lives<-1:
                wow.bye()
        if(count%(100//level)==0):
            for i in wow.turtles():
                if i not in dontcheckthese:
                    Random(i)
                    Checking(i)
            Dead()
        if count==3*(100//level):
            if tempdont==0:
                Create(Wallpellet)
                Create(Mpellet)
                Create(Apple)
            else:
                tempdont=0
            count=1
        count+=1
        #wow.update()
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
    wow.onkeypress(a,"A")
    wow.onkeypress(w,"W")
    wow.onkeypress(d,"D")
    wow.onkeypress(a,"Left")
    wow.onkeypress(w,"Up")
    wow.onkeypress(d,"Right")
    wow.listen()
    #defining check for the clock and calling Check to start the clock.
    check=Label()
    Check()
#First instructions
Run()
