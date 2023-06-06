import os
import json


class SpireRun:
	def __init__(self,filename):
		self.fileInfo = self.processRun(filename)
		fileInfoString = self.fileInfo
		for key in fileInfoString:
			try:
				exec("self."+key+"="+str(fileInfoString[key]))

			#for individual errors
			except SyntaxError as e: 
				if key == "play_id":
					self.play_id = fileInfoString[key]
				elif key == "build_version":
					self.build_version = fileInfoString[key]
				elif key == "killed_by":
					self.killed_by = fileInfoString[key]
				elif key == "neow_cost":
					self.neow_cost = fileInfoString[key]
				elif key == "neow_bonus":
					self.neow_bonus = fileInfoString[key]
				else:	
					print("\""+key+"\"",e)

			#for Strings in dictionnary		
			except NameError: exec("self."+key+"=\""+fileInfoString[key]+"\"")

	def allInfo(self):
		return sorted(list(self.fileInfo.keys()))
	
	def getMetaData(self):
		return  ("build_version: "+str(self.build_version)
				+"\nchose_seed: "+str(self.chose_seed)
				+"\nseed_played: "+str(self.seed_played)
				+"\nseed_source_timestamp: "+str(self.seed_source_timestamp)
				+"\nlocal_time: "+str(self.local_time)
				+"\nplay_id: "+str(self.play_id)
				+"\ntimestamp: "+str(self.timestamp))
				
	
	def getGamemode(self):
		gamemode = ""
		if self.is_ascension_mode:
			gamemode+="Ascension mode level "+str(self.ascension_level)+"\n"
		if self.is_daily:
			gamemode+="Daily mode \n"
		if self.is_endless:
			gamemode+="Endless mode \n"
		if self.is_trial:
			gamemode+="Trial mode \n"
		if gamemode == "": gamemode = "Normal mode \n"

		if len(gamemode)>25:
			gamemode = "Custom mode: \n"+gamemode
		
		return gamemode+"Character: "+str(self.character_chosen)+"\n"

	def getSummary(self):
		return self.getGamemode()+("Result: "+("Victory\n" if self.victory else "Defeat\n")
			   +"Floor reached: "+str(self.floor_reached)+"\n"
			   +"Score: "+str(self.score))

	def processRun(self,filename):
		with open(filename,'r') as runfile:
			return json.load(runfile)
		


def loadIroncladRuns():
	return [SpireRun("runs/IRONCLAD/"+file) for file in os.listdir("runs/IRONCLAD")]

def loadTheSilentRuns():
	return [SpireRun("runs/THE_SILENT/"+file) for file in os.listdir("runs/THE_SILENT")]

def loadDefectRuns():
	return [SpireRun("runs/DEFECT/"+file) for file in os.listdir("runs/DEFECT")]

def loadWatcherRuns():
	return [SpireRun("runs/WATCHER/"+file) for file in os.listdir("runs/WATCHER")]



def main():
	run1 = SpireRun("runs/THE_SILENT/1543965538.run")
	
	#print(run1.allInfo())
	#print(run1.purchased_purges)
	print(run1.getMetaData())
	print(run1.getGamemode())
	print()
	print(run1.getSummary())
	#ironclad_runs = loadIroncladRuns()
	#print([run.killed_by if hasattr(run,"killed_by") else "None" for run in ironclad_runs])
	#the_silent_runs = loadTheSilentRuns()
	#defect_runs = loadDefectRuns()
	#watcher_runs = loadWatcherRuns()


	

if __name__ == "__main__": main()