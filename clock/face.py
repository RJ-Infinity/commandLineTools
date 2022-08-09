import math
import os
import sys
import timeit

chars = [' ', '.', "'", '`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '>', '<', '~', '+', '_', '-', '?', ']', '[', '}', '{', '1', ')', '(', '|', '\\', '/', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']

map = lambda value,fromMin,fromMax,toMin,toMax: toMin+(((value-fromMin)/(fromMax-fromMin))*(toMax-toMin))

CreatePixels = lambda width,height:[[False] * width for _ in range(height)]

def GenerateCircle(pixels,diameter = None):
	if diameter == None:
		diameter = min(len(pixels[0]),len(pixels))
	radius = diameter / 2
	for y in range(diameter):
		for x in range(diameter):
			pixels[y][x] = x == int((-math.sqrt(math.pow(radius,2)-math.pow(y-radius,2))+radius+.5)) or x == int(math.sqrt(math.pow(radius,2)-math.pow(y-radius,2))+radius+.5)
	return pixels


def drawPixels(charWidth,charHeight,pixels):
	WidthInChars = int(len(pixels[0])/charWidth)

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
			binned[i][j] += pixels[y][x]
	maxChar = charWidth*charHeight
	for row in binned:
		for i in row:
			sys.stdout.write(chars[int(map(i,0,maxChar,0,len(chars))+.5)])
		sys.stdout.write("\n")
	sys.stdout.flush()


def main(args):
	width=30
	drawPixels(30)

if __name__ == "__main__":

	CHAR_WIDTH, CHAR_HEIGHT = 8, 18

	p = CreatePixels(80*CHAR_WIDTH,80*CHAR_WIDTH)
	GenerateCircle(p)
	

	drawPixels(CHAR_WIDTH,CHAR_HEIGHT,p)