from Screen import Screen

# pygame setup
screen = Screen()

while screen.isRunning():
    screen.update()
    screen.render()
screen.stop()
