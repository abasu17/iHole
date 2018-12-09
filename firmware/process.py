import serial
import cv2
import face_recognition
import sys
import os


cwd = os.getcwd()

''' define function to compare two images.
 	input_image is captured by camera.
 	database_image is stored into database.
 	@author : Aniket Basu <aniketbasu7@gmail.com>
	@packages : faceRecognition '''
def faceRecognition( input_image, database_image ):

	''' take two image and load them into two different variables '''
	# known_image is input_image
	known_image = face_recognition.load_image_file(input_image)
	# unknown_image is database_image
	unknown_image = face_recognition.load_image_file(database_image)

	''' encode the loaded images and stored them. '''
	# known_encoding stores data regarding known_image
	known_encoding = face_recognition.face_encodings(known_image)[0]
	# known_encoding stores data regarding unknown_encoding
	unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

	''' compare results of two encoded variables. '''
	# result stores True or False.
	results = face_recognition.compare_faces([known_encoding], unknown_encoding)

	# return result
	return results
''' End of faceRecognition function'''


''' define function to capture images.
 	input_image is captured by camera.
 	@author : Aniket Basu <aniketbasu7@gmail.com>
	@packages : captureFace '''	
def captureFace():
	face_cascade = cv2.CascadeClassifier(cwd + '/object_files/haarcascade_frontalface_default.xml')
	cap = cv2.VideoCapture(0)
	while(True):
		# Capture frame-by-frame
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		# Display the resulting frame
		cv2.imshow('frame', frame)
        
		# check if 'q' is pressed
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break                                   # quit
		elif str(type(faces)) != "<class 'tuple'>":     # if 'c' is pressed
			cv2.imwrite(cwd + '/temp/temp_img.jpg', frame)      # capture image
			break
	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()
''' End of captureFace function'''


''' define function to capture images.
 	input_image is captured by camera.
 	@author : Aniket Basu <aniketbasu7@gmail.com>
	@packages : captureFace '''	
def checkFace(img):
	for root, dirs, files in os.walk(cwd+'/uploads'):
		for _file in files:
			if _file.endswith(".jpg") or _file.endswith(".jpeg"):
				print(root +"/"+_file)
				res = faceRecognition(img, str(root +"/"+_file))
				if (res):
					return res
        
''' define function to capture images.
	input_image is captured by camera.
	@author : Aniket Basu <aniketbasu7@gmail.com>
	@packages : unlockLock '''	
def unlockLock():
	#Start the serial port to communicate with arduino
	data = serial.Serial('/dev/ttyACM1', 9600, timeout = 1)
	data.write(b'1')   # open lock
    

captureFace()
if(checkFace(cwd + '/temp/temp_img.jpg')):
	unlockLock()
	captureFace()
