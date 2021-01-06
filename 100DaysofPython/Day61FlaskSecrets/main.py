from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
app.secret_key = "some secret string"


class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[
                             DataRequired(), Length(min=8)])
    login = SubmitField(label='Login')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    print(f"{form.email.data},{type(form.password.data)}, {form.validate_on_submit()}")
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            print('success')
            return render_template('success.html')
        else:
            print('denied')
            return render_template('denied.html')
    else:
        print('retry')
        return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
