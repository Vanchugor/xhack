# Преобразование в цветовое пространство HSV
import cv2
import numpy as np
from matplotlib import pyplot as plt

from numpy import uint8
from scipy.stats import mode


'''
какой-то всратый черновик
с помощью гистограмм пытается определить, какие цвета на картинке преобладают, и подгоняет их под нужный диапазон
(оно очень плохо работает)
'''

# Загрузка изображения
image = cv2.imread('../../pictures/pic1.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Построение гистограмм каждого канала
for i in range(3):
    plt.subplot(3, 1, i + 1)
    plt.hist(hsv_image[:, :, i].ravel(), bins=256, color='gray', alpha=0.75)
    plt.title(f'Channel {i}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Обрезка очень светлых и темных цветов (уменьшение контрастности)
hsv_image[..., 2] = np.clip(hsv_image[..., 2], 60, 200)  # Обрезка значения V (яркость)

# Извлечение каждого канала цветового пространства HSV
h_channel = hsv_image[:, :, 0]
s_channel = hsv_image[:, :, 1]
v_channel = hsv_image[:, :, 2]

# Вычисление моды и среднего значения для каждого канала
mode_h, _ = mode(h_channel.ravel())
mean_h = np.mean(h_channel)

mode_s, _ = mode(s_channel.ravel())
mean_s = np.mean(s_channel)

mode_v, _ = mode(v_channel.ravel())
mean_v = np.mean(v_channel)

# Увеличение или уменьшение каждого канала на разницу между средним значением и модой
hsv_image[..., 0] += int(mean_h - mode_h)
hsv_image[..., 1] += int(mean_s - mode_s)
hsv_image[..., 2] += int(mean_v - mode_v)

# Ограничение значений каналов HSV в допустимых пределах
hsv_image[..., 0] = np.clip(hsv_image[..., 0], 0, 179)  # Оттенок в пределах [0, 179]
hsv_image[..., 1] = np.clip(hsv_image[..., 1], 0, 255)  # Насыщенность в пределах [0, 255]
hsv_image[..., 2] = np.clip(hsv_image[..., 2], 0, 255)  # Значение в пределах [0, 255]

# Преобразование обратно в цветовое пространство BGR
final_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

# Отображение изображений
cv2.imshow('Original Image', image)
cv2.imshow('Adjusted Image', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
