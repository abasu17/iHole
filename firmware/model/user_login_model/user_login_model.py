from model.model import *

class UserLoginModel:
	
	def user_login(self, data):
		login_data = db.sys_users.find_one({ "user_name" : data['user_id'] , "password" : data['password']})
		return login_data
