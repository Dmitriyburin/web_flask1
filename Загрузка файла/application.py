from flask import Flask
from flask import url_for, request, render_template
import os

app = Flask(__name__)
img = False


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    global img
    url_style = url_for('static', filename='css/style.css')
    if request.method == 'GET':
        print(img)
        return render_template('index.html', url_style=url_style, img=img)
    elif request.method == 'POST':
        f = request.files['file']
        if f.filename:
            try:
                if img:
                    print(img)
                    os.remove(img[1:])
            except FileNotFoundError:
                pass
            f.save(f'static/img/{f.filename}')
            img = url_for('static', filename=f'img/{f.filename}')
        return render_template('index.html', url_style=url_style, img=img)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
