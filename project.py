# command line resolution : 236x63
symbols = ['.', ':', '!', '/', 'r', '(', '1', 'H', 'W', '@']


# symbols = list(r'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,   ')
# symbols.reverse()

# symbols = list(r' .:-=+*#%@')

####################### Settings #######################

width = 100 # symbols
height = 50	# symbols
file_name = 'anime.gif'

####################### Settings #######################

import os

cmd = f'mode {width},{height}'
os.system(cmd)



import numpy as np
np.set_printoptions(threshold=np.inf, linewidth= width)
import cv2
import time

# img = cv2.imread('testimg.jpg', 0)
# img = cv2.resize(img, [width, height])
# # print(np.amin(img))
# new_matrix = np.array(np.eye(height,width), dtype=str)
# # print(*new_matrix)


vidcap = cv2.VideoCapture(file_name)
frames_list = []
success,image = vidcap.read()
image = cv2.resize(image, [width, height])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
frames_list.append(image)
count = 0
while success:   
	success,image = vidcap.read()
	if type(image) is np.ndarray:
		image = cv2.resize(image, [width, height])
		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		frames_list.append(image)
	count += 1


# print(len(frames_list))

new_matrix = []
new_matrix = np.array(np.eye(height,width), dtype=str)


time.sleep(2)
while 1:
	# frames_list = frames_list[:20]
	time_start = time.time()
	for img in frames_list:
		# filling matrix with symbols
		min_value = np.amin(img)
		max_value = np.amax(img)
		for row in range(0, img.shape[0]):
			for pixel in range(0,len(img[row])):
				# print(pixel)
				symbolid = ((int(img[row][pixel]) - min_value) / (max_value - min_value) * len(symbols)) - 1
				pixel_scaled = symbols[int(symbolid)]
				new_matrix[row][pixel]= pixel_scaled


		# printing image, i got
		the_whole_string = ''
		for row in range(0, new_matrix.shape[0]):
			string = ''
			for pixel in range(0,len(new_matrix[row])):
				string += str(new_matrix[row][pixel])
			the_whole_string = the_whole_string + string
		print(the_whole_string)

		time.sleep(1/24)
		# print('\n' * 63)

print(time.time()-time_start)
input()


