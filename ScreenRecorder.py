import cv2
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
SCREEN_SIZE = (1920, 1080)
fourcc= cv2.VideoWriter_fourcc(*"XVID")
cv2.VideoWriter
out = cv2.VideoWriter_fourcc("output.avi",fourcc,20.0,(SCREEN_SIZE))
while True:
 img=pyautogui.screenshot()
 frame=np.array(img)
 farme=cv2.cvtColor(frame,cv2.COLOR_BGR2RBG)
 out.write(frame)
 cv2.imshow("screenshot",frame)
 if cv2.waitKey(1) == ord("q"):
  break
  cv2.destroyALLWindows()
  out.release()