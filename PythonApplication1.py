import cv2
img=cv2.imread(r"D:\imags\wz.jpg")
zhen1=cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))
cv2.imwrite(r"D:\imags\zhen1.JPG",zhen1)
img1=cv2.imread(r"D:\imags\zhen1.JPG")
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
face_casade=cv2.CascadeClassifier(r"D:\imags\haarcascade_frontalface_default.xml")
face=face_casade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=30)
for x,y,w,h in face:
	img1=cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),5)
cv2.imshow("demo",img1)
cv2.waitKey(0)
 