import sys
import helpers

def parseFlag(flag):
	if flag[0] != "-" and flag[:2] != "--" and flag[0] != "/":
		return False
	if flag[:2] == "--":
		return flag[2:]
	if flag[0] == "-" or flag[0] == "/":
		return flag[1:]



def parseArgs(args:list[str],opts:list[dict])->list[dict]:
	lastFlag = None
	settings = []
	for arg in args:
		if arg[0] == "-" or arg[:2] == "--" or arg[0] == "/":
			if lastFlag == None:
				found = False
				for opt in opts:
					if (
						(parseFlag(arg) == opt["short"] or parseFlag(arg) == opt["full"]) and
						"args" in opt and len(opt["args"])>0
					):
						found = True
						lastFlag = parseFlag(arg)
						settings.append({"name":opt["name"],"args":[]})
				if not found:
					sys.stderr.write(f"Error '{parseFlag(arg)}' is not a valid argument\n")
			else:
				sys.stderr.write(f"Error: The flag '{lastFlag}' requires more arguments\n")
				del settings[-1]
				lastFlag = None
		else:
			found = False
			for opt in opts:
				if not found and lastFlag == opt["short"] or lastFlag == opt["full"]:
					found = True
					if len(settings[-1]["args"]) <= len(opt["args"]):
						try:
							value = opt["args"][len(settings[-1]["args"])]["parse"](arg)
						except:
							sys.stderr.write(f"Error argument '{arg}' not in correct format\nfomat should be {opt['args'][len(settings[-1]['args'])]['format']}\n")
						if (
							value < opt["args"][len(settings[-1]["args"])]["range"][0] or 
							value > opt["args"][len(settings[-1]["args"])]["range"][1]
						):
							sys.stderr.write(
								f"flag {lastFlag}'s "
								f"{len(settings[-1]['args'])+1}"
								f"{helpers.OrdinalSuffixOf(len(settings[-1]['args'])+1)}"
								f" argument must be with in the range {opt['args'][len(settings[-1]['args'])]['range'][0]}"
								f" < x < {opt['args'][len(settings[-1]['args'])]['range'][1]}\n")
							lastFlag = None
							del settings[-1]
						else:
							settings[-1]["args"].append(value)
							if len(opt["args"]) == len(settings[-1]["args"]):
								lastFlag = None

	for opt in opts:
		if len(settings) > 0 and settings[-1]["name"] == opt["name"] and len(settings[-1]["args"]) < len(opt["args"]):
			sys.stderr.write(f"Error: The flag '{lastFlag}' requires more arguments\n")
			del settings[-1]
	sys.stderr.flush()
	return settings