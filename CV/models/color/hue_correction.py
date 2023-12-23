import cv2
import numpy as np

'''
пока что лучший вариант из всей цветокоррекции, которая есть, но работает по-терпильному
'''

# пересчёт яркости пикселей каждого цветового канала
def adjust_color(image):
    b, g, r = cv2.split(image)

    min_b, max_b = np.percentile(b, [5, 95])
    min_g, max_g = np.percentile(g, [5, 95])
    min_r, max_r = np.percentile(r, [5, 95])

    b = b * ((max_b - min_b) / 255.0) + min_b
    g = g * ((max_g - min_g) / 255.0) + min_g
    r = r * ((max_r - min_r) / 255.0) + min_r

    b = np.clip(b, 0, 255).astype('uint8')
    g = np.clip(g, 0, 255).astype('uint8')
    r = np.clip(r, 0, 255).astype('uint8')

    corrected_image = cv2.merge([b, g, r])

    return corrected_image
