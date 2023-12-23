# Преобразование в цветовое пространство LAB
import cv2
import numpy as np
from matplotlib import pyplot as plt

from scipy.stats import mode

'''
Цветовое пространство LAB (L - яркость, A - зеленый-красный, B - синий-желтый)
тот же алгос с модой, который я пыталась сделать вчера, работает норм, но задачу не решает
а вообще, цветовое пространство идейное очень, с помощью него можно баланс белого делать
'''

# Загрузка изображения
image = cv2.imread('../../pictures/pic1.jpg')
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Построение гистограмм каждого канала
for i in range(3):
    plt.subplot(3, 1, i + 1)
    plt.hist(lab_image[:, :, i].ravel(), bins=256, color='gray', alpha=0.75)
    plt.title(f'Channel {i}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Обрезка очень светлых и темных цветов (уменьшение контрастности)
lab_image[..., 0] = np.clip(lab_image[..., 0], 60, 200)  # Обрезка яркости L

# Извлечение каждого канала цветового пространства LAB
l_channel = lab_image[:, :, 0]
a_channel = lab_image[:, :, 1]
b_channel = lab_image[:, :, 2]

# Вычисление моды и среднего значения для каждого канала
mode_l, _ = mode(l_channel.ravel())
mean_l = np.mean(l_channel)

mode_a, _ = mode(a_channel.ravel())
mean_a = np.mean(a_channel)

mode_b, _ = mode(b_channel.ravel())
mean_b = np.mean(b_channel)

# Увеличение или уменьшение каждого канала на разницу между средним значением и модой
lab_image[..., 0] += int(mean_l - mode_l)
lab_image[..., 1] += int(mean_a - mode_a)
lab_image[..., 2] += int(mean_b - mode_b)

# Ограничение значений каналов LAB в допустимых пределах
lab_image[..., 0] = np.clip(lab_image[..., 0], 0, 255)
lab_image[..., 1] = np.clip(lab_image[..., 1], 0, 255)
lab_image[..., 2] = np.clip(lab_image[..., 2], 0, 255)

# Преобразование обратно в цветовое пространство BGR
final_image = cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)

# Отображение изображений
cv2.imshow('Original Image', image)
cv2.imshow('Adjusted Image', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
