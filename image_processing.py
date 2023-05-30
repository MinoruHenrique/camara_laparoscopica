import cv2

def HE(image):
    R, G, B = cv2.split(image)

    output1 = cv2.equalizeHist(R)
    output2 = cv2.equalizeHist(G)
    output3 = cv2.equalizeHist(B)

    equ = cv2.merge((output1, output2, output3))
    return equ

def gaussian_filter(image, kernel_size=5,sigmax=0):
    blur = cv2.GaussianBlur(image, (kernel_size,kernel_size),sigmax)
    return blur