import cv2
import matplotlib.pyplot as plt


img = cv2.imread('test.jpg')
print(img.shape)
x_min,x_max = 50,550
y_min,y_max = 250, 640
# cv2.rectangle(img, pt1=(50,250), pt2=(550,640), color=(0,255,0), thickness=5)
temp = img[y_min:y_max, x_min:x_max].copy()
# cv2.rectangle(img, pt1=(x_min,y_min), pt2=(x_max,y_max), color=(0,255,0), thickness=10)
plt.imshow(img)
plt.show()
