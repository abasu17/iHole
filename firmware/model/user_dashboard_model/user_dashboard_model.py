from model.model import *

class UserDashboardModel:

	def storeUnlockData(self, data):
		type_check = db.sys_lock_data.insert_one(data)
		return (str(type(type_check)) ==  "<class 'pymongo.results.InsertOneResult'>" )
