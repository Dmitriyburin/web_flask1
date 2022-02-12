from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/distribution', methods=['GET', 'POST'])
def distribution():
    url_style = url_for('static', filename='css/style.css')
    staff = ['Ридли Скот', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']

    return render_template('distribution.html', url_style=url_style, staff=staff)


@app.route('/success')
def succes():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
