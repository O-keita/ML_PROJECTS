from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, DateField, SelectField
from wtforms.validators import DataRequired


class PredictForm(FlaskForm):
    city = SelectField('City', choices=[], validators=[DataRequired()])
    sale_date = DateField('Sale Date', format='%Y-%m-%d', validators=[DataRequired()])
    months_listed = FloatField('Months Listed', validators=[DataRequired()])
    bedrooms = SelectField('Bedrooms', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], validators=[DataRequired()])
    house_type = SelectField('House Type', choices=[], validators=[DataRequired()])
    area = FloatField('Area (sq.m)', validators=[DataRequired()])
   