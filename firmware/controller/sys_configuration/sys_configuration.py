from controller.controller import *


class SysConfiguration:	
	
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
	
	def changeAdminPassword(self):
		model_obj = SysConfigurationModel()
		password = request.form.get('inputPassword')
		if (model_obj.change_adminPassword(password)):
			return True
		return False

	def changeUserPassword(self):
		data = {}
		model_obj = SysConfigurationModel()
		password = request.form.get('inputPassword')
		data["user_name"] = session["user_name"]
		data["password"] = password
		if (model_obj.change_userPassword(data)):
			return True
		return False
