from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '75258a82e2ea078c0f545eca3c7a3d10'

class InputForm(FlaskForm):
    input = TextAreaField('Введите строку', validators=[DataRequired()])
    submit = SubmitField('Отправить')

@app.route('/', methods=['GET', 'POST'])
def input():
    form = InputForm()
    output = ''
    if form.validate_on_submit():
        output = count_digits(form.input.data)
    return render_template('input.html', form=form, output=output)

def count_digits(string):
    digits_total = len(list(filter(lambda sym: sym.isdigit(), string)))
    return digits_total

if __name__ == '__main__':
    app.run()