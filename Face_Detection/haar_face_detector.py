#Importing all the necessary packages
import argparse#for arguement parsing
import imutils#for opencv functions
import cv2#for opencv bindings

#Constructing argument parser to parse the arguements
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",type=str,required=True,
	help = "Give the path to input image")
ap.add_argument("-c","--cascade",type = str,
	default = 'haarcascade_frontalface_default.xml',
	help = "Give path to the haar cascade face detector")
args = vars(ap.parse_args())#This contains our required arguements in form of dict()

#Loading the Haar classifier from the disk
print("[INFO] loading the face detector...")
detector = cv2.CascadeClassifier(args["cascade"])#Loads he classifier

#Now load the input image from the disk, do the resizing, convert it to grey scale
image = cv2.imread(args["image"])#loads the imag
image = imutils.resize(image,width=500)#Resize the image
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#grey scaling

#Detection and annotation
print("[INFO] performing the face detection...")
rects = detector.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5,minSize=(10,10),
	flags = cv2.CASCADE_SCALE_IMAGE)
print("[INFO] {} faces detected....".format(len(rects)))
#Refer : scaleFactor,minNeighbors,minSize
#Looping oer the bounded boxes
for (x,y,w,h) in rects:
	# draw the the bounding box on the image
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

#Show the output image 
cv2.imshow("Image",image)
if cv2.waitKey(0) != 0:#any key
        exit()