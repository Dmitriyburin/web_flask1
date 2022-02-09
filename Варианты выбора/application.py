from flask import Flask
from flask import url_for, request, render_template
from random import randint

app = Flask(__name__)

planets_dict = {
    'Mars': ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!'],
    'Pluto': ['Здесь очень холодно.', 'Мало полезных ресурсов.', 'Далеко до Земли.', 'Вообще не считают планетой.',
              'Не жизнь, а сказка!'],
    'Saturn': ['Есть кольцо из метеоритов.', 'Красивые бесконечные виды.', 'Гораздо больше места.',
               'Состоит из газов и жидкости.', 'Невероятно новые ощущения!']
}


@app.route('/choice/<planet_name>', methods=['GET'])
def form_sample(planet_name):
    url_style = url_for('static', filename='css/style.css')
    if planet_name not in planets_dict:
        return '<h1>Такой планеты у нас еще нет(</h1>'

    sent_for_planet = planets_dict[planet_name]
    if request.method == 'GET':
        return render_template('index.html', url_style=url_style, sent_for_planet=sent_for_planet, planet=planet_name)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
