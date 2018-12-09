from controller.controller import *


class UserDetails:
	model_obj = UserDetailsModel()
	
	def getUserDetails(self):
		user_details = []
		for user in model_obj.get_userDetails():
			user_details.append(user)
		return user_details
