import cv2
import numpy as np
from scipy import stats

'''
ебанутая солянка из методов для коррекции баланса белого, включая автоматическую из opencv, 
ручную на основе алгоса из интернета с логарифмами (он не работает) и тут было что-то ещё, но я это, кажется, удалила
'''
def calculate_pixel_temperature(hue):
    temp_min = 1000
    temp_max = 40000

    hue_norm = hue / 180.0
    temp = temp_min * (1 - hue_norm) + temp_max * hue_norm

    return temp


def img_to_float(image):
    return image.astype('float32') / 255.0


def img_to_uint8(image):
    return (image * 255.0).astype('uint8')


def white_balance_correction(image):
    wb = cv2.xphoto.createSimpleWB()
    corrected_image = wb.balanceWhite(image)

    return corrected_image


def calculate_pixel_color(temp):
    temp = temp / 100
    r, g, b = 0, 0, 0
    if temp <= 66:
        r = 255
        g = 99.4708025861 * np.log(temp) - 161.1195681661
        if temp <= 19:
            b = 0
        else:
            b = 138.5177312231 * np.log(temp - 10) - 305.0447927307
    else:
        r = 329.698727446 * ((temp - 60) ** -0.1332047592)
        g = 288.1221695283 * ((temp - 60) ** -0.0755148492)
        b = 255

    r = np.clip(r, 0, 255).astype('uint8')
    g = np.clip(g, 0, 255).astype('uint8')
    b = np.clip(b, 0, 255).astype('uint8')

    return r, g, b

def manual_white_balance_correction(image):
    image = img_to_float(image)
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue = image_hsv[:, :, 0]
    for i in range(len(hue)):
        for j in range(len(hue[i])):
            r, g, b = calculate_pixel_color(calculate_pixel_temperature(hue[i][j]))
            image[i][j][0] = r
            image[i][j][1] = g
            image[i][j][2] = b

    image = img_to_uint8(image)
    return image
