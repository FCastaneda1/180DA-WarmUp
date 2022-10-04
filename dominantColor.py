# Example code from code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def find_dominant_color():
	cap = cv2.VideoCapture(0)

	while(True):
		# Capture frame-by-frame
		ret, frame = cap.read()

		# Perform operations
		frame_reshaped = frame.reshape((frame.shape[0] * frame.shape[1], 3))
		clt = KMeans(n_clusters=3)
		clt.fit(frame_reshaped)
		hist = find_histogram(clt)
		bar = plot_colors2(hist, clt.cluster_centers_)

		# Display the resulting frame
		cv2.imshow('frame', frame)
		cv2.imshow('bar', bar)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# Release everything when done
	cap.release()
	cv2.destroyAllWindows()

def find_histogram(clt):
	"""
	create a histogram with k clusters
	:param: clt
	:return: hist
	"""
	numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
	(hist, _) = np.histogram(clt.labels_, bins=numLabels)

	hist = hist.astype("float")
	hist /= hist.sum()

	return hist

def plot_colors2(hist, centroids):
	bar = np.zeros((50,300,3), dtype="uint8")
	startX = 0

	for (percent, color) in zip(hist, centroids):
		# plot the relative percentage of each cluster
		endX = startX + (percent * 300)
		cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
			      color.astype("uint8").tolist(), -1)
		startX = endX

	# return the bar chart
	return bar

if __name__ == '__main__':
	find_dominant_color()
