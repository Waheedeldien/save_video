import cv2

import os
import time

import time
timestr = time.strftime("%Y%m%d-%H%M%S")
print(cv2.__version__)
print(cv2.getBuildInformation())
#vidcap = cv2.VideoCapture(0)

vidcap = cv2.VideoCapture('/dev/video0',cv2.CAP_V4L2 )
vidcap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
vidcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
vidcap.set(cv2.CAP_PROP_FPS, 60)
fps = vidcap.get(cv2.CAP_PROP_FPS)


print("fps: ", fps)
success,image = vidcap.read()
cv2.imwrite("test1.png", image)
count = 0
fr = []

# fourcc = cv2.VideoWriter_fourcc(*'MP4V')
# out = cv2.VideoWriter('output.mp4', fourcc, 40.0, (1280,720))
video_file = timestr + '.mp4'
out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'MP4V'), fps, (1920,1080))
while success:
    success,img = vidcap.read()
    out.write(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
out.release()