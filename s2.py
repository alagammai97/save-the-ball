import turtle
import math
import random
import time
starttime = time.perf_counter()
# creating the background in all 4 sides
al = turtle.Screen()
al.bgcolor('black')
al.title('space invaders')
borderpen = turtle.Turtle()
borderpen.speed(0)
borderpen.color('white')
borderpen.penup()
borderpen.setposition(-300,-300)
borderpen.pendown()
borderpen.turtlesize(3)
side = 600
for _ in range(4):
    borderpen.fd(side)
    borderpen.lt(90)
borderpen.hideturtle()
# creating the player turtle
player = turtle.Turtle()
player.speed(0)
player.turtlesize(5)
player.color('blue')
player.penup()
player.setposition(0,-150)
player.setheading(90)
playerspeed = 15

# move left and key binding
def moveleft():
    x = player.xcor()
    x-=playerspeed
    if x<-230:
        x = -230
    player.setx(x)
turtle.listen()
turtle.onkey(moveleft,'Left')
# move right and key binding
def moveright():
    x = player.xcor()
    x+=playerspeed
    if x> 230:
        x = 230
    player.setx(x)

turtle.listen()
turtle. onkey(moveright,'Right')
# setup score:
score = 0
scorepen = turtle.Turtle()
scorepen.color('white')
scorepen.turtlesize(8)
scorepen.penup()
scorepen.setposition(-290,280)
scorepenstring = 'score: %s' %score
scorepen.write(scorepenstring,False,align = 'left',font =('Arial',14,'normal'))
scorepen.hideturtle()
#enemy red ball
enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.turtlesize(3)
enemy.penup()
enemy.setposition(-200,250)
enemy.speed(0)
enemyspeed = 8
bulletstate ='ready'
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)  
bullet.setheading(90)
bullet.shapesize(1.5,1.5)
bullet.hideturtle()
bulletspeed = 10
# function to be done when bullet is ready
def fullbull():
    global bulletstate
    if bulletstate == 'ready':
        bulletstate = 'fire'
        x = player.xcor()
        y = player.ycor()+10
        bullet.setposition(x,y) 
        bullet.showturtle()
turtle.listen()
turtle.onkey( fullbull,'space')
# collision between player and enemy happens 
def iscollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else :
        return False
# collision is true, number of times is noted and enemy position is reset
while True :
    x = enemy.xcor()
    x+=enemyspeed
    enemy.setx(x)
    if enemy.xcor()>230:
        y = enemy.ycor()
        y-=40
        enemyspeed*=-1
        enemy.sety(y)
    if enemy.xcor()<-230:
         y = enemy.ycor()
         y-=40
         enemy.sety(y)
         enemyspeed*=-1
    if bulletstate == 'fire':
        y = bullet.ycor()
        y+= bulletspeed
        bullet.sety(y)
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate = 'ready'
# collision fun is called to check between bullet and enemy and reset the enemyand bullet
    if iscollision(bullet,enemy):
        bullet.hideturtle()
        bulletstate = 'ready'
        bullet.setposition(0,-340)
        x = random.randint(-200,200)
        y = random.randint(100,250)
        enemy.setposition(x,y)
# update the score
        score +=10
        scorepenstring = 'score: %s' %score
        scorepen.clear()
        scorepen.write(scorepenstring,False,align = 'left',font =('Arial',14,'normal'))
        
# collision fun is called to check between player and enemy and game over
    if iscollision(player,enemy):
        player.hideturtle()
        enemy.hideturtle()
        print('Game over')
        break
# printing a random score, based on how much minutes spent
if starttime >60:
    print('you survived',starttime/4,'minutes')
else :
    print('you survived',starttime,'seconds')
