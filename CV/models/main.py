import cv2
import numpy as np

'''
здесь все процессы с картинками, тут вводишь пути к файлам, картинки показываются и сохраняются
'''

from brightness.main import adjust_brightness
from whitebalance.main import white_balance_correction, manual_white_balance_correction
from color.hue_correction import adjust_color
from color.contrast_correction import adjust_contrast

if __name__ == '__main__':
    image_path = '../pictures/pic4.jpg'
    image_path_2 = '../pictures/pic5.jpg'
    image = cv2.imread(image_path)
    image2 = cv2.imread(image_path_2)

    brightened = adjust_brightness(image, 5, 95)
    brightened_2 = adjust_brightness(image2, 5, 95)
    colored = adjust_color(brightened)
    colored_2 = adjust_color(brightened_2)

    # cv2.imshow('Original', image)
    # cv2.imshow('Original 2', image2)

    # cv2.imshow('pic1', colored)
    # cv2.imshow('pic2', colored_2)

    cl1 = adjust_contrast(colored)
    cl2 = adjust_contrast(colored_2)

    cv2.imshow("Image1", np.concatenate([image, cl1], axis=1))
    cv2.imshow("Image2", np.concatenate([image2, cl2], axis=1))

    cv2.imwrite('../pictures/pic4_white_balanced_and_brightened.jpg', cl1)
    cv2.imwrite('../pictures/pic5_white_balanced_and_brightened.jpg', cl2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
