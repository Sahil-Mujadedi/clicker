#Clicker

import turtle
import time
import threading

# Adding the screen
wn = turtle.Screen()
wn.title("Clicker")
wn.bgcolor("black")
wn.setup(width=1080, height=690)
wn.tracer(0)

# Variables
neededclicks1 = 5
neededclicks2 = 10

textcolor = 'white'

clicks = 0
clicks_per_sec = 0
clickvalue = 1

# Adding turtles
clicksneeded = turtle.Turtle()
clicksneeded.speed(0)
clicksneeded.color(textcolor)
clicksneeded.penup()
clicksneeded.hideturtle()
clicksneeded.goto(-25, -100)
clicksneeded.write("Clicks needed to upgrade: 5                                                                Clicks needed to upgrade: 10", align='center', font=('Arial', 15, 'normal'))

totalclicks = turtle.Turtle()
totalclicks.speed(0)
totalclicks.color(textcolor)
totalclicks.penup()
totalclicks.hideturtle()
totalclicks.goto(0, 260)
totalclicks.write("Clicks: 0", align='center', font=('Arial', 24, "normal"))

ClicksPerSec = turtle.Turtle()
ClicksPerSec.speed(0)
ClicksPerSec.color(textcolor)
ClicksPerSec.penup()
ClicksPerSec.hideturtle()
ClicksPerSec.goto(0, 200)
ClicksPerSec.write("Clicks Each Second: 0", align='center', font=('Arial', 24, 'normal'))

ClickHere = turtle.Turtle()
ClickHere.speed(0)
ClickHere.color(textcolor)
ClickHere.penup()
ClickHere.hideturtle()
ClickHere.goto(0, -200)
ClickHere.write("CLICK ANYWHERE", align='center', font=('Arial', 35, 'normal'))

Upgrademan = turtle.Turtle()
Upgrademan.speed(0)
Upgrademan.color(textcolor)
Upgrademan.penup()
Upgrademan.hideturtle()
Upgrademan.goto(0, +100)
Upgrademan.write("Press E to upgrade click value.                          Press Q to upgrade clicks per second.", align='center', font=('Arial', 20, 'normal'))

SaQ = turtle.Turtle()
SaQ.speed(0)
SaQ.color(textcolor)
SaQ.penup()
SaQ.hideturtle()
SaQ.goto(-450, 325)
SaQ.write("Press Esc to save and quit", align='center', font=('Arial', 10, 'normal'))

# Making functions 
def click(uselessparameter1, uselessparameter1point5):
	global clickvalue
	global clicks
	clicks += clickvalue
	totalclicks.clear()
	totalclicks.write("Clicks: {}".format(str(clicks)), align='center', font=('Arial', 24, "normal"))
def upgradeValue():
	global clickvalue
	global neededclicks1
	global clicks
	if clicks >= neededclicks1:
		clicks -= neededclicks1
		neededclicks1 *= 2
		clickvalue += 2
		totalclicks.clear()
		totalclicks.write("Clicks: {}".format(str(clicks)), align='center', font=('Arial', 24, 'normal'))
		clicksneeded.clear()
		clicksneeded.write("Clicks needed to upgrade: {}                                                                Clicks needed to upgrade: {}".format(neededclicks1, neededclicks2), align='center', font=('Arial', 15, 'normal'))
		
	else:
		Upgrademan.clear()
		Upgrademan.write('Not enough clicks', align='center', font=('Arial', 15, 'normal'))
		time.sleep(0.2)
		Upgrademan.clear()
		Upgrademan.write("Press E to upgrade click value.                            Press Q to upgrade clicks per second.", align='center', font=('Arial', 20, 'normal'))

def upgradeClicksPerSec():
	global clicks_per_sec
	global clicks
	global neededclicks2
	if clicks >= neededclicks2:
		clicks_per_sec += 1
		clicks -= neededclicks2
		neededclicks2 *= 2
		totalclicks.clear()
		clicksneeded.clear()
		ClicksPerSec.clear()
		totalclicks.write("Clicks: {}".format(str(clicks)), align='center', font=('Arial', 24, 'normal'))
		clicksneeded.write("Clicks needed to upgrade: {}                                                                Clicks needed to upgrade: {}".format(neededclicks1, neededclicks2), align='center', font=('Arial', 15, 'normal'))
		ClicksPerSec.write("Clicks Each Second: {}".format(clicks_per_sec), align='center', font=('Arial', 24, 'normal'))
	else:
		Upgrademan.clear()
		Upgrademan.write('Not enough clicks', align='center', font=('Arial', 15, 'normal'))
		time.sleep(0.2)
		Upgrademan.clear()
		Upgrademan.write("Press E to upgrade click value.                            Press Q to upgrade clicks per second.", align='center', font=('Arial', 20, 'normal'))
		
def addingclicks():
	global clicks
	global clicks_per_sec
	clicks += clicks_per_sec
	totalclicks.clear()
	totalclicks.write("Clicks: {}".format(str(clicks)), align='center', font=('Arial', 24, 'normal'))


wn.listen()
turtle.onscreenclick(click)
wn.onkey(upgradeValue, 'e')
wn.onkey(upgradeClicksPerSec, 'q')


while True:
	wn.update()
	



