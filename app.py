"""Flask app for Cupcakes"""
from flask import Flask, render_template, flash, redirect, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
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
    all_cupcakes = [c.serialize_cupcake() for c in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route('/api/cupcakes/<int:c_id>')
def get_cupcake(c_id):
    """Get data about a single cupcake"""
    cupcake = Cupcake.query.get_or_404(c_id)
    return jsonify(cupcake=cupcake.serialize_cupcake())


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """Create a cupcake"""
    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"], rating=request.json["rating"], image=request.json["image"])
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize_cupcake()), 201)


# @app.route('/api/cupcakes/<int:c_id>', methods=['PATCH'])
# def update_cupcake(c_id):
#     """Update a cupcake"""



# @app.route('/api/cupcakes/<int:c_id>', methods=['DELETE'])
# def delete_cupcake(c_id):
#     """Delete a cupcake"""