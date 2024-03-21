import cv2
import easyocr
import matplotlib.pyplot as plt
import os
# import numpy as np


# read image
image_path = os.path.dirname(os.path.abspath(__file__)) + '\\data\\test4.jpg'
img = cv2.imread(image_path)

# instance text detector
reader = easyocr.Reader(['en'], gpu=False) # English language, no GPU support

# detect text on image
text_ = reader.readtext(img) # returns list of detected text

threshold = 0.25
# draw bbox and text
for t_, t in enumerate(text_):
    print(t)

    bbox, text, score = t # [Bounding box coords, Text read, Accuracy or Chance of True Positive?]

    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2) # Font size = 0.65

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
