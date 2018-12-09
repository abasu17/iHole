import sys, os
sys.path.append(os.path.abspath(os.path.join('..', ''))) 

from app import *
from flask_pymongo import PyMongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.automateLock_db

def f():
	print("Hello")
	
mongo = PyMongo(app)

from model.admin_login_model.admin_login_model import *
from model.sys_configuration_model.sys_configuration_model import *
from model.sys_history_model.sys_history_model import *
#from model.sys_networking_model.sys_networking_model import *
#from model.sys_onlineDevices_model.sys_onlineDevices_model import *
from model.user_dashboard_model.user_dashboard_model import *
from model.user_details_model.user_details_model import *
from model.user_login_model.user_login_model import *
from model.user_registration_model.user_registration_model import *

