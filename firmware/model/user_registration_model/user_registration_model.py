from model.model import *

class UserRegistrationModel:
	
	def user_signup(self, data):
		type_check = db.sys_users.insert_one(data)
		return (str(type(type_check)) ==  "<class 'pymongo.results.InsertOneResult'>" )
