from flask import Flask
from flask import url_for, request, render_template
from random import randint

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>', methods=['GET'])
def form_sample(nickname, level: int, rating: float):
    url_style = url_for('static', filename='css/style.css')

    if request.method == 'GET':
        return render_template('index.html', url_style=url_style, nickname=nickname, level=level, rating=rating)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
