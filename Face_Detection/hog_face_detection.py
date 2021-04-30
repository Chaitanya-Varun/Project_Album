#importing the necessary modules
from pyimagesearch.helpers import convert_and_trim_bb
import argparse
import imutils
import time 
import dlib
import cv2

#Argument parser 
ap = argparse.ArgumentParser()
ap.add_argument('-i',"--image",type=str,required=True,help="Path of the input image")
#The path to the input image where we apply HOG + Linear SVM face detection.
ap.add_argument('-u',"--upsample",type=int,default=1,help="#Number of times to upsample")
#Number of times to upsample an image before applying face detection.
args = vars(ap.parse_args())

#Loading the dlibs modules of HOG+SVM face detector
print("[INFO] loading the HOG + Linear SVM Face detector...")
detector = dlib.get_frontal_face_detector()

#Load the input image
image = cv2.imread(args["image"])
image = imutils.resize(image, width=600)
#Convert the image from BGR to RGB channel ordering (dlib expects RGB images)
rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


# perform face detection using dlib's face detector
start = time.time()
print("[INFO[ performing face detection with dlib HOG model...")
rects = detector(rgb, args["upsample"])
end = time.time()
print("[INFO] face detection took {:.4f} seconds".format(end - start))

# convert the resulting dlib rectangle objects to bounding boxes,
# then ensure the bounding boxes are all within the bounds of the
# input image
boxes = [convert_and_trim_bb(image, r) for r in rects]

# loop over the bounding boxes
for (x, y, w, h) in boxes:
	# draw the bounding box on our image
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)