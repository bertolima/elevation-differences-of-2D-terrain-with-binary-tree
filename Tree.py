from Triangle import Triangle
from collections import deque
import pygame

class binaryTree:
	def __init__(self, width:float, height:float, depth:int, pixelList):
		self.imgHeight = height
		self.imgWidth = width

		self.left:Triangle = Triangle((0,0), (width, height), (0, height), 1)
		self.right:Triangle = Triangle((0,0), (width, height), (width, 0), 1)

		self.depth:int = depth

		self.objects = [None] * (2*(pow(2,self.depth)-1))
	
	def draw(self, window):
		parent:list[Triangle] = deque()
		parent.append(self.left)
		parent.append(self.right)
		child:list[Triangle] = deque()
		for i in range(self.depth-1):
			for node in parent:
				node.draw(window)
				child.append(node.getLeft())
				child.append(node.getRight())

			parent = child
			child:list[Triangle] = deque()
		[objeto.draw(window) for objeto in parent]
	
	def drawErro(self, window):
		parent:list[Triangle] = deque()
		parent.append(self.left)
		parent.append(self.right)
		child:list[Triangle] = deque()
		for i in range(self.depth-1):
			for node in parent:
				if(node.getErro() > 20):
					node.draw(window)
					child.append(node.getLeft())
					child.append(node.getRight())

			parent = child
			child:list[Triangle] = deque()
		[objeto.draw(window) for objeto in parent if objeto.getErro() > 20]
	
	def subdivide(self):
		parent:list[Triangle] = deque()
		parent.append(self.left)
		parent.append(self.right)
		child:list[Triangle] = deque()
		self.objects[0] = self.left
		self.objects[1] = self.right
		j = 2
		for i in range(self.depth-1):
			for node in parent:
				node.subdivide()
				child.append(node.getLeft())
				child.append(node.getRight())
				self.objects[j] = node.getLeft()
				j +=1
				self.objects[j] = node.getRight()
				j +=1

			parent = child
			child:list[Triangle] = deque()
		
	def calculateError(self, pixelList, width):
		[objeto.calcularIntensidadeMedia(pixelList, width) for objeto in self.objects]

	def addDepth(self, pixelList, width):
		size = self.imgWidth * self.imgWidth
		triangles = 2 * pow(2, self.depth-1)
		if(triangles < size):
			self.depth+=1
			self.left.addDepth(self.depth, pixelList, width, self.objects)
			self.right.addDepth(self.depth, pixelList, width, self.objects)
	
	def removeDepth(self):
		if(self.depth >0):
			self.depth-=1
