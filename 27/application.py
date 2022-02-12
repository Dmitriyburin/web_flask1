from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/table/<sex>/<int:age>')
def distribution(sex, age):
    url_style = url_for('static', filename='css/style.css')
    url_images = [url_for('static', filename='img/adult.png'), url_for('static', filename='img/young.png')]
    return render_template('cabin.html', url_style=url_style, sex=sex, age=age, young=url_images[1], adult=url_images[0])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
