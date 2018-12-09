from model.model import *

class UserDetailsModel:
	
	def get_userDetails(self):
		return db.sys_users.find()
