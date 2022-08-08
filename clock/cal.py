import datetime
import calendar
import sys
import time
from TUI import Seq
import helpers
from parseArgs import parseArgs


def main(args):
	settings = parseArgs(args[2:],[
		{
			"full":"month","short":"m","name":"month","args":[
				{"parse":int,"range":[1,12],"format":"integer between 1 and 12 (inclusive)"}
			]
		},
		{
			"full":"year","short":"y","name":"year","args":[
				{"parse":int,"range":[1,9999],"format":"integer between 1 and 12 (inclusive)"}
			]
		}
	])

	keys = [s["name"] for s in settings]

	helpers.EnableVirtualTerminalProcessing()

	# timeZone = time.tzname[0 if time.localtime().tm_isdst == 0 else 1]
	# utcTime = "UTC Time"
	timeNow = datetime.datetime.now()
	# timeNow = timeNow.replace(day=31)
	displayTime = timeNow
	print(keys)
	if "month" in keys:
		displayTime = displayTime.replace(
			month=list(filter(
				lambda arg:arg["name"] == "month",
				settings
			))[0]["args"][0])
	if "year" in keys:
		displayTime = displayTime.replace(
			year=list(filter(
				lambda arg:arg["name"] == "year",
				settings
			))[0]["args"][0])
	monthrange = calendar.monthrange(displayTime.year,displayTime.month)
	weekOffset = datetime.timedelta(monthrange[0])

	sys.stdout.write(
		# f"{timeZone}: {helpers.padd(timeZone,utcTime)}{timeNow:%d/%m/%Y %I:%M:%S %p}\n"
		# f"{utcTime}: {helpers.padd(utcTime,timeZone)}{datetime.datetime.utcnow():%d/%m/%Y %I:%M:%S %p}\n\n"
		f"{timeNow:%A} {str(timeNow.day)}{helpers.OrdinalSuffixOf(timeNow.day)} {timeNow:%B} {str(timeNow.year)}\n\n"+
		#month
		# (Seq.CharRendition(Seq.BrightFgBlack) if displayTime.year != timeNow.year else "")+
		"\n".join([
			" ".join([
				(Seq.CharRendition(Seq.BgWhite)+Seq.CharRendition(Seq.FgBlack)if timeNow.month == i+j and displayTime.year == timeNow.year else '')+
				calendar.month_name[i+j]+
				helpers.padd(calendar.month_name[i+j],helpers.longest(calendar.month_name)+" ")+
				(Seq.CharRendition(Seq.Default)if timeNow.month == i+j and displayTime.year == timeNow.year else '')
				for j in range(1,13,4)
			])
			for i in range(4)
		])+Seq.CharRendition(Seq.Default)+
		f"\n\n{calendar.month_name[displayTime.month]} {displayTime.year}\n"+
		#day collumns
		" ".join([calendar.day_abbr[i] for i in range(7)])+"\n"+
		("" if (displayTime.month == 1 and timeNow.month == 12 and timeNow.year == displayTime.year-1) or
			(displayTime.month-1 == timeNow.month and displayTime.year == timeNow.year)
			else displayTime.month)+
		#last month
		"".join([
			(Seq.CharRendition(Seq.BgWhite)+Seq.CharRendition(Seq.FgBlack) if
				date == timeNow.day and
				(displayTime.month-1 == timeNow.month and displayTime.year == timeNow.year) or
				(displayTime.month == 1 and timeNow.month == 12 and timeNow.year == displayTime.year-1) else"")+
			str(date)+helpers.padd(str(date),helpers.longest(calendar.day_abbr))+
			(Seq.CharRendition(Seq.Default) if
				date == timeNow.day and
				(displayTime.month-1 == timeNow.month and displayTime.year == timeNow.year) or
				(displayTime.month == 1 and timeNow.month == 12 and timeNow.year == displayTime.year-1) else"")+" "
			for date in [
				(displayTime.replace(day=1) - weekOffset + datetime.timedelta(i)).day
				for i in range(weekOffset.days)
			]
		])+(Seq.CharRendition(Seq.Default) if displayTime.month == timeNow.month and displayTime.year == timeNow.year else Seq.CharRendition(Seq.BrightFgBlack))+
		#days
		"".join([
			("\n"if displayTime.replace(day=date).weekday()==0 and date > 1 else"")+
			(Seq.CharRendition(Seq.BgWhite)+Seq.CharRendition(Seq.FgBlack) if date == timeNow.day and displayTime.month == timeNow.month and displayTime.year == timeNow.year else"")+
			str(date)+helpers.padd(str(date),helpers.longest(calendar.day_abbr))+
			(Seq.CharRendition(Seq.Default) if date == timeNow.day else"")+" "+
			("" if displayTime.month == timeNow.month and displayTime.year == timeNow.year else Seq.CharRendition(Seq.BrightFgBlack))
			for date in range(1,monthrange[1]+1)
		])+Seq.CharRendition(Seq.BrightFgBlack)+
		#next month
		"".join([
			str(date)+helpers.padd(str(date),helpers.longest(calendar.day_abbr)+" ")
			for date in range(1, 8-(calendar.monthrange(
				displayTime.year if displayTime.month!=12 else (displayTime.year+1),
				displayTime.month+1 if displayTime.month!=12 else 1
			)[0] or 8))
		])+Seq.CharRendition(Seq.Default)+"\n"
	)
if __name__ == "__main__":
	main(['C:\\Users\\rjinf\\RJ_Infinity\\workspace\\commandLineTools\\\\clock\\main.py', 'cal', '-m', '1','/y' ,'2020'])