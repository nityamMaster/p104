import cv2
image=cv2.imread("solar-system.jpg")
cv2.putText(image,"mercuery",(100,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image,"venus",(200,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image,"earth",(300,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image,"mars",(400,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.imshow("display",image)
cv2.waitKey(2000)
cv2.imwrite("greeting.jpg",image)
