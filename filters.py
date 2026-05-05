import numpy as np
import cv2

# blur 
def apply_blur(img,ksize):
    if ksize % 2 ==0:
        ksize +=1

    blur = cv2.GaussianBlur(img,(ksize,ksize),0)
    return blur
 # sharpness

def apply_sharpness(img, alpha):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharp = cv2.filter2D(img , -1 , kernel)
    result = cv2.addWeighted(img, 1 - alpha, sharp, alpha, 0)
    return result
# brightness
def adjust_brightness(img,beta):
    bright = cv2.convertScaleAbs(img,alpha=1,beta=beta)
    return bright
 # contrast
def adjust_contrast(img,alpha):
    contrast = cv2.convertScaleAbs(img,alpha=alpha,beta=0)
    return contrast
# Edge Detection
def apply_canny(img, t1, t2):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, t1, t2)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
# Grayscale 
def apply_grayscale(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

