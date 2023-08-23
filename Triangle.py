import pygame

class Triangle:
    def __init__(self, p1, p2, p3, depth:int):
        #pontos que formam o triangulo
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        #calculo de ponto medio da hipotenusa
        self.pM = self.calculateMiddlePoint()

        #pointer pra Null
        self.erro = None

        #profundidade do nó atual
        self.depth = depth

        #pointer pros filhos direito e esquerdo
        self.left:Triangle = None
        self.right:Triangle = None

    def calculateMiddlePoint(self):
        return ((self.p1[0]+self.p2[0])/2, (self.p1[1]+self.p2[1])/2)
    
    def draw(self, window, maxDepth):
        if(self.depth == 0):
            pygame.draw.line(window, "white", self.p1, self.p2)
            pygame.draw.line(window, "white", self.p1, self.p3)
            pygame.draw.line(window, "white", self.p2, self.p3)
        pygame.draw.aaline(window, "white", self.p3, self.pM)

        if (self.depth == (maxDepth-1)):
            return
        else:
            self.left.draw(window, maxDepth)
            self.right.draw(window, maxDepth)
        

    def subdivide(self, maxDepth:int):
        if (self.depth == maxDepth):
            return
        else:
            self.left = Triangle(self.p1, self.p3, self.pM, self.depth+1)
            self.right = Triangle(self.p3, self.p2, self.pM, self.depth+1)

            self.left.subdivide(maxDepth)
            self.right.subdivide(maxDepth)

    def addDepth(self, maxDepth):
        if (self.depth == maxDepth-1):
            self.left = Triangle(self.p1, self.p3, self.pM, self.depth+1)
            self.right = Triangle(self.p3, self.p2, self.pM, self.depth+1)
        else:
            self.left.addDepth(maxDepth)
            self.right.addDepth(maxDepth)
    
    def contains(self, p):
        orientacao1 = (self.p2[0] - self.p1[0]) * (p[1] - self.p1[1]) - (p[0] - self.p1[0]) * (self.p2[1] - self.p1[1])
        orientacao2 = (self.p3[0] - self.p2[0]) * ([1] - self.p2[1]) - (p[0] - self.p2[0]) * (self.p3[1] - self.p2[1])
        orientacao3 = (self.p1[0] - self.p3[0]) * (p[1] - self.p3[1]) - (p[0] - self.p3[0]) * (self.p1[1] - self.p3[1])

        if (orientacao1 >= 0 and orientacao2 >= 0 and orientacao3 >= 0) or (orientacao1 <= 0 and orientacao2 <= 0 and orientacao3 <= 0):
            return True
        return False
    
    def calcularIntensidadeMedia(self, pixel_data, imgWidth):
        eMin = 256
        eMax = 0
        sum = 0
        nPixel = 0

        x3 = int(min(self.p1[0], self.p2[0], self.p3[0]))
        x2 = int(max(self.p1[0], self.p2[0], self.p3[0]))
        y3 = int(min(self.p1[1], self.p2[1], self.p3[1]))
        y1 = int(max(self.p1[1], self.p2[1], self.p3[1]))

        #loop que faz o calculo do numero de pixels percorridos e o valor total da intensidade desses pixels
        for x in range(x3+1, x2, 2):
            for y in range(y3+1, y1, 2):
                if (self.contains((x,y))):
                    index = y * imgWidth + x
                    intensidade = pixel_data[index]
                    sum += intensidade
                    nPixel +=1
                    if intensidade > eMax: eMax = intensidade
                    elif intensidade < eMin: eMin = intensidade

        #calculo da media da intensidade de pixel do triangulo
        if (nPixel == 0):
            eMed = 0
        else:
            eMed = sum/nPixel

        self.erro = max(abs(eMin - eMed), abs(eMax - eMed))

    