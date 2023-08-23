from Triangle import Triangle
import pygame


class binaryTree:
	def __init__(self, width:float, height:float, depth:int):
		self.imgHeight = height
		self.imgWidth = width
		
		self.pixelList = None

		self.left:Triangle = Triangle((0,0), (width, height), (0, height), 0)
		self.right:Triangle = Triangle((0,0), (width, height), (width, 0), 0)

		self.depth:int = depth

		self.subdivide()
	
	def draw(self, window, maxDepth):
		self.left.draw(window, maxDepth)
		self.right.draw(window, maxDepth)
	
	def subdivide(self):
		self.left.subdivide(self.depth)
		self.right.subdivide(self.depth)

	def addDepth(self):
		self.depth+=1
		self.left.addDepth(self.depth)
		self.right.addDepth(self.depth)
	
	def removeDepth(self):
		self.depth-=1
