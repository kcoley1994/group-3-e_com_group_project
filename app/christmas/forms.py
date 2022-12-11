from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class Productform(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField()

      #implament in form 
#     name = db.Column(db.String(50), nullable=False)
#     img_url = db.Column(db.String, nullable=False)
#     price = db.Column(db.Integer, nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     description = db.Column(db.String, nullable=False)