import math
import os
import sys
import timeit
import TermDraw

CHAR_WIDTH, CHAR_HEIGHT = 8, 18

def main(args):pass

if __name__ == "__main__":
	face = TermDraw.Pixels(80*CHAR_WIDTH,80*CHAR_WIDTH)
	face.drawCircle()
	img = face.clone()
	img.renderPixels(CHAR_WIDTH,CHAR_HEIGHT)