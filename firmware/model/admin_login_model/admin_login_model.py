from model.model import *

class AdminLoginModel:
	
	def admin_login(self, data):
		login_data = db.sys_admin.find_one({ "username" : data['user_id'] , "password" : data['password']})
		return login_data
