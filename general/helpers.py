import os
import ctypes
from ctypes import wintypes

def padd(paddFrom:str, paddTo:str, char:str=" ")->str:
	if len(paddFrom) > len(paddTo): return ""
	return char*(len(paddTo) - len(paddFrom))

def OrdinalSuffixOf(i):#https://stackoverflow.com/a/13627586/15755351
	lastDigit = i % 10
	lastTwoDigits = i % 100
	if (lastDigit == 1 and lastTwoDigits != 11): return "st"
	if (lastDigit == 2 and lastTwoDigits != 12): return "nd"
	if (lastDigit == 3 and lastTwoDigits != 13): return "rd"
	return "th"

def longest(items):
	currLongest = -1
	currLongestIndex = None
	for i in items:
		if len(i) > currLongest:
			currLongest = len(i)
			currLongestIndex = i
	return currLongestIndex

def EnableVirtualTerminalProcessing():
	if os.name == "nt":
		kernel32 = ctypes.windll.kernel32
		mode = wintypes.DWORD()
		kernel32.GetConsoleMode(kernel32.GetStdHandle(-11), ctypes.byref(mode))
		kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), mode.value | 0x0004)
