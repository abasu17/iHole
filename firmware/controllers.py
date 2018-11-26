from flask import render_template, request, session, Response
from models import *
import os, socket
from werkzeug.utils import secure_filename
from plugins import *
import pyspeedtest
import time

dat = data_store()
proc_m = processing_model()

class users:
	
	def admLogin(self):
		login_data = {}
		login_data["user_id"] = request.form.get('inputUserID')
		login_data["password"] = request.form.get('inputPassword')
		if (str(dat.admin_login(login_data)) == "None" ):
			return False
		session['user_name']  = request.form.get('inputUserID')
		return True

	def getRegistrationData(self):
		user_data = {}
		session['new_file'] = uuid()
		if request.form.get('inputPassword') == request.form.get('inputConfPassword') and (request.form.get('inputFname') != None):
			user_data["f_name"]  = request.form.get('inputFname')
			user_data["l_name"] = request.form.get('inputLname')
			user_data["gender"] = request.form.get('inputGender')
			user_data["dob"] = request.form.get('inputDOB')
			user_data["mobile"] = request.form.get('inputMobile')
			user_data["password"] = request.form.get('inputPassword')
			user_data["user_name"] = (request.form.get('inputFname')).lower() + "." + (request.form.get('inputLname')).lower()
			user_data["file_name"] = session['new_file']
			dat.user_signup(user_data)
		return user_data
	
	def uploadImage(self):
		photo = request.files['inputImage']
		if photo:
			filename = secure_filename(photo.filename)
			photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			os.rename(os.path.join(app.config['UPLOAD_FOLDER'], filename), os.path.join(app.config['UPLOAD_FOLDER'], session['new_file']))
			os.system('cp ' +  os.path.join(app.config['UPLOAD_FOLDER'], session['new_file']) + ' '  + os.path.join(app.config['STATIC_F'], session['new_file']))
			return True
	
	def registrationSuccessful(self):
		os.system('rm ' +  os.path.join(app.config['STATIC_F'], session['new_file']))
		session.pop('new_file')
		session.pop('f_name')
		session.pop('user_name')
		session.pop('password')
		return True
	
	def getUserDetails(self):
		user_details = []
		for user in dat.get_userDetails():
			user_details.append(user)
		return user_details

		
class configuration:

	def ipAddrChange(self, new_ip_addr):
		os.system("ifconfig wlp6s0 down")
		os.system("ifconfig wlp6s0 " + new_ip_addr)
		os.system("ifconfig wlp6s0 up")
		return True
	
	def getCurrentIP(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		ip = s.getsockname()[0]
		s.close()
		return ip
	
	def getNetworkInterfaces(self):
		return os.popen("ifconfig -a | sed 's/[ \t].*//;/^\(lo\|\)$/d'").read().split("\n")[:-1]
	
	def changeUserPassword(self):
		password = request.form.get('inputPassword')
		if (dat.change_userPassword(password)):
			return True
		return False

class networking:
	
	def getPing(self, webPing):
		st = pyspeedtest.SpeedTest(webPing)
		return st.ping()

class processing:
	
	def getLockData(self):
		lock_data = {}
		currentTime = time.asctime( time.localtime(time.time()) )
		currentTime = currentTime.split(" ")
		lock_data["user_name"]  = session['user_name']
		lock_data["unlockDate"]  = localtime[2] + "-" + localtime[1] + ", " + localtime[-1] + " (" + localtime[0] + ")"
		lock_data["unlockTime"]  = localtime[3]
		if (proc_m.storeLockData(lock_data)):
			return True
		return False

	
	def getLockDetails(self):
		lock_details = []
		for det in proc_m.get_lockDetails():
			lock_details.append(det)
		return lock_details

class activeDevices:
	def getPingFromDev(self):
		ip_dect = []
		base_ip = "192.168.1."
		for i in range(2, 21):
			if(os.popen("ping -c 1 -i 0.2 " + base_ip + str(i)).read().find("Destination Host Unreachable") < 0):
				ip_dect.append([base_ip + str(i)])
		return ip_dect
