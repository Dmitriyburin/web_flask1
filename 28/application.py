from flask import Flask, render_template, url_for, request
import os

app = Flask(__name__)
try:
    os.chdir('static/img')
except FileNotFoundError:
    pass

@app.route('/galery', methods=['POST', 'GET'])
def distribution():
    images = os.listdir()
    url_style = url_for('static', filename='css/style.css')
    url_images = [url_for('static', filename=f'img/{img}') for img in images]
    if request.method == 'GET':
        return render_template('landscape.html', url_style=url_style, url_images=url_images)
    elif request.method == 'POST':
        f = request.files['file']
        if f.filename:
            try:
                f.save(f'{f.filename}')
            except FileNotFoundError:
                pass
            img = url_for('static', filename=f'img/{f.filename}')
            url_images.append(img)
        return render_template('landscape.html', url_style=url_style, url_images=url_images)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
