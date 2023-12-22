from flask import Flask, request, jsonify
import config

app = Flask(__name__)


@app.route('/api/correct', methods=['POST'])
def color_correction():
    images = request.files.getlist('images')  # change to one file
    results = {'status': 'success', 'corrected_images': []}

    for img in images:
        # Обработка каждого изображения и выполнение цветокоррекции
        corrected_image = img

        # Добавление корректированного изображения в список
        results['corrected_images'].append(corrected_image)

    return jsonify(results)


@app.route('/api/glare_out', methods=['POST'])
def glare_out():
    uploaded_file = request.files['file']  # change filename
    return jsonify("glared_out")


@app.route('/check', methods=['GET'])
def check():
    return jsonify("aboba")


if __name__ == '__main__':
    app.run(host=config.host, port=config.port, debug=True)
