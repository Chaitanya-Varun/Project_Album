# Project_Album
Classification of images based on the faces and clustering them together.

The main idea for the project is to help in obtaining the photos of an individual wherever he is in the picture. These come in handy when we obtain a huge set of photos from trips or photowalks.

The implementation of this idea is done in steps :
- Face Detection : I used different approaches for detection of faces which include Haar Classifier, OpenCV's DNN, dlib tools - HOG and CNN classfiers.
The performance was one better than the previous. For implementation, walkthrough the code.
- Face Recognition : I used the google collab for this part for using the GPU. The motive in this step is given some data of the individual, it has to segregate his pictures into a new folder. We use the Face_Recognition library for encoding and recorgnition. And in the code used, we have implemented face detection using the dlibs- CNN method for better accuracy. 
- Face Clustering : ---
