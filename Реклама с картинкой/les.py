from flask import Flask
from flask import url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    countdown_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!',
                      'Пуск!']
    return '</br>'.join(countdown_list)


@app.route('/image_mars')
def image():
    return f'''
    <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                    <p>Красота какая!</p>
                  </body>
                </html>
        '''


@app.route('/promotion_image', methods=['POST', 'GET'])
def form_sample():
    promotion_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!',
                      'Пуск!']
    url_pic = url_for('static', filename='img/mars.png')
    url_style = url_for('static', filename='css/style.css')
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_style}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                          <h1>Жди нас, Марс!</h1>
                            <img src="{url_pic}" 
                            alt="здесь должна была быть картинка, но не нашлась">
                        <p>Красота какая!</p>
                            <div class="alert alert-primary" role="alert">
                              <h3>{promotion_list[0]}</h3>
                            </div>
                            <div class="alert alert-secondary" role="alert">
                              <h3>{promotion_list[1]}</h3>
                            </div>
                            <div class="alert alert-success" role="alert">
                              <h3>{promotion_list[2]}</h3>
                            </div>
                            <div class="alert alert-danger" role="alert">
                              <h3>{promotion_list[3]}</h3>
                            </div>
                            <div class="alert alert-warning" role="alert">
                               <h3>{promotion_list[4]}</h3>
                            </div>
                            <div class="alert alert-info" role="alert">
                              <h3>{promotion_list[5]}</h3>
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
