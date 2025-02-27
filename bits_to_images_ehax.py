import numpy as np
import cv2



for i in range(5000):
    f = open(f"./out/flag_{i+1}", "r")
    img_arr = np.array([[255 if int(z) == 1 else 0  for z in x.split(" ")] for x in f.read().split("\n")[:-1]], np.uint8)
    cv2.imwrite(f"./img/flag_{i+1}.jpg", img_arr)
    print(f"Made image {i+1}...")

