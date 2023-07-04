import cv2 as cv
import numpy as np
import sys
filename = '17m.png'

image = cv.imread(filename=filename, flags=0)
image_shape = image.shape
output_image = np.zeros(image_shape, dtype=np.uint8)
for j in range(image_shape[0]):
    for l in range(image_shape[1]):
        output_image[j][l] = 255

count =0

def bfs(x, y):
    global output_image
    global image
    global count

    queue = [(x, y)]  
    while queue:
        x, y = queue.pop(0)
        if image[x][y] == 0 and output_image[x][y]:
            output_image[x][y] = 0
            count += 1

            if x + 1 < image_shape[0]:
                queue.append((x + 1, y))
            if x - 1 >= 0:
                queue.append((x - 1, y))
            if y + 1 < image_shape[1]:
                queue.append((x, y + 1))
            if y - 1 >= 0:
                queue.append((x, y - 1))

def process():
    first = -1
    last = -1
    global output_image

    for j in range(image_shape[0]):
        
        for l in range(image_shape[1]):
            if(output_image[j][l] == 0 and first == -1):
                first = l
            if(output_image[j][image_shape[1]-l-1] == 0 and last == -1):
                last = image_shape[1] - l
        
        for l in range(first,last):
            output_image[j][l] = 0

        first = -1
        last = -1
_, image = cv.threshold(image, 80, 255, cv.THRESH_BINARY)
bfs(0,0)
cv.imwrite(filename.split('.')[0] +'_process.png',output_image)
process()
cv.imwrite(filename.split('.')[0] +'_process_dark .png',output_image)


'''
Just put the image file in the same folder as this file and change the filename on line number 4 to the name of the file and run the code
'''