import math
import os
import sys
import timeit
import TermDraw

CHAR_WIDTH, CHAR_HEIGHT = 8, 18

def main(args):pass

if __name__ == "__main__":
	SIZE = 80
	face = TermDraw.Pixels(SIZE*CHAR_WIDTH,SIZE*CHAR_WIDTH)
	face.drawCircle()
	img = face.clone()
	img.drawLine(SIZE//2*CHAR_WIDTH,SIZE//2*CHAR_WIDTH,100,100)
	img.renderPixels(CHAR_WIDTH,CHAR_HEIGHT)