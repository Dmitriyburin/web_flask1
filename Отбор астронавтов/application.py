from flask import Flask
from flask import url_for, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    url_style = url_for('static', filename='css/style.css')
    if request.method == 'GET':
        return render_template('index.html', url_style=url_style)
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['file'])
        print(request.form['prof'])
        print(request.form['education'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])

        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
