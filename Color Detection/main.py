import cv2

from util import get_limits
from PIL import Image


yellow = [0, 255, 255] # Yellow in BGR colorspace
cap = cv2.VideoCapture(0) # No external cams, built-in cam is 0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Applying mask for specified color range
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=yellow)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Using the Pillow library
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox() # bbox is "bounding box"

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 5)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    '''
    "What does ord('q') and 0xFF mean? How is it being used here?"
    -   ord('q') returns the Unicode code point of q
    -   cv2.waitkey(1) returns a 32-bit integer corresponding 
        to the pressed key
    -   0x0000_00FF is a bit mask which sets the left 24 bits to zero, 
        because ord() returns a value betwen 0 and 255, since your 
        keyboard only has a limited character set
    -   Therefore, once the mask is applied, it is then possible 
        to check if it is the corresponding key.
    '''

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()