import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

'''
мл принял ислам
'''

# чб признаки (гистограмма)
def get_grayscale_histogram(image):
    image = cv2.resize(image, (256, 256))
    return cv2.calcHist([image], [0], None, [256], [0, 256]).flatten()

'''
# цветовые признаки (гистограмма)
def get_color_histogram(image):
    image = cv2.resize(image, (256, 256))
    red_hist = cv2.calcHist([image], [0], None, [256], [0, 256]).flatten()
    green_hist = cv2.calcHist([image], [1], None, [256], [0, 256]).flatten()
    blue_hist = cv2.calcHist([image], [2], None, [256], [0, 256]).flatten()
    return np.concatenate([red_hist, green_hist, blue_hist])'''


'''# объединяем все признаки в один вектор
def get_features(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_hist = get_grayscale_histogram(gray)
    color_hist = get_color_histogram(image)
    return np.concatenate([gray_hist])'''


# косинусное сходство между векторами признаков
def get_similarity(features1, features2):
    return cosine_similarity([features1], [features2])[0][0]


if __name__ == '__main__':
    pic1 = cv2.imread('../../pictures/pic1.jpg')
    pic2 = cv2.imread('../../pictures/pic1_white_balanced_and_brightened.jpg')

    features1 = get_grayscale_histogram(pic1)
    features2 = get_grayscale_histogram(pic2)

    print(get_similarity(features1, features2))
