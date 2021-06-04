# from flask_wtf import FlaskForm
# from wtforms import StringField, FloatField
# from wtforms.validators import InputRequired, URL

# class AddNewCupcakeForm(FlaskForm):
#     """Create form for adding a new cupcake"""
#     flavor = StringField("Cupcake Flavor", validators=[InputRequired("Must include a flavor")])
#     size = StringField("Cupcake Size", validators=[InputRequired("Must include a size")])
#     rating = FloatField("Cupcake Rating", validators=[InputRequired("Must include a rating")])
#     image = StringField("Image URL of Cupcake", validators=[InputRequired("Must include an image URL"), URL()])