from datetime import datetime, timedelta
import importlib, math, time

'''
the bots being run through
key = bot name (i.e. "hi" is "hi.py")
value = the condition in which the bot is run (x is the current hour) (i.e. hi runs every 5 hours)
'''
bots = {"hi": lambda x: x % 5 == 0}

def main():
	#find the nearest full hour, and then sleep until that time.
	nearestHour = datetime.now().replace(second=0, microsecond=0, minute=0) + timedelta(hours=math.ceil(datetime.now().minute/60))
	time.sleep((nearestHour-datetime.now()).total_seconds())
	while True:
		#when a full hour is reached, go through each bot
		for bot in bots.keys():
			#if the bot is schduled to post during this time, do so.
			if bots[bot](nearestHour.hour):
				print(bot "is schduled to tweet!")
				process = importlib.import_module(bot)
				process.main()
				print(bot + " processed!")
		#after all bots have been checked, rest until the next hour.
		nearestHour = datetime.now().replace(second=0, microsecond=0, minute=0) + timedelta(hours=math.ceil(datetime.now().minute/60))
		time.sleep((nearestHour-datetime.now()).total_seconds())

if __name__ == "__main__":
    main()