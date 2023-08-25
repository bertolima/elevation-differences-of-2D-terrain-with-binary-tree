import pygame
from Tree import binaryTree
import numpy as np

class Screen:
    def __init__(self):
        self.width = None
        self.height = None

        self.window = None
        self.clock = None
        self.player_pos = None
        self.running = False

        self.tree = None
        self.pixelList = None

        self.canDraw = True
        self.renderTreeB = True
        self.renderImageB = False
        self.renderImageFiltered = False

        self.treeBackGround = None
        self.treeDepth = 15
        self.flag = 6
        self.treeUpdated = False

        self.initVariables()
        self.initWindow()
        self.initTree()

    def initWindow(self):
        self.window = pygame.display.set_mode((self.width, self.height))
        self.pixelList = self.imp.convert()
        
    def initVariables(self):
        self.running = True
        pygame.init()

        self.imp = pygame.image.load("DEMs/Terreno1K.png")

        self.width = self.imp.get_width()
        self.height = self.imp.get_height()

        self.treeBackGround = pygame.Surface((self.width, self.height))
        self.clock = pygame.time.Clock()

    def initTree(self):
        self.tree = binaryTree(self.width, self.height, self.treeDepth, self.pixelList)
        self.tree.subdivide()

    def poolEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    self.running = False
                elif(event.key == pygame.K_UP):
                    self.pressUp()
                elif(event.key == pygame.K_DOWN):
                    self.pressDown()
                elif(event.key == pygame.K_RIGHT):
                    self.pressRight()
                elif(event.key == pygame.K_LEFT):
                    self.pressLeft()

    def updateTree(self):
        if (not self.treeUpdated):
            self.tree.calculateError(self.pixelList, self.width)
            self.treeUpdated = True

    def renderTree(self):
        if (self.canDraw):
            if(self.renderTreeB):
                self.treeBackGround.fill("black")
                self.tree.draw(self.treeBackGround)
                self.treeBackGround = self.treeBackGround.convert()
                self.canDraw = False

            elif(self.renderImageFiltered):
                self.treeBackGround.fill("black")
                self.tree.drawErro(self.treeBackGround, self.flag)
                self.treeBackGround = self.treeBackGround.convert()
                self.canDraw = False

        if (self.renderImageB):
            self.window.blit(self.imp, (0,0))

        else:
            self.window.blit(self.treeBackGround, (0,0))

    def pressUp(self):
        if (self.renderTreeB):
            self.tree.addDepth(self.pixelList, self.width)
            self.canDraw = True
        elif(self.renderImageFiltered):
            if(self.flag <=51):
                self.flag += 5
                self.canDraw = True
        
    
    def pressDown(self):
        if (self.renderTreeB):
            self.tree.removeDepth()
            self.canDraw = True
        elif(self.renderImageFiltered):
            if(self.flag>=5):
                self.flag -= 5
                self.canDraw = True
        
    def pressRight(self):
        self.canDraw = True
        if(self.renderImageB):
            self.renderImageB = False
            self.renderImageFiltered = True
        elif(self.renderImageFiltered):
            self.renderImageFiltered = False
            self.renderTreeB = True
        else:
            self.renderImageB = True
            self.renderTreeB = False
            
    def pressLeft(self):
        self.canDraw = True
        if(self.renderImageB):
            self.renderImageB = False
            self.renderTreeB = True
        elif(self.renderImageFiltered):
            self.renderImageFiltered = False
            self.renderImageB = True
        else:
            self.renderImageFiltered = True
            self.renderTreeB = False

    def update(self):
        self.poolEvent()
        self.updateTree()
        
    def render(self):
        self.window.fill("black")

        self.renderTree()
        
        pygame.display.flip()
        self.dt = self.clock.tick(144) / 1000
    
    def isRunning(self):
        return self.running
    
    def stop(self):
        pygame.quit()


