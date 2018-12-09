from app import app
from datetime import timedelta
from flask import render_template, request, session, send_from_directory, redirect
from controller.controller import *
import os
from camera import VideoCamera
from plugins import *

@app.before_request
def make_session_permanent():
	session.permanent = True
	app.permanent_session_lifetime = timedelta(days=365)    

@app.route('/', methods=['GET', 'POST'])
def user_login():
	userLogin_controller = UserLogin()
	flag = 0
	session['auth'] = False
	if request.method == 'POST':
		flag = 1
		if (userLogin_controller.userLogin()):
			session['auth'] = True
			return redirect('/dashboard')
	return render_template('user_login/user_login.html', f = flag)
	
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
	adminLogin_controller = AdminLogin()
	flag = 0
	session['auth'] = False
	if request.method == 'POST':
		flag = 1
		if (adminLogin_controller.adminLogin()):
			session['auth'] = True
			return redirect('/dashboard')
	return render_template('admin_login/admin_login.html', f = flag)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
	dashboard_controller = UserDashboard()
	lock_status = 0
	session['auth'] = False
	if (not session['auth']):
		return redirect('/')
	if request.method == 'POST':
		if(unlockLock()):
			if(dashboard_controller.storeUnlockData()):
				lock_status = 1
	return render_template('user_dashboard/user_dashboard.html', lock_stat = lock_status )

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	userRegistration_controller = UserRegistration()
	if (not session['auth']):
		return redirect('/')
	if request.method == 'POST':
		u_reg = userRegistration_controller.getRegistrationData()
		if ( request.form.get('page_index') == '2' ):
			if (userRegistration_controller.uploadImage()):
				return render_template('user_registration/user_information.html', user = session)
		elif (  u_reg != {}): 
			session['f_name'] = u_reg['f_name']
			session['uname'] = u_reg['user_name']
			session['password'] = u_reg['password']
			return render_template('user_registration/user_image_upload.html' , user = u_reg['f_name'])
	return render_template('user_registration/user_signup.html')


@app.route('/completed', methods=['POST', 'GET'])
def regCompleted():
	userRegistration_controller = UserRegistration()
	if (not session['auth']):
		return redirect('/')
	if (userRegistration_controller.registrationSuccessful()):
		return render_template('user_dashboard/user_dashboard.html')
	return redirect('/')

@app.route('/details')
def userDetails():
	userDetails_controller = UserDetails()
	if (not session['auth']):
		return redirect('/')
	user_data = userDetails_controller.getUserDetails()
	return render_template('user_details/user_details.html', users = user_data)

@app.route('/changeConfiguration', methods=['POST', 'GET'])
def changeConfiguration():
	sysConfiguration_controller = SysConfiguration()
	if (not session['auth']):
		return redirect('/')
	flag = 0
	if request.method == 'POST':
		ip_address = request.form.get('ip_addr')
		sysConfiguration_controller.ipAddrChange(ip_address)
		flag = 1
	return render_template('sys_configuration/sys_changeConfiguration.html', ip_addr = sysConfiguration_controller.getCurrentIP(), net_List = sysConfiguration_controller.getNetworkInterfaces(), f = flag)

@app.route('/changePassword', methods=['POST', 'GET'])
def changePassword():
	sysConfiguration_controller = SysConfiguration()
	if (not session['auth']):
		return redirect('/')
	flag = 0
	if request.method == 'POST':
		if (session['user_name'] == 'admin'):
			if (sysConfiguration_controller.changeAdminPassword()):
				flag = 1
		else :
			if (sysConfiguration_controller.changeUserPassword()):
				flag = 1
	return render_template('sys_configuration/sys_changePassword.html', f = flag)

''' Addons '''
@app.route('/video_feed')
def video_feed():
	if (not session['auth']):
		return redirect('/')
	return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/networking', methods=['POST', 'GET'])
def networking():
	if (not session['auth']):
		return redirect('/')
	return render_template('sys_networking/sys_networking.html')

@app.route('/pingData')
def pingData():
	sysNetworking_controller = SysNetworking()
	if (not session['auth']):
		return redirect('/')
	return str(sysNetworking_controller.getPing("www.google.com"))

@app.route('/logout')
def logout():
	session.pop('auth')
	return redirect('/')
	
@app.route('/history')
def history():
	sysHistory_controller = SysHistory()
	if (not session['auth']):
		return redirect('/')
	hist_data = sysHistory_controller.getLockDetails()
	return render_template('sys_history/sys_history.html', data = hist_data)

@app.route('/onlineDevices')
def onlineDevices():
	sysOnlineDevices_controller = SysOnlineDevices()
	if (not session['auth']):
		return redirect('/')
	online_dat = sysOnlineDevices_controller.getPingFromDev()
	return render_template('sys_onlineDevices/sys_onlineDevices.html', data = online_dat)
