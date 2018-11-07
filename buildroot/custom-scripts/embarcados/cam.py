from flask import Flask, flash, redirect, render_template, request, session, abort
from threading import Thread
import time
import os

is_running = False

def cam(delay,shots,local):
    # initialize the camera
    # cam = VideoCapture(0)   # 0 -> index of camera

    try:
        file = open(local+"index","r+")    
        index = int(file.readline())
        file.close()
    except:
        index = 0

    for x in range(0,shots):
        index= index+1
        os.system('fswebcam -r 640x480 -S 1 --jpeg 50 --save '+local+'/img'+str(index)+'.jpg')
        os.system('cp '+local+'img'+str(index)+'.jpg ./static/images/capture.jpg')

#        s, img = cam.read()
#        
#        if s:    # frame captured without any errors
#            imwrite("static/images/capture.jpg",img) #save image
#            index= index+1
#            imwrite(local+"img"+str(index)+".jpg",img) #save image
        time.sleep(delay) 
        

    file = open(local+"index","w+")    
    file.write(str(index))
    file.close()
    
    global is_running
    is_running = False

cam(0.3,10,'./images/')
