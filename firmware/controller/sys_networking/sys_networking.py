from controller.controller import *


class SysNetworking:	
	
	def getPing(self, webPing):
		st = pyspeedtest.SpeedTest(webPing)
		return st.ping()
