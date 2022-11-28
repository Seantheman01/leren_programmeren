from random import randint, random, shuffle
import turtle
import random
screen = turtle.Screen()
screen.bgcolor('lightblue') # background color
color = ['green', 'blue', 'purple','red']
random_color = random.choice(color)
player_one = turtle.Turtle()
player_one.color('red')

player_one.shape('turtle')

x = 0
while x == 0:
  player_one.forward((randint(0, 250)))
  player_one.right((randint(0, 250)))
  player_one.left((randint(0, 250)))
  player_one.backward((randint(0,250)))
  player_one.color(random.choices(color))
  screen.bgcolor('black')
  screen.bgcolor('white')
  player_one.speed('fastest')

turtle.done()