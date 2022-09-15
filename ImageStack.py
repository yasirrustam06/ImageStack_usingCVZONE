import cv2
import cvzone
from cvzone.PoseModule import PoseDetector
pose_detector = PoseDetector(detectionCon=0.8,trackCon=0.5)
cap =cv2.VideoCapture("5.mp4")

while True:
    ret,img =cap.read()

    Image = pose_detector.findPose(img)
    ImgList = [Image,Image,Image,Image,Image,Image,Image,Image,Image,Image,Image,Image,Image,Image,Image]
    ImageStack = cvzone.stackImages(ImgList,cols=3 , scale=0.4)

    cv2.imshow("Image",ImageStack)
    cv2.waitKey(1)