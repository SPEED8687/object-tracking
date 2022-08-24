import cv2
import math
goalX=530
goalY=300
video=cv2.VideoCapture('bb3.mp4')
trakcer=cv2.TrackerCSRT_create()
ret,image=video.read()
bbox=cv2.selectROI("trapping",image,False)
trakcer.init(image,bbox)
def drawbox(image,bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3,1)
def goalTracking(image,bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    c1=x+int(w/2)
    c2=y+int(h/2)
    cv2.circle(image,(c1,c2),2,(255,0,0),5)
    cv2.circle(image,(goalX,goalY),2,(255,0,0),5)
    dist = math.sqrt(((c1-goalX)**2) + (c2-goalY)**2)
    if(dist<40):
        cv2.putText(image,"Goal Achieved",(350,90),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)
while True:
    ret,image=video.read()
    success,bbox=trakcer.update(image)
    if(success==True):
        drawbox(image,bbox)
    goalTracking(image,bbox)
    cv2.imshow("result", image) # Quit Display Window when Spacebar key is pressed 
    key = cv2.waitKey(25) 
    if key == 32: 
        print("Stopped") 
        break