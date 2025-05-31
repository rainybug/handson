##Sample##

import albumentations as A
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

print(np.__version__)

# 変形の種類を決定
transform = A.Compose([
    A.RandomBrightnessContrast(p=0.6),
    A.ElasticTransform(p=0.5),
    A.RandomGamma(p=0.6),
    A.Blur(p=0.5),
    A.RandomFog(p=0.5),
    A.RGBShift(p=0.6),
    A.Defocus(p=0.5),
    A.Downscale(p=0.5),
    A.ZoomBlur(p=0.4),
])


for i in range(0, 101):
    #パス設定
    root_file = "root_img/" + str(i) + ".jpg"
    des_dir = "albumed_img/" + str(i)
    des_file = "albumed_img/" + str(i) + "/" + str(i) 

    #エラーチェック（タイプ確認）
    print(type(root_file))
    
    #ディレクトリ生成
    if not os.path.exists(des_dir):
        os.makedirs(des_dir)

    #画像読み込み
    image = cv2.imread(root_file)
    print(type(image))

    #BGR(opencv)->RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print(type(image))

    #５０通りに拡張
    for k in range(0, 50):
        transformed = transform(image=image)
        transformed_image = transformed["image"]
        cv2.imwrite(des_file + "_albumed_" + str(k+1) + ".jpg", transformed_image)
    print(des_file + "_albumed_" + str(k) + ".jpg")