from argparse import ArgumentError
import math
import sys
from turtle import clone
from TUI import Seq
map = lambda value,fromMin,fromMax,toMin,toMax: toMin+(((value-fromMin)/(fromMax-fromMin))*(toMax-toMin))

class Pixels:
	def __init__(self,width,height) -> None:
		self.chars = [' ', '.', "'", '`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '>', '<', '~', '+', '_', '-', '?', ']', '[', '}', '{', '1', ')', '(', '|', '\\', '/', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']
		self.__pixels = [[0] * width for _ in range(height)]
	@classmethod
	def __fromPixels(cls,p):
		rv = Pixels(1,1)
		rv.__pixels = [l.copy() for l in p]
		return rv
	def drawCircle(self,diameter = None):
		if diameter == None:
			diameter = min(len(self.__pixels[0]),len(self.__pixels))
		radius = diameter / 2
		for y in range(diameter):
			t = y-radius
			t = math.sqrt((radius*radius)-(t*t))
			value1=int(t+radius+.5)
			value2=int(-t+radius+.5)
			for x in range(diameter):
				self.__pixels[y][x] = x == value1 or x == value2
		return self
	# def drawLine(self,x1,y1,x2,y2):
	# 	if (
	# 		x1<0 or
	# 		x2<0 or
	# 		y1<0 or
	# 		y2<0 or
	# 		x1>len(self.__pixels[0]) or
	# 		x2>len(self.__pixels[0]) or
	# 		y1>len(self.__pixels) or
	# 		y2>len(self.__pixels)
	# 	):
	# 		raise ValueError("the argumnets can not be less than 0 or larger than the size of the Pixels")

		# if x1>=x2:
			# x2,x1=x1,x2

		# # if y1>y2:
		# # 	y2,y1=y1,y2

		# dx = x2 - x1
		# dy = y2 - y1

		# for x in range(x1, x2):
		# 	y = y1 + dy * (x - x1) / dx
		# 	self.__pixels[int(y+0.5)][int(x+0.5)] = 1
	def drawLine(self,x0,y0,x1,y1):
		dx = abs(x1 - x0)
		sx = 1 if x0 < x1 else -1
		dy = -abs(y1 - y0)
		sy = 1 if y0 < y1 else -1
		error = dx + dy
		
		while True:
			try:
				self.__pixels[y0][x0]=1
			except IndexError:pass
			if x0 == x1 and y0 == y1:
				break
			e2 = 2 * error
			if e2 >= dy:
				if x0 == x1:
					break
				error = error + dy
				x0 = x0 + sx
			if e2 <= dx:
				if y0 == y1:
					break
				error = error + dx
				y0 = y0 + sy

	def drawPos(self,x,y,value):
		self.__pixels[y][x] == value
	def clone(self):
		return self.__class__.__fromPixels(self.__pixels)
	def renderPixels(self, charWidth, charHeight,file=sys.stdout):
		WidthInChars = int(len(self.__pixels[0])/charWidth)
		PixelWidth = WidthInChars*charWidth
		HeightInChars = int((PixelWidth/charHeight)+.5)
		binned = [[0] * (WidthInChars+1) for _ in range(HeightInChars+1)]
		i=-1
		for y in range(PixelWidth):
			if y%charHeight == 0:
				i+=1
			j=-1
			for x in range(PixelWidth):
				if x%charWidth == 0:
					j+=1
				binned[i][j] += self.__pixels[y][x]
		maxChar = charWidth*charHeight
		for row in binned:
			for i in row:
				file.write(self.chars[int(map(i,0,maxChar,0,len(self.chars))+.5)])
			file.write("\n")
		file.flush()