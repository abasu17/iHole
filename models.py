from app import *
from controllers import *
from flask_pymongo import PyMongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.automateLock_db

mongo = PyMongo(app)

class data_store:
	
	def user_signup(self, data):
		print(data)
		type_check = db.sys_users.insert_one(data)
		return (str(type(type_check)) ==  "<class 'pymongo.results.InsertOneResult'>" )

	
	def admin_login(self, data):
		login_data = db.sys_admin.find_one({ "username" : data['user_id'] , "password" : data['password']})
		return login_data


	def get_userDetails(self):
		return db.sys_users.find()

	def change_userPassword(self, data):
		return db.sys_admin.update_one({"username" :"admin"}, {"$set" : {"password" : data}})
