from flask import Flask
from flask import url_for, request, render_template
from random import randint

app = Flask(__name__)


@app.route('/', methods=['GET'])
def form_sample():
    url_style = url_for('static', filename='css/style.css')
    url_images = [url_for('static', filename='img/1.jpg'), url_for('static', filename='img/2.jpg'),
                  url_for('static', filename='img/3.jpg'), url_for('static', filename='img/4.jpg')]

    if request.method == 'GET':
        return render_template('index.html', url_style=url_style, url_images=url_images)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
