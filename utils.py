import cv2
import numpy as np
from PIL import Image
import io
 
# PIL - opencv
def pil_to_cv(img):
    img = np.array(img)
    return cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

# OpenCV → bytes
def cv_to_bytes(img): 
    _, buffer = cv2.imencode('.png', img) 
    return buffer.tobytes() 