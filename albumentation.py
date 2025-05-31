##Sample##

import albumentations as A
import cv2
import numpy as np
import matplotlib.pyplot as plt

print(np.__version__)

# Declare an augmentation pipeline
transform = A.Compose([
    A.RandomBrightnessContrast(p=0.6),
    A.ElasticTransform(p=0.5),
    A.OpticalDistortion(p=0.6),
    A.RandomGamma(p=0.6),
    A.ShiftScaleRotate(p=0.3),
    A.HueSaturationValue(p=0.5),
    A.Blur(p=0.5),
    A.GridDistortion(p=0.6),
    A.Superpixels(p=0.5),
    A.RandomFog(p=0.5),
    A.RGBShift(p=0.6),
    A.Defocus(p=0.5),
    A.Downscale(p=0.5),
    A.ZoomBlur(p=0.4),
    A.GaussNoise(p=0.6)
])


for i in range(0, 100):
    root_file = "root_img/" + str(i) + ".jpg"
    des_file = "albumed_img/" + str(i) + "/" + str(i) 

    # Read an image with OpenCV and convert it to the RGB colorspace
    print(type(root_file))

    image = cv2.imread(root_file)
    print(type(image))

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print(type(image))

    # Augment an image

    for k in range(0, 50):
        transformed = transform(image=image)
        transformed_image = transformed["image"]

        cv2.imwrite(des_file + "_albumed_" + str(k+1) + ".jpg", transformed_image)
        
    print(des_file + "_albumed_" + str(k) + ".jpg")