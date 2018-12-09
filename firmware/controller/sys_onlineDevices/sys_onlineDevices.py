from controller.controller import *


class SysOnlineDevices:	
	
	def getPingFromDev(self):
		ip_dect = []
		base_ip = "192.168.1."
		for i in range(2, 10):
			if(os.popen("ping -c 1 -i 0.2 " + base_ip + str(i)).read().find("Destination Host Unreachable") < 0):
				ip_dect.append([base_ip + str(i)])
		return ip_dect
