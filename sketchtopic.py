# install opencv-python and import 
import cv2
 # load your image from specific path 
image1 = cv2.imread('C:\\Users\\lenovo\\Desktop\\HARRY PROJECT\\Pencil Sketch using\\lala.jpg')

# Convert image color( to gray)

gray_img =cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gray_img)

#img smooth ness
blur = cv2.GaussianBlur(invert,(21,21),0)

invertblur = cv2.bitwise_not(blur)
sketch = cv2.divide(gray_img,invertblur , scale=256.0)

# save image to your storage( give spevific path )

cv2.imwrite("C:\\Users\\lenovo\\Desktop\\HARRY PROJECT\\Pencil Sketch using\\converteb2.png", sketch)

# success
