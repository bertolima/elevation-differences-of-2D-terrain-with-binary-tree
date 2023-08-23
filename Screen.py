import pygame
from Tree import binaryTree

class Screen:
    def __init__(self):
        self.width = None
        self.height = None

        self.window = None
        self.clock = None
        self.player_pos = None
        self.running = False
        self.dt = 0

        self.tree = None
        self.pixelList = None
        self.renderTreeB = True
        self.renderImageB = False
        self.treeBackGround = None
        self.treeDepth = 5

        self.initVariables()
        self.initWindow()

    def initWindow(self):
        self.window = pygame.display.set_mode((self.width, self.height))

    def initVariables(self):
        self.running = True
        pygame.init()

        self.imp = pygame.image.load("DEMs/test2.jpg")
        self.width = self.imp.get_width()
        self.height = self.imp.get_height()

        self.treeBackGround = pygame.Surface((self.width, self.height))
        self.player_pos = pygame.Vector2( self.width / 2,  self.height / 2)
        self.tree = binaryTree(self.width, self.height, self.treeDepth)

        self.clock = pygame.time.Clock()
    
    def renderTree(self):
        if(self.renderTreeB):
            self.treeBackGround.fill("black")
            self.tree.draw(self.treeBackGround, self.treeDepth)
            self.treeBackGround = self.treeBackGround.convert()
            self.renderTreeB = False
        if (self.renderImageB):
            self.window.blit(self.imp, (0,0))
        else:
            self.window.blit(self.treeBackGround, (0,0))

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

    def updatePlayerPosition(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player_pos.y -= 300 * self.dt
        if keys[pygame.K_s]:
            self.player_pos.y += 300 * self.dt
        if keys[pygame.K_a]:
            self.player_pos.x -= 300 * self.dt
        if keys[pygame.K_d]:
            self.player_pos.x += 300 * self.dt
    # def updateTree(self):
#       self.tree.subdivide()
    def pressUp(self):
        self.treeDepth+=1
        self.tree.addDepth()
        self.renderTreeB = True
    
    def pressDown(self):
        self.treeDepth-=1
        self.tree.removeDepth()
        self.renderTreeB = True

    def pressRight(self):
        if(self.renderImageB):
            self.renderImageB = False
        else:
            self.renderImageB = True



    def renderPlayer(self):
        pygame.draw.circle( self.window, "red", self.player_pos, 40)

    def update(self):
        self.poolEvent()
        self.updatePlayerPosition()
        # self.updateTree()
        
    def render(self):
        self.window.fill("black")

        self.renderTree()
        self.renderPlayer()
        
        
        pygame.display.flip()
        self.dt = self.clock.tick(144) / 1000
    
    def isRunning(self):
        return self.running
    
    def stop(self):
        pygame.quit()


