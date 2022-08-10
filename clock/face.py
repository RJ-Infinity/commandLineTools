import math
import signal
from time import sleep
from TUI import Seq
import sys
import datetime
import TermDraw
import helpers


CHAR_WIDTH, CHAR_HEIGHT = 8, 18

CrtlC = False

def main(args):pass

if __name__ == "__main__":
	live = True
	def handler(signum, frame):
		global CrtlC
		if signum == 2:
			CrtlC = True

	signal.signal(signal.SIGINT, handler)


	helpers.EnableVirtualTerminalProcessing()

	SIZE = 40
	face = TermDraw.Pixels(SIZE*CHAR_HEIGHT,SIZE*CHAR_HEIGHT)
	face.drawCircle()

	
	r = SIZE//2*CHAR_HEIGHT
	sys.stdout.write(Seq.CursorDown(SIZE+1))

	while True:
		now = datetime.datetime.now().replace(hour=3)
		
		hourX=int((math.sin(math.radians((now.hour*30)%360))*(r-(CHAR_HEIGHT*5))+r))
		hourY=r-int(math.cos(math.radians((now.hour*30)%360))*(r-(CHAR_HEIGHT*5)))
		
		minX=int((math.sin(math.radians((now.minute*6)%360))*(r)+r))
		minY=r-int(math.cos(math.radians((now.minute*6)%360))*(r))

		secX=int((math.sin(math.radians((now.second*6)%360))*(r)+r))
		secY=r-int(math.cos(math.radians((now.second*6)%360))*(r))

		sys.stdout.write(Seq.CursorUp(SIZE+1))

		img = face.clone()
		img.drawLine(r,r,hourX,hourY)
		img.drawLine(r,r,minX,minY)
		img.drawLine(r,r,secX,secY)
		img.renderPixels(CHAR_WIDTH,CHAR_HEIGHT)
		if (not live) or CrtlC:break
		sleep(0.9)
		if (not live) or CrtlC:break