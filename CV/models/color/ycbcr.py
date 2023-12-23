import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy import uint8
from scipy.stats import mode

'''
Цветовое пространство YCrCb (Y - яркость, Cr - красный, Cb - синий)
опять алгос с модой, работает почти так же как lab, но пространство другое
'''

def adjust_contrast_brightness(image, alpha, beta):
    # Применение линейного преобразования к изображению
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted_image


def main():
    # Загрузка изображения
    image = cv2.imread('../../pictures/pic1.jpg')

    # Преобразование в цветовое пространство YCrCb
    ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

    # Построение гистограмм каждого канала
    for i in range(3):
        plt.subplot(3, 1, i + 1)
        plt.hist(ycbcr_image[:, :, i].ravel(), bins=256, color='gray', alpha=0.75)
        plt.title(f'Channel {i}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

    # Обрезка очень светлых и темных цветов (уменьшение контрастности)
    ycbcr_image[..., 0] = np.clip(ycbcr_image[..., 0], 60, 200)  # Обрезка яркости Y

    y_channel = ycbcr_image[:, :, 0]
    cr_channel = ycbcr_image[:, :, 1]
    cb_channel = ycbcr_image[:, :, 2]

    # Вычисление моды каждого канала
    mode_y, _ = mode(y_channel.ravel())
    mode_cr, _ = mode(cr_channel.ravel())
    mode_cb, _ = mode(cb_channel.ravel())

    # Вычисление среднего значения каждого канала
    mean_y = np.mean(y_channel)
    mean_cr = np.mean(cr_channel)
    mean_cb = np.mean(cb_channel)

    # Увеличение или уменьшение каждого канала на разницу между средним значением и модой
    ycbcr_image[..., 0] -= (mean_y - mode_y).astype(uint8)
    ycbcr_image[..., 1] -= (mean_cr - mode_cr).astype(uint8)
    ycbcr_image[..., 2] -= (mean_cb - mode_cb).astype(uint8)

    # Ограничение значений каналов YCrCb в допустимых пределах
    ycbcr_image[..., 0] = np.clip(ycbcr_image[..., 0], 0, 255)
    ycbcr_image[..., 1] = np.clip(ycbcr_image[..., 1], 0, 255)
    ycbcr_image[..., 2] = np.clip(ycbcr_image[..., 2], 0, 255)

    # Преобразование обратно в цветовое пространство BGR
    final_image = cv2.cvtColor(ycbcr_image, cv2.COLOR_YCrCb2BGR)

    # Отображение изображений
    cv2.imshow('Original Image', image)
    cv2.imshow('Adjusted Image', final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
