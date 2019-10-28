import cv2
import numpy as np
import math

image = cv2.imread("./orange.jpg", 0)
image=image.astype(np.int32)
ori_row = image.shape[0]
ori_col = image.shape[1]
new_row = int(image.shape[0] * math.sqrt(2))
new_col = int(image.shape[1] * math.sqrt(2))
result = np.zeros((new_row, new_col),dtype=np.uint8)

for x in range(new_row):
	for y in range(new_col):
		m = ori_row * x / new_row
		n = ori_col * y / new_col
		i = int(m)
		j = int(n)
		if i < ori_row - 1 and j < ori_col - 1:
			# print(m,n,i,j)
			pin = image[i][j] + (image[i][j + 1] - image[i][j]) * (n - j)
			pmj = image[i][j] + (image[i + 1][j] - image[i][j]) * (m - i)
			pi1n = image[i + 1][j] + (image[i + 1][j + 1] - image[i + 1][j]) * (n - j)
			pmj1 = image[i][j + 1] + (image[i + 1][j + 1] - image[i][j + 1]) * (m - i)
			# pmn=pin+(pi1n-pin)*(m-i)+pmj+(pmj1-pmj)*(n-j)
			pmn = pmj + (pmj1 - pmj) * (n - j)
		else:
			pmn = 0

		result[x][y] = pmn

print(image.shape)
result=result.astype(np.uint8)
cv2.imshow("result", result)
cv2.waitKey(0)
