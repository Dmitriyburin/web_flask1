from flask import Flask
from flask import url_for, render_template

app = Flask(__name__)


@app.route('/training/<val>', methods=['POST', 'GET'])
def form_sample(val):
    url_style = url_for('static', filename='css/style.css')
    url_img = url_for('static', filename='img/1.png')
    return render_template('index.html', url_style=url_style, url_img=url_img, prof=val)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)

