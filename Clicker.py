from turtle import Screen, Turtle
from time import sleep

# Constants
TEXT_COLOR = 'white'

TINY_FONT = ('Arial', 10, 'normal')
SMALL_FONT = ('Arial', 15, 'normal')
MEDIUM_FONT = ('Arial', 20, 'normal')
LARGE_FONT = ('Arial', 24, 'normal')
HUGE_FONT = ('Arial', 35, 'normal')

# Variables
needed_clicks_1 = 5
needed_clicks_2 = 11

clicks = 0
clicks_per_sec = 0
click_value = 1

# Functions
def click(x, y):
    global clicks

    clicks += click_value
    total_clicks.clear()
    total_clicks.write("Clicks: {}".format(round(clicks)), align='center', font=LARGE_FONT)

def upgradeValue():
    global click_value
    global needed_clicks_1
    global clicks

    if clicks >= needed_clicks_1:
        clicks -= needed_clicks_1
        needed_clicks_1 *= 2
        click_value += 2

        total_clicks.clear()
        total_clicks.write("Clicks: {}".format(round(clicks)), align='center', font=LARGE_FONT)

        clicks_needed.clear()
        clicks_needed.write("Clicks needed to upgrade: {}                                                                Clicks needed to upgrade: {}".format(needed_clicks_1, needed_clicks_2), align='center', font=SMALL_FONT)

    else:
        upgrade_man.clear()
        upgrade_man.write('Not enough clicks', align='center', font=SMALL_FONT)
        sleep(0.2)
        upgrade_man.clear()
        upgrade_man.write("Press E to upgrade click value.                            Press Q to upgrade clicks per second.", align='center', font=MEDIUM_FONT)

def upgradeClicks_Per_Sec():
    global clicks_per_sec
    global clicks
    global needed_clicks_2

    if clicks >= needed_clicks_2:
        clicks_per_sec += 1
        clicks -= needed_clicks_2
        needed_clicks_2 *= 2

        total_clicks.clear()
        total_clicks.write("Clicks: {}".format(str(round(clicks))), align='center', font=LARGE_FONT)

        clicks_needed.clear()
        clicks_needed.write("Clicks needed to upgrade: {}                                                                Clicks needed to upgrade: {}".format(needed_clicks_1, needed_clicks_2), align='center', font=SMALL_FONT)

        Clicks_Per_Sec.clear()
        Clicks_Per_Sec.write("Clicks Each Second: {}".format(clicks_per_sec), align='center', font=LARGE_FONT)
    else:
        upgrade_man.clear()
        upgrade_man.write('Not enough clicks', align='center', font=SMALL_FONT)
        sleep(0.2)
        upgrade_man.clear()
        upgrade_man.write("Press E to upgrade click value.                            Press Q to upgrade clicks per second.", align='center', font=MEDIUM_FONT)

def adding_clicks():
    global clicks

    # Add by the clicks per second divided by 8 because we will be adding that number each second divided 8 times to get a more fluid incrementing display
    clicks += clicks_per_sec / 8
    total_clicks.clear()
    total_clicks.write("Clicks: {}".format(round(clicks)), align='center', font=LARGE_FONT)

    # Call adding clicks at 1000 / 8 ms so total clicks updates more fluidly instead of jumping by clicks_per_sec each second 
    screen.ontimer(adding_clicks, 125)

# Adding the screen
screen = Screen()
# Turn off the tracer because we do not need to see any drawing animations
screen.tracer(False)
screen.title("Clicker")
screen.bgcolor("black")
screen.setup(width=1080, height=690)

# Adding turtles
clicks_needed = Turtle()
clicks_needed.hideturtle()
clicks_needed.color(TEXT_COLOR)
clicks_needed.penup()
clicks_needed.goto(-25, -100)
clicks_needed.write("Clicks needed to upgrade: 5                                                                Clicks needed to upgrade: 11", align='center', font=SMALL_FONT)

total_clicks = Turtle()
total_clicks.hideturtle()
total_clicks.color(TEXT_COLOR)
total_clicks.penup()
total_clicks.goto(0, 260)
total_clicks.write("Clicks: 0", align='center', font=LARGE_FONT)

Clicks_Per_Sec = Turtle()  # to avoid clashing with clicks_per_sec
Clicks_Per_Sec.hideturtle()
Clicks_Per_Sec.color(TEXT_COLOR)
Clicks_Per_Sec.penup()
Clicks_Per_Sec.goto(0, 200)
Clicks_Per_Sec.write("Clicks Each Second: 0", align='center', font=LARGE_FONT)

click_here = Turtle()
click_here.hideturtle()
click_here.color(TEXT_COLOR)
click_here.penup()
click_here.goto(0, -200)
click_here.write("CLICK ANYWHERE", align='center', font=HUGE_FONT)

upgrade_man = Turtle()
upgrade_man.hideturtle()
upgrade_man.color(TEXT_COLOR)
upgrade_man.penup()
upgrade_man.goto(0, 100)
upgrade_man.write("Press E to upgrade click value.                          Press Q to upgrade clicks per second.", align='center', font=MEDIUM_FONT)

save_and_quit = Turtle()
save_and_quit.hideturtle()
save_and_quit.color(TEXT_COLOR)
save_and_quit.penup()
save_and_quit.goto(-450, 325)
save_and_quit.write("Press Esc to save and quit", align='center', font=TINY_FONT)

screen.onscreenclick(click)
screen.onkey(upgradeValue, 'e')
screen.onkey(upgradeClicks_Per_Sec, 'q')
screen.listen()

adding_clicks()

screen.mainloop()