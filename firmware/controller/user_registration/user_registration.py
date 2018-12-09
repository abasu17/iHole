from controller.controller import *


class UserRegistration:
	
	def getRegistrationData(self):
		model_obj = UserRegistrationModel()
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
			model_obj.user_signup(user_data)
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
		session.pop('uname')
		session.pop('password')
		return True
