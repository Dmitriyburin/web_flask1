from flask import Flask
from flask import url_for, render_template

app = Flask(__name__)


@app.route('/<title>', methods=['POST', 'GET'])
def form_sample(title):
    url_style = url_for('static', filename='css/style.css')
    return render_template('base.html', url_style=url_style, title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)

