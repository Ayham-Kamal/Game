import turtle
import time

'''
This is a multiplayer Game, where player 1 plays using 
arrows to survive obstacles sent by player 2.
player 2, can send obstacles using 'A','S','D','F' KEYS, 
and 'G' KEY can be used to to restore initial positions 
for these obstacles. 'Z','X','C','V','B','N' KEYS can also
be used to send other obstacles, and 'SPACE' key can be used
to restore initial positions for these obstacles. 
If player 1 wasn't hit by any oblstacles during the first 
60 seconds player 1 wins. Otherwise, player 2 wins.
'''

#draw the border
border=turtle.Turtle()
border.color("red")
border.ht()
border.speed(0)
border.penup()
border.goto(-290,250)
border.pendown()
border.width(3)
border.forward(580)
border.right(90)
border.forward(525)
border.right(90)
border.forward(580)
border.right(90)
border.forward(525)

#The timer.
l=60
the_timer=turtle.Turtle()
the_timer.speed(0)
the_timer.penup()
the_timer.goto(70,253)
the_timer.fillcolor("black")
the_timer.write("The time remaining = " + str(l), font=("Keter YG", 15, 'normal', 'bold', 'underline'))
the_timer.ht()

#call the obstacles
t1=turtle.Turtle()
t1.ht()
t1.speed(0)
t2=turtle.Turtle()
t2.ht()
t2.speed(0)
t3=turtle.Turtle()
t3.ht()
t3.speed(0)
t4=turtle.Turtle()
t4.ht()
t4.speed(0)
t5=turtle.Turtle()
t5.ht()
t5.speed(0)
t6=turtle.Turtle()
t6.ht()
t6.speed(0)
x=-270
y=235
screen=turtle.Screen()
screen.bgcolor("turquoise")


t1.penup()
t1.goto(x,y)
t1.shape("circle")
t1.color("red")
t1.right(90)

x=x+105
t2.penup()
t2.goto(x,y)
t2.shape("circle")
t2.color("red")
t2.right(90) 

x=x+105
t3.penup()
t3.goto(x,y)
t3.shape("circle")
t3.color("red")
t3.begin_fill()
t3.end_fill()
t3.right(90) 

x=x+115
t4.penup()
t4.goto(x,y)
t4.shape("circle")
t4.color("red")
t4.right(90) 

x=x+105
t5.penup()
t5.goto(x,y)
t5.shape("circle")
t5.color("red")
t5.begin_fill()
t5.end_fill()
t5.right(90) 

x=x+105
t6.penup()
t6.goto(x,y)
t6.shape("circle")
t6.color("red")
t6.right(90)

#THe player 
the_player=turtle.Turtle()
the_player.speed(0)
the_player.color("#33090d")
the_player.ht()
the_player.penup()
the_player.goto(0,-250)
the_player.left(90)
the_player.st()
the_player.shape("turtle")

#The new obstacles
sq1=turtle.Turtle()
sq1.ht()
sq1.speed(0)
sq1.penup()
sq1.goto(275,200)
sq1.shape("square")
sq1.color("green")
sq1.right(180) 

sq2=turtle.Turtle()
sq2.ht()
sq2.speed(0)
sq2.penup()
sq2.goto(275,-230)
sq2.shape("square")
sq2.color("green")
sq2.right(180)

sq3=turtle.Turtle()
sq3.ht()
sq3.speed(0)
sq3.penup()
sq3.goto(-270,80)
sq3.shape("square")
sq3.color("green")

sq4=turtle.Turtle()
sq4.ht()
sq4.speed(0)
sq4.penup()
sq4.goto(-270,-115)
sq4.shape("square")
sq4.color("green")

tr=turtle.Turtle()
tr.ht()
tr.speed(0)
tr.penup()
tr.goto(0,235)
tr.shape("triangle")
tr.color("yellow")
tr.right(90)

#controling.

def m():
  tr.st()
  tr.speed(1)
  for i in range(515):
    tr.forward(1)
screen.onkey(m,'m')  


def a():
  sq1.st()
  sq1.speed(1)
  for q in range(570):  
    sq1.forward(1)
  
screen .onkey(a,'a') 

def s():
  sq2.st()
  sq2.speed(1)
  for w in range(570):
    sq2.forward(1)
screen .onkey(s,'s')

def d():
  sq3.st()
  sq3.speed(1)
  for e in range(570):
    sq3.forward(1)
screen .onkey(d,'d')

def f():
  sq4.st()
  sq4.speed(1)
  for r in range(570):
    sq4.forward(1)
screen .onkey(f,'f')


def g():
  sq1.ht()
  sq1.speed(0)
  sq1.goto(275,200)
  sq2.ht()
  sq2.speed(0)
  sq2.goto(275,-230) 
  sq3.ht()
  sq3.speed(0)
  sq3.goto(-270,80)
  sq4.ht()
  sq4.speed(0)
  sq4.goto(-270,-115) 
screen.onkey(g,'g')



def right():
  the_player.right(20)
  
screen.onkey(right,'right')

def left():
  the_player.left(20)
  
screen.onkey(left,'left')

def up():
  the_player.forward(10)
  if the_player.ycor()>= 250:
    the_player.backward(20)
  
  elif the_player.xcor()>=290:
    the_player.backward(20)  

  elif the_player.ycor()<=-275:
    the_player.backward(20)

  elif the_player.xcor()<=-290:
    the_player.backward(20)

screen.onkey(up,'up')


def z():
  t1.st()
  t1.speed(0)
  for t in range(515):
    t1.forward(1)
screen.onkey(z,'z')

def x ():
  t2.st()
  t2.speed(1)
  for y in range(515):
    t2.forward(1)
screen.onkey(x,'x')

def c ():
  t3.st()
  t3.speed(0)
  for u in range(515):
    t3.forward(1)
screen.onkey(c,'c')

def v ():
  t4.st()
  t4.speed(1)
  for i in range(515):
    t4.forward(1)
screen.onkey(v,'v')

def b ():
  t5.st()
  t5.speed(1)
  for o in range(515):
    t5.forward(1)
screen.onkey(b,'b')

def n ():
  t6.st()
  t6.speed(1)
  for p in range(515):
    t6.forward(1)
screen.onkey(n,'n')

def space():
  t1.ht()
  t1.speed(0)
  t1.goto(-270,235)
  t2.ht()
  t2.speed(0)
  t2.goto(-165,235) 
  t3.ht()
  t3.speed(0)
  t3.goto(-60,235)
  t4.ht()
  t4.speed(0)
  t4.goto(45,235)
  t5.ht()
  t5.speed(0)
  t5.goto(150,235)
  t6.ht()
  t6.speed(0)
  t6.goto(255,235)
  tr.ht()
  tr.speed(0)
  tr.goto(0,235)
screen.onkey(space,'space')

screen.listen()  

def check_collision(distance, player, obstacle):
  if player.distance(obstacle.xcor(), obstacle.ycor()) < distance:
    return True

the_result=turtle.Turtle()
the_result.ht()

start_time=time.time()

gameOn = True
while gameOn == True:
  t=int(60-(time.time()-start_time))
  the_timer.clear()
  the_timer.write("The time remaining = " + str(t), font=("Keter YG", 15, 'normal', 'bold' 'underline'))

  if t<=0:
      the_result.speed(0)
      the_result.ht()
      the_result.penup()
      the_result.goto(-160,0)
      the_result.fillcolor("orange")
      the_result.write("Player 1 wins" , font=("Keter YG", 45, 'normal', 'bold', 'underline'))
      break

  
  if check_collision(30, the_player, tr):

    the_result.speed(0)
    the_result.penup()
    the_result.goto(-160,0)
    the_result.hideturtle()
    the_result.fillcolor("orange")
    the_result.write("Player 2 wins" , font=("Keter YG", 45, 'normal', 'bold', 'underline'))
    break

  if check_collision(30, the_player, sq1):
      the_result=turtle.Turtle()
      the_result.speed(0)
      the_result.ht()
      the_result.penup()
      the_result.goto(-160,0)
      the_result.fillcolor("orange")
      the_result.write("Player 2 wins" , font=("Keter YG", 45, 'normal', 'bold', 'underline'))
      break

    
  if check_collision(30, the_player, sq2):
      the_result=turtle.Turtle()
      the_result.speed(0)
      the_result.ht()
      the_result.penup()
      the_result.goto(-160,0)
      the_result.fillcolor("orange")
      the_result.write("Player 2 wins" , font=("Keter YG", 45, 'normal', 'bold', 'underline'))
      break
   
  if check_collision(30, the_player, sq3):
    the_result=turtle.Turtle()
    the_result.speed(0)
    the_result.ht()
    the_result.penup()
    the_result.goto(-160,0)
    the_result.fillcolor("orange")
    the_result.write("Player 2 wins" , font=("Keter YG", 45, 'normal', 'bold', 'underline'))
    break

  if check_collision(30, the_player, sq4):
    the_result=turtle.Turtle()
    the_result.speed(0)
    the_result.ht()
    the_result.penup()
    the_result.goto(-160,0)
    the_result.fillcolor("orange")
    the_result.write("Player 2 wins" , font=("Keter YG", 45, 'normal', 'bold', 'underline'))
    break
    
  if check_collision(30, the_player, t1):
    the_result=turtle.Turtle()
    the_result.speed(0)
    the_result.ht()
    the_result.penup()
    the_result.goto(-160,0)
    the_result.fillcolor("orange")
    the_result.write("Player 2 wins" , font=("Keter YG", 45, 'normal', 'bold', 'underline'))
    break
 
  if check_collision(30, the_player, t2):
    the_result=turtle.Turtle()
    the_result.speed(0)
    the_result.ht()
    the_result.penup()
    the_result.goto(-160,0)
    the_result.fillcolor("orange")
    the_result.write("Player 2 wins" , font=("Keter YG", 45, 'normal', 'bold', 'underline'))
    break

  if check_collision(30, the_player, t3):
    the_result=turtle.Turtle()
    the_result.speed(0)
    the_result.ht()
    the_result.penup()
    the_result.goto(-160,0)
    the_result.fillcolor("orange")
    the_result.write("Player 2 wins" , font=("Keter YG", 45, 'normal', 'bold', 'underline'))
    break
    
  if check_collision(30, the_player, t4):
    the_result=turtle.Turtle()
    the_result.speed(0)
    the_result.ht()
    the_result.penup()
    the_result.goto(-160,0)
    the_result.fillcolor("orange")
    the_result.write("Player 2 wins" , font=("Keter YG", 45, 'normal', 'bold', 'underline'))
    break

  if check_collision(30, the_player, t5):
    the_result=turtle.Turtle()
    the_result.speed(0)
    the_result.ht()
    the_result.penup()
    the_result.goto(-160,0)
    the_result.fillcolor("orange")
    the_result.write("Player 2 wins" , font=("Keter YG", 45, 'normal', 'bold', 'underline'))
    break

  if check_collision(30, the_player, t6):
    the_result=turtle.Turtle()
    the_result.speed(0)
    the_result.ht()
    the_result.penup()
    the_result.goto(-160,0)
    the_result.fillcolor("orange")
    the_result.write("Player 2 wins" , font=("Keter YG", 45, 'normal', 'bold', 'underline'))
    break  
  
  

  time.sleep(0.5)