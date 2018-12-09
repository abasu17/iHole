from model.model import *

class SysConfigurationModel:
	
	def change_userPassword(self, data):
		return db.sys_users.update_one({"user_name" :data['user_name']}, {"$set" : {"password" : data["password"]}})
	
	def change_adminPassword(self, data):
		return db.sys_admin.update_one({"username" :"admin"}, {"$set" : {"password" : data}})
