from flask import Flask, render_template, url_for, request
import json
import os

app = Flask(__name__)


@app.route('/member')
def news():
    print(os.listdir())
    with open('templates/staff.json', "rt", encoding="utf8") as f:
        staff_list = json.loads(f.read())
    url_style = url_for('static', filename='css/style.css')
    return render_template('staff.html', url_style=url_style, staff=staff_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
