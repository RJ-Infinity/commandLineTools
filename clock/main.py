import sys
import cal
import datetime

def main(args):
	if len(args) < 2:
		sys.stderr.write("Error Not Enough Arguments Provided")

	if args[1] == "cal":
		cal.main(args)
		return
	
	if args[1] == "date":
		print(datetime.datetime.strptime(input()).__repr__())
		return


if __name__ == "__main__":
	main(sys.argv)