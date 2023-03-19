import tensorflow as tf
import keras
import numpy as np
from PIL import Image
import os

# List available devices and print

from tensorflow.python.client import device_lib 
print(device_lib.list_local_devices())

#Disable GPU: to disable GPU un-comment the next line of code

# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Load model

loaded_model = tf.keras.models.load_model('r341')

# Allocate space for the image

myImage = np.zeros(((1,128,128)))

# Read image and make grayscale. Assuming correct size.

myImage[0,:,:] = Image.open("myImage1.jpg").convert('L') # convert('L') makes it grayscale
# myImage[0,:,:] = Image.open("myImage2.jpg").convert('L') # convert('L') makes it grayscale

# Convert the grayscale image to binary

for i in range(128):
	for j in range(128):
		if myImage[0, i, j] < 150:
			myImage[0, i, j] = 0
		else:
			myImage[0, i, j] = 1

# Predict and print image

keff = loaded_model.predict(myImage)

print("Keff/kf = ", keff)
