import cv2
import numpy as np

#Image size
WIDTH = 1000
HEIGHT = 700

#green background
track = np.full((HEIGHT, WIDTH, 3), (0, 180, 0), dtype=np.uint8)

#outer road
cv2.rectangle(track, (100, 100), (900, 600), (100, 100, 100), -1)

#inner grass
cv2.rectangle(track, (250, 250), (750, 450), (0, 180, 0), -1)

#white lane boundaries
cv2.rectangle(track, (100, 100), (900, 600), (255, 255, 255), 4)
cv2.rectangle(track, (250, 250), (750, 450), (255, 255, 255), 4)

#start/finish line
for y in range(100, 180, 20):
    cv2.rectangle(track, (120, y), (140, y + 10), (255, 255, 255), -1)

cv2.imwrite("track.png", track)

print("Track saved as track.png")