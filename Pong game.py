
#import library
import pygame
from pygame import mixer
 
#Creating background music
pygame.mixer.init(44100, -16,2,2048)
mixer.music.load("arcade_game.wav")
mixer.music.play(-1)
 
import turtle
import tkinter as tk
 
 
def Gameloop():
    screen = turtle.Screen()
    screen.title("Pong game")
    screen.bgcolor("black")
    screen.setup(width=1000, height=600)
    reg = turtle.Turtle()
    reg.speed(40)
    reg.shape("circle")
    reg.color("blue")
    reg.penup()
    reg.goto(0, 0)
    reg.dx = 5
    reg.dy = -5
    #left pad
    lpad = turtle.Turtle()
    lpad.speed(0)
    lpad.shape("square")
    lpad.color("red")
    lpad.shapesize(stretch_wid=6, stretch_len=1)
    lpad.penup()
    lpad.goto(-400, 0)
    #right pad
    rpad = turtle.Turtle()
    rpad.speed(0)
    rpad.shape("square")
    rpad.color("red")
    rpad.shapesize(stretch_wid=6, stretch_len=1)
    rpad.penup()
    rpad.goto(400, 0)
 
    #start score
    leftplayer = 0
    rightplayer = 0
    sco = turtle.Turtle()
    sco.speed(0)
    sco.color("blue")
    sco.penup()
    sco.hideturtle()
    sco.goto(0, 260)
    sco.write("Left Player : 0    Right Player: 0",align="center", font=("Comic Sans", 30,  "normal"))
    #paddle movements
    def pad1for():
       y = lpad.ycor()
       y += 40
       lpad.sety(y)
    def pad1back():
       y = lpad.ycor()
       y -= 40
       lpad.sety(y)
    def pad2for():
       y = rpad.ycor()
       y += 40
       rpad.sety(y)
    def pad2back():
       y = rpad.ycor()
       y -= 40
       rpad.sety(y)
   
    screen.listen()
    screen.onkeypress(pad1for, "w")
    screen.onkeypress(pad1back, "s")
    screen.onkeypress(pad2for, "Up")
    screen.onkeypress(pad2back, "Down")
    while True:
       screen.update()
       reg.setx(reg.xcor()+reg.dx)
       reg.sety(reg.ycor()+reg.dy)
       if reg.ycor() > 280:
           reg.sety(280)
           reg.dy *= -1
       if reg.ycor() < -280:
           reg.sety(-280)
           reg.dy *= -1
       if reg.xcor() > 500:
           reg.goto(0, 0)
           reg.dy *= -1
           leftplayer += 1
           sco.clear()
           sco.write("Left Player : {}    Right Player: {}".format(leftplayer, rightplayer), align="center",font=("Comic Sans MS", 30, "normal"))
       if reg.xcor() < -500:
           reg.goto(0, 0)
           reg.dy *= -1
           rightplayer += 1
           sco.clear()
           sco.write("Left Player : {}    Right Player: {}".format(leftplayer, rightplayer), align="center", font=("Comic Sans", 30, "normal"))
       #Collision
       if (reg.xcor() > 365 and reg.xcor() < 395) and (reg.ycor() < rpad.ycor()+40 and reg.ycor() > rpad.ycor()-40):
           reg.setx(360)
           reg.dx*=-1
       if (reg.xcor()<-365 and reg.xcor()>-395) and (reg.ycor()<lpad.ycor()+40 and reg.ycor()>lpad.ycor()-40):
           reg.setx(-360)
           reg.dx*=-1
 
# Exit button
# trying to find a way to override the warning for killing a program bc it gives a warning every time i use the exit button if the game is still running
 
def exitGame():
    quit()
   
# Create Starting screen
window = tk.Tk()
window.title('Menu')
window.geometry('200x200')
button1 = tk.Button(text='Start', command=Gameloop)
button2 = tk.Button(text='Exit', command=exitGame)
button1.pack()
button2.pack()
window.mainloop()

