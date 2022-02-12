from flask import Flask
from flask import url_for, render_template

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def form_sample():
    param = {}
    param['title'] = 'Анкета'
    param['surname'] = 'Бурин'
    param['name'] = 'Дмитрий'
    param['education'] = 'Среднее'
    param['profession'] = 'Программист'
    param['sex'] = 'Мужской'
    param['motivation'] = 'Я ГОТОВ ЛЕТАТь'
    param['ready'] = True

    url_style = url_for('static', filename='css/style.css')
    return render_template('auto_answer.html', url_style=url_style, **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
