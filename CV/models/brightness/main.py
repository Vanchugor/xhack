import cv2
import numpy as np

'''
работа с яркостью картинки
'''

# пересчёт яркости пикселей относительно другого диапазона
def adjust_brightness(image, left, right):
    ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    y_channel = ycbcr_image[:, :, 0]
    min_val, max_val = np.percentile(y_channel, [left, right])

    y_channel_modified = y_channel * ((max_val - min_val) / 255.0) + min_val
    y_channel_modified = np.clip(y_channel_modified, 0, 255).astype('uint8')

    ycbcr_image[:, :, 0] = y_channel_modified
    modified_image = cv2.cvtColor(ycbcr_image, cv2.COLOR_YCrCb2BGR)

    return modified_image


# просто подгоняем пиксели под нужный диапазон
def clip_pixels(image, left, right):
    ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    y_channel = ycbcr_image[:, :, 0]
    y_channel_modified = np.clip(y_channel, left, right).astype('uint8')

    ycbcr_image[:, :, 0] = y_channel_modified
    modified_image = cv2.cvtColor(ycbcr_image, cv2.COLOR_YCrCb2BGR)

    return modified_image
