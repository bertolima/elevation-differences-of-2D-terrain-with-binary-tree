from Screen import Screen

#Altere aqui a imagem
img = "DEMs/Terreno1K.png"

# pygame setup
screen = Screen(img)

#gameloop
while screen.isRunning():
    screen.update()
    screen.render()
screen.stop()
