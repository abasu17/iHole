from flask import render_template, request, session, Response
import socket, pyspeedtest, time
from werkzeug.utils import secure_filename
from plugins import *

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', ''))) 

from model.model import *

from controller.admin_login.admin_login import *
from controller.sys_configuration.sys_configuration import *
from controller.sys_history.sys_history import *
from controller.sys_networking.sys_networking import *
from controller.sys_onlineDevices.sys_onlineDevices import *
from controller.user_dashboard.user_dashboard import *
from controller.user_details.user_details import *
from controller.user_login.user_login import *
from controller.user_registration.user_registration import *

