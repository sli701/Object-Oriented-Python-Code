# Simple Timer Example

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
import pyghelpers

# 2 - Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)
TIMER_LENGTH = 2.5  # seconds

def myFunction(theNickname):
    print('In myFunction, timer for', theNickname, 'call back was executed')

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables
headerMessage = pygwidgets.DisplayText(window, (0, 50), 'Click the button to start a ' +
                                       str(TIMER_LENGTH) + ' second timer:', \
                                       fontSize=36, justified='center', width=WINDOW_WIDTH)

startButton = pygwidgets.TextButton(window, (280, 100), 'Start')

clickMeButton = pygwidgets.TextButton(window, (320, 100), 'Click Me')

timerMessage = pygwidgets.DisplayText(window, (0, 160), 'Message showing during timer', \
                                      fontSize=36, justified='center', width=WINDOW_WIDTH)

timerMessage.hide()  # start off with this message hidden
oTimer = pyghelpers.Timer(TIMER_LENGTH, nickname='2.5 second timer',
                          callBack=myFunction)  # create a timer object


# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit pygame and the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if startButton.handleEvent(event):
            oTimer.start()  # start the timer
            startButton.disable()
            timerMessage.show()
            print('Starting timer')

        if clickMeButton.handleEvent(event):
            print('Other button was clicked')

    # 8 - Do any "per frame" actions
    if oTimer.update():  # True here means timer has ended
        startButton.enable()
        timerMessage.hide()
        print('Timer ended')


    # 9 - Clear the screen
    window.fill(WHITE)

    # 10 - Draw all screen elements
    headerMessage.draw()
    startButton.draw()
    clickMeButton.draw()
    timerMessage.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount