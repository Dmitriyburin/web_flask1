from flask import Flask
from flask import url_for, render_template

app = Flask(__name__)


@app.route('/list_prof/<list>', methods=['POST', 'GET'])
def form_sample(list):
    list_prof = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
                 'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                 'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман']
    url_style = url_for('static', filename='css/style.css')
    return render_template('index.html', url_style=url_style, list=list, list_prof=list_prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
