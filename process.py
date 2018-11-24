import serial
import cv2
import face_recognition
import sys
import os

'''define function to compare two images..
 	input_image is captured by camera.
 	database_image is stored into database.
 	@author : Aniket Basu <aniketbasu7@gmail.com>
	@packages : faceRecognition'''
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
    cap = cv2.VideoCapture(0)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # check if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break                                   # quit
        elif cv2.waitKey(1) & 0xFF == ord('c'):     # if 'c' is pressed
            cv2.imwrite('temp_img.jpg', frame)      # capture image

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
''' End of captureFace function'''


''' define function to capture images.
 	input_image is captured by camera.
 	@author : Aniket Basu <aniketbasu7@gmail.com>
	@packages : captureFace '''	
def checkFace(img):
    for root, dirs, files in os.walk('./data'):
        for _file in files:
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
    return True
