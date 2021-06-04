"""Flask app for Cupcakes"""
from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Cupcake
# from forms

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "santanarush"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/api/cupcakes')
def list_cupcakes():
    """Get data about all cupcakes"""



@app.route('api/cupcakes/<int:c_id>')
def get_cupcake(c_id):
    """Get data about a single cupcake"""



@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """Create a cupcake"""



@app.route('/api/cupcakes/<int:c_id>', methods=['PATCH'])
def update_cupcake(c_id):
    """Update a cupcake"""



@app.route('/api/cupcakes/<int:c_id>', methods=['DELETE'])
def delete_cupcake(c_id):
    """Delete a cupcake"""