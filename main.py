from Screen import Screen

# pygame setup
screen = Screen()

#gameloop
while screen.isRunning():
    screen.update()
    screen.render()
screen.stop()
