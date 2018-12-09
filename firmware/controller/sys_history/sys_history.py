from controller.controller import *


class SysHistory:
	
	def getLockDetails(self):
		model_obj = SysHistoryModel()
		lock_details = []
		for det in model_obj.get_unlockHistory():
			lock_details.append(det)
		return lock_details
