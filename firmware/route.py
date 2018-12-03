from app import app
from flask import render_template, request, session, send_from_directory, redirect
from controllers import *
import os
from camera import VideoCamera
from plugins import *

user = users()
conf = configuration()
netw = networking()
proc = processing()
act_dev = activeDevices()

@app.route('/', methods=['GET', 'POST'])
def index():
	flag = 0
	session['auth'] = False
	if request.method == 'POST':
		flag = 1
		if (user.userLogin()):
			session['auth'] = True
			return redirect('/dashboard')
	return render_template('user_login/user_login.html', f = flag)

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
	flag = 0
	session['auth'] = False
	if request.method == 'POST':
		flag = 1
		if (user.admLogin()):
			session['auth'] = True
			return redirect('/dashboard')
	return render_template('admin_login/admin_login.html', f = flag)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
	lock_status = 0
	if (not session['auth']):
		return redirect('/')
		
	if request.method == 'POST':
		print("POST")
		if(unlockLock()):
			if(proc.getLockData()):
				lock_status = 1
	return render_template('user_dashboard/user_dashboard.html', lock_stat = lock_status )


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if (not session['auth']):
		return redirect('/')

	if request.method == 'POST':
		u_reg = user.getRegistrationData()
		if ( request.form.get('page_index') == '2' ):
			if (user.uploadImage()):
				return render_template('user_registration/user_information.html', user = session)
		elif (  u_reg != {}): 
			session['f_name'] = u_reg['f_name']
			session['uname'] = u_reg['user_name']
			session['password'] = u_reg['password']
			return render_template('user_registration/user_image_upload.html' , user = u_reg['f_name'])
	return render_template('user_registration/user_signup.html')


@app.route('/completed', methods=['POST', 'GET'])
def regCompleted():
	if (not session['auth']):
		return redirect('/')
	if (user.registrationSuccessful()):
		return render_template('user_dashboard/user_dashboard.html')
	
	return redirect('/')

@app.route('/details')
def userDetails():
	if (not session['auth']):
		return redirect('/')
	user_data = user.getUserDetails()
	return render_template('user_details/user_details.html', users = user_data)

@app.route('/video_feed')
def video_feed():
	if (not session['auth']):
		return redirect('/')
	return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/changeConfiguration', methods=['POST', 'GET'])
def changeConfiguration():
	if (not session['auth']):
		return redirect('/')
	
	flag = 0
	if request.method == 'POST':
		ip_address = request.form.get('ip_addr')
		conf.ipAddrChange(ip_address)
		flag = 1
	return render_template('sys_configuration/sys_changeConfiguration.html', ip_addr = conf.getCurrentIP(), net_List = conf.getNetworkInterfaces(), f = flag)

@app.route('/changePassword', methods=['POST', 'GET'])
def changePassword():
	if (not session['auth']):
		return redirect('/')
	flag = 0
	if request.method == 'POST':
		if (conf.changeUserPassword()):
			flag = 1
	return render_template('sys_configuration/sys_changePassword.html', f = flag)

@app.route('/networking', methods=['POST', 'GET'])
def networking():
	if (not session['auth']):
		return redirect('/')
	return render_template('sys_networking/sys_networking.html')

@app.route('/pingData')
def pingData():
	if (not session['auth']):
		return redirect('/')
	return str(netw.getPing("www.google.com"))

@app.route('/logout')
def logout():
	session.pop('auth')
	return redirect('/')
	
@app.route('/history')
def history():
	if (not session['auth']):
		return redirect('/')
	hist_data = proc.getLockDetails()
	return render_template('sys_history/sys_history.html', data = hist_data)

@app.route('/onlineDevices')
def onlineDevices():
	if (not session['auth']):
		return redirect('/')
	online_dat = act_dev.getPingFromDev()
	return render_template('sys_onlineDevices/sys_onlineDevices.html', data = online_dat)
