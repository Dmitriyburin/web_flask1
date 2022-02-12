from tkinter import E
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username1 = StringField('id капитана', validators=[DataRequired()])
    password1 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    url_style = url_for('static', filename='css/style.css')
    emblem = url_for('static', filename='img/emblem.png')
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', url_style=url_style, title='Авторизация', 
        form=form, emblem=emblem)

@app.route('/success')
def succes():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
