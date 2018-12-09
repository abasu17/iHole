from controller.controller import *

class UserDashboard:
	
	model_obj = UserDashboardModel()
	
	def storeUnlockData(self):
		
		lock_data = {}
		
		currentTime = time.asctime( time.localtime(time.time()) )
		currentTime = currentTime.split(" ")
		
		lock_data["user_name"]  = session['user_name']
		lock_data["unlockDate"]  = currentTime[3] + "-" + currentTime[1] + ", " + currentTime[-1] + " (" + currentTime[0] + ")"
		lock_data["unlockTime"]  = currentTime[-2]
		
		if (model_obj.storeUnlockData(lock_data)):
			return True
		return False
