import cv2
import histogram
import numpy as np

image=cv2.imread("./orange.jpg",0)
cv2.imshow("ori",image)
# cv2.waitKey(0)

hist=histogram.calHistogram(image)
histogram.drawHistoGram(hist)

# calculate the lookup table (LUT)
lut=hist.cumsum()
lut_masked=np.ma.masked_equal(lut,0)
lut=(lut_masked-lut_masked.min())*255/(lut_masked.max()-lut_masked.min())
lut=np.ma.filled(lut,0).astype("uint8")

result=lut[image]
hist_bala=histogram.calHistogram(result)
histogram.drawHistoGram(hist_bala)

cv2.imshow("balanced",result)
cv2.waitKey(0)
