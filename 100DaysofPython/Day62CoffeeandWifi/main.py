from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, URL
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location (Google Maps URL)',
                           validators=[DataRequired(), URL()])
    open = StringField('Opening Time (e.g. 8am)', validators=[DataRequired()])
    close = StringField('Closing Time (e.g. 10pm)',
                        validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=[
                         "☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=[
                       "✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@ app.route("/")
def home():
    return render_template("index.html")


@ app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('/Users/smith/python/100DaysofPython/Day62CoffeeandWifi/cafe-data.csv') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@ app.route('/cafes')
def cafes():
    with open('/Users/smith/python/100DaysofPython/Day62CoffeeandWifi/cafe-data.csv', newline='') as csv_file:
        csv_data = pd.read_csv(csv_file)
    return render_template('cafes.html', rows=list(csv_data.values.tolist()), titles=csv_data.columns.values)


if __name__ == '__main__':
    app.run(debug=True)
