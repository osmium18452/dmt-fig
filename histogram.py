import matplotlib.pyplot as pyplot
import numpy as np

def calHistogram(img):
	if len(img.shape) != 2:
		print("wrong image size")
		return None
	histogram=np.zeros(256)
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			histogram[img[i][j]] += 1
	return histogram


def drawHistoGram(histogram):
	pyplot.figure()
	pyplot.axis([0, 256, 0, max(histogram)])
	pyplot.grid(True)
	x=np.arange(0,256,1)
	pyplot.bar(x,histogram)
	pyplot.show()
