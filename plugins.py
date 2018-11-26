import string
import random
from flask import session, redirect

def uuid(size = 32, chars = string.ascii_uppercase + string.digits ):
	return ''.join(random.choice(chars) for _ in range(size))

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


''' define function to capture images.
 	input_image is captured by camera.
    @author : Aniket Basu <aniketbasu7@gmail.com>
	@packages : unlockLock '''	
def unlockLock():
    #Start the serial port to communicate with arduino
    data = serial.Serial('/dev/ttyACM1', 9600, timeout = 1)
    data.write(b'1')   # open lock
    return True
