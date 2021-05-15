from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms.fields import SelectField
from wtforms.widgets import ListWidget, RadioInput
from wtforms.validators import DataRequired

SECRET_KEY = 'development'

app = Flask(__name__)
app.config.from_object(__name__)


class CustomRadioField(SelectField):
    widget = ListWidget(prefix_label=False)
    option_widget = RadioInput()

    def pre_validate(self, form):
        for v, _ in self.choices:
            if self.data == v:
                break
        else:
            raise ValueError(self.gettext('OMG, PICK SOMETHING'))


class SimpleForm(FlaskForm):
    example = CustomRadioField('Label', choices=[('value','aaa'),('aa','whatever')], validators=[DataRequired()])


@app.route('/',methods=['post','get'])
def hello_world():
    form = SimpleForm()
    if form.validate_on_submit():
        flash( form.example.data)
    else:
        flash( form.errors)
    return render_template('radio.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
