import numpy as np
import cv2

image = cv2.imread(f'.\\', cv2.IMREAD_GRAYSCALE)
image_array = np.array(image)

def convolution2d(image, filter_kernel):
    filter_height, filter_width = filter_kernel.shape
    image_height, image_width = image.shape
    
    conv_result = np.zeros((image_height, image_width))
    
    padded_image = np.pad(image, ((filter_height // 2, filter_height // 2), 
                                  (filter_width // 2, filter_width // 2)), mode='constant')
    
    for i in range(image_height):
        for j in range(image_width):
            region = padded_image[i:i + filter_height, j:j + filter_width]
            conv_result[i, j] = np.sum(region * filter_kernel)
    
    return conv_result

xSobel = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

ySobel = np.array([[-1, -2, -1],
                    [ 0,  0,  0],
                    [ 1,  2,  1]])

edge_x = convolution2d(image_array, xSobel)
edge_y = convolution2d(image_array, ySobel)

edges = np.hypot(edge_x, edge_y)
edges = edges / edges.max() * 255


cv2.imshow('تشخیص لبه', edges.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
