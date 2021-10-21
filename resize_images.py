import cv2
import os
import glob
from tqdm import tqdm

resize = 512
outputFolder = "data/train_resized"
imagePathlist=glob.glob("data\\train\\*")
for imagePath in tqdm(imagePathlist):
    img = cv2.imread(imagePath)
    img = cv2.resize(img, (resize, resize))
    imgPath = os.path.join(outputFolder, os.path.basename(imagePath))
    cv2.imwrite(imgPath, img)