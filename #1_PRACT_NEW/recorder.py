import cv2
import numpy as np
import pyautogui
import time

screen = (1920,1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi",fourcc,20.0,(screen))
fps = 120
pre = 0
while True:
    time_elapsed = time.time()-pre
    img = pyautogui.screenshot()
    if time_elapsed > (1.0/fps):
        pre = time.time()
        frame = np.array(img)
        frame = cv2.cvtcolor(frame,cv2.COLOR_BGR2RGB)
        out.write(frame)
    cv2.waitkey(100)
cv2.destroyAllWindows()
cv2.release()
    
