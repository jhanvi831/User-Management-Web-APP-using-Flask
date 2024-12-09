from flask import Blueprint, redirect, render_template, url_for
from controllers.user import add_user_function, delete_user_function, edit_user_function
import sys
from models.user import User

# Create a blueprint named 'main'
main = Blueprint('main', __name__)

# Define a route within the blueprint
@main.route('/', methods=['GET'])
def home():
    data = User.get_all()
    return render_template('index.html', data=data)

@main.route('/adduser', methods=['GET', 'POST'])
def add_user():
    data = add_user_function()
    print(data, file=sys.stderr)
    return render_template('adduser.html', data=data)

@main.route('/edituser/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.get_by_id(id)
    data = edit_user_function(user)
    print(data, file=sys.stderr)
    return render_template('edituser.html', user=user, data=data)

@main.route('/deleteuser/<int:id>', methods=['POST'])
def delete_user(id):
    user = User.get_by_id(id)
    delete_user_function(user)
    return redirect(url_for('main.home'))
