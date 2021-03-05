import os
try:
    import urllib.request
except:
    os.system('pip install urllib.request')
    import urllib.request
try:
    import io
except:
    os.system('pip install io')
    import io
try:
    import cv2
except:
    os.system('pip install cv2')
    import cv2
try:
    import numpy as np
except:
    os.system('pip install numpy')
    import numpy as np
try:
    import getpass
except:
    os.system('pip install getpass')
    import getpass


class DetectMyFace:
    def __init__(self):   
        self.clientname = str(getpass.getuser())
        self.face_cascade_read = ('https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml')
        urllib.request.urlretrieve(self.face_cascade_read, 'C:\\Users\\{}\\Desktop\\face_cascade.xml'.format(self.clientname))

        self.face_cascade_img = cv2.CascadeClassifier('C:\\Users\\{}\\Desktop\\face_cascade.xml'.format(self.clientname))

        self.eye_cascade_read = ('https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_eye.xml')
        urllib.request.urlretrieve(self.eye_cascade_read, 'C:\\Users\\{}\\Desktop\\eyes_cascade.xml'.format(self.clientname))

        self.eye_cascade_img = cv2.CascadeClassifier('C:\\Users\\{}\\Desktop\\eyes_cascade.xml'.format(self.clientname))
        

    def DoWork(self):
        try:
            cap = cv2.VideoCapture(0)
        except:
            cap = cv2.VideoCapture(1)

        while True:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face = self.face_cascade_img.detectMultiScale(gray, 1.3, 5)
            
            for (x, y, w, h) in face:
                cv2.rectangle(img, (x,y), (x+w, y+h), (179, 255, 255), 2)   ## axes, color, thickness
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                smile = self.eye_cascade_img.detectMultiScale(roi_gray)
                for (sx, sy, sw, sh) in smile:
                    cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (168, 50, 50), 2)  ## axes, color, thickness

            cv2.imshow('img', img)
            k = cv2.waitKey(30) & 0xff    ## Escape key
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
if __name__=="__main__":
    DetectMyFace().DoWork()