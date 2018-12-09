from controller.controller import *


class AdminLogin:	
	
	def adminLogin(self):
		model_obj = AdminLoginModel()
		login_data = {}
		login_data["user_id"] = request.form.get('inputUserID')
		login_data["password"] = request.form.get('inputPassword')
		if (str(model_obj.admin_login(login_data)) == "None" ):
			return False
		session['user_name']  = request.form.get('inputUserID')
		return True
