import cv2


def adjust_contrast(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    R, G, B = cv2.split(image)

    output1_R = clahe.apply(R)
    output1_G = clahe.apply(G)
    output1_B = clahe.apply(B)

    return cv2.merge((output1_R, output1_G, output1_B))
