import cv2
import datetime as dt

'''
просто конвертер в пнг, должно хорошо работать по идее
'''
def convert_to_png(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)

    if image is not None:
        cv2.imwrite(output_image_path, image, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        print(f'Изображение успешно конвертировано в {output_image_path}')
    else:
        print('Не удалось прочитать изображение.')


def generate_img_name():
    return '../pictures/' + dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.png'


if __name__ == '__main__':
    input_image_path = '../pictures/pic1.jpg'
    output_image_path = generate_img_name()

    convert_to_png(input_image_path, output_image_path)
