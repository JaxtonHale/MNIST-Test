#Remember to download mnist_train and mnist_test!!

import numpy as np
import matplotlib.pyplot as plt
image_size = 28
num_labels = 10
num_pixels_per_image = image_size * image_size
train_data = np.loadtxt("mnist_train.csv", delimiter=",")
test_data = np.loadtxt("mnist_test.csv", delimiter=",")

print('primed')
print(train_data[1])
