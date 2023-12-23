import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    cv2.imshow("Aboba", img)
    cv2.waitKey(1)

# Загрузка изображений
images = [cv2.imread('image1.jpg'), cv2.imread('image2.jpg'), cv2.imread('image3.jpg')]

# Создание пустого массива для хранения корректированных изображений
corrected_images = []

# Загрузка цветовой карты
color_map = cv2.imread('color_map.jpg')

# Применение цветовой карты к каждому изображению
for image in images:
    # Изменение размера цветовой карты до размеров изображения
    color_map_resized = cv2.resize(color_map, (image.shape[1], image.shape[0]))

    # Применение цветовой карты к изображению
    corrected_image = cv2.addWeighted(image, 0.5, color_map_resized, 0.5, 0)

    # Добавление корректированного изображения в массив
    corrected_images.append(corrected_image)

# Отображение результатов
for image in corrected_images:
    cv2.imshow('Corrected Image', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
