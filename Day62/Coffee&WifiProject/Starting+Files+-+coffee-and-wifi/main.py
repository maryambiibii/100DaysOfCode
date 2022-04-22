from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_key'
Bootstrap(app)

coffee_choices = [('1', '☕️'),('2', '☕️☕️'),('3', '☕️☕️☕️'),('4', '☕️☕️☕️☕️'),('5', '☕️☕️☕️☕️☕️')]
wifi_rating_choices = [('1', '✘'),('2', '💪'),('3', '💪💪'),('4', '💪💪💪'),('5', '💪💪💪💪'),('6', '💪💪💪💪💪')]
power_socket_choices = [('1', '✘'), ('2', '🔌️'),('3', '🔌🔌️') ,('4', '🔌🔌🔌️'),('5', '🔌🔌🔌🔌️'),('6', '🔌🔌🔌🔌️🔌️')]


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe Name', validators=[DataRequired()])
    location_URL = StringField(label='Cafe Location on Google Maps(URL)', validators=[DataRequired(), URL()])
    open_time = StringField(label='Open Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField(label='Close Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', choices= coffee_choices, validators=[DataRequired()])
    wifi_strength_rating = SelectField(label='Wifi Strength Rating', choices=wifi_rating_choices, validators=[DataRequired()])
    power_socket_availability = SelectField(label='Power Socket Availability', choices=power_socket_choices, validators=[DataRequired()])
    submit = SubmitField(label='Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = form.cafe.data
        location_URL = form.location_URL.data
        open_time = form.open_time.data
        closing_time = form.closing_time.data
        coffee_rating_data = dict(coffee_choices).get(form.coffee_rating.data)
        wifi_strength_rating_data = dict(wifi_rating_choices).get(form.wifi_strength_rating.data)
        power_socket_availability_data = dict(power_socket_choices).get(form.power_socket_availability.data)

        with open('cafe-data.csv', mode='a') as file:
            file.write(f'\n{cafe},{location_URL},{open_time},{closing_time},{coffee_rating_data},{wifi_strength_rating_data},{power_socket_availability_data}')
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
        return cafes()
    return render_template('add.html', form=form, submit=form.submit)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    print(list_of_rows)
    print(list_of_rows[1:])
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
