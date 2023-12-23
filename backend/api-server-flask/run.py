import os

from flask import Flask, request, jsonify, render_template

import config
app = Flask(__name__, template_folder=config.template_dir, static_folder=config.static_dir)


@app.route('/api/color_correction', methods=['POST'])
def color_correction():
    results = {'status': 'success', 'corrected_images': []}

    for file in request.files.getlist('file'):
        filename = file.filename
        filepath = os.path.join('static/uploads', filename)
        file.save(filepath)
        results['corrected_images'].append(filepath)

    return jsonify(results)


@app.route('/api/glare_out', methods=['POST'])
def glare_out():
    uploaded_file = request.files['file']  # change filename
    return jsonify("glared_out")


@app.route('/check', methods=['GET'])
def check():
    return jsonify("aboba")

@app.route('/index.html', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=config.host, port=config.port, debug=True)
