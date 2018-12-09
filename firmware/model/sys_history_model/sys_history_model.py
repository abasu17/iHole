from model.model import *

class SysHistoryModel:
	
	def get_unlockHistory(self):
		return db.sys_lock_data.find()
