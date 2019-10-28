import cv2
import math
import numpy as np

image = cv2.imread("./orange.jpg", 0)
rows = image.shape[0]
cols = image.shape[1]

beta = -45/180*math.pi
center = [rows//2, cols//2]
transform = np.array([[math.cos(beta), -math.sin(beta), 0],
					  [math.sin(beta), math.cos(beta), 0],
					  [0, 0, 1]])


result = np.zeros((rows, cols), dtype=np.uint8)
for i in range(rows):
	for j in range(cols):
		src_pos = np.array([i - center[0], j - center[1], 1])
		[x, y, z] = np.dot(transform, src_pos)
		x = int(x) + center[0]
		y = int(y) + center[1]

		if x >= rows or y >= cols or x < 0 or y < 0:
			result[i][j] = 255
		else:
			result[i][j] = image[x][y]

cv2.imshow("rotate", result)
cv2.waitKey(0)
