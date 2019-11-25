from flask import request, jsonify
from project import app
from project.models import User
from project.serializers import UserSerializer
from project import db


@app.route('/')
def hello():
    return f'Hello, World!'


#user = {'name':'Tugce','pin':12345,'balance':1000}
#users = [{'name':'John','pin':12345,'balance':1000}, {'name':'Jane','pin':12345,'balance':2000}]

#@app.route('/users')
#def getUsers():
 #   xxxx = User.query.all()
  #  return jsonify(xxxx[0].name)


@app.route('/users', methods=["GET"])
def show_users():
    users = User.query.all()
    results = []

    for user in users:
        serialized_user = UserSerializer.serialize(user)
        results.append(serialized_user)

    return jsonify(results)

@app.route('/users', methods=["POST"])
def create_user():
    body = request.get_json()
    name = body.get("name")
    pin = body.get("pin")
    balance = body.get("balance")

    new_user = User(name=name, pin=pin, balance=balance)
    db.session.add(new_user)
    db.session.commit()
    return "OK"

@app.route('/users/<name>', methods=["DELETE"])
def delete_user(name):
    u = User.query.filter_by(name=name).delete()
    db.session.commit()
    return "Deleted"

    new_user = User(name=name, pin=pin, balance=balance)
    db.session.add(new_user)
    db.session.commit()
    return "OK"


@app.route('/balance')
def display_balance():
    pin = int(request.args.get('pin'))
    user = request.args.get('name')
    user_data = User.query.filter_by(name=user).first()
    if pin == user_data.pin:
        return 'This is your current amount of money: {}'.format(user_data.balance)
    else:
        return 'Incorrect PIN!!!'


@app.route('/withdraw', methods=["PUT"])
def withdraw_money():
    body = request.get_json()
    name = body.get("name")
    pin = body.get("pin")
    withdraw = body.get("withdraw")
    user_data = User.query.filter_by(name=name).first()
    if pin == user_data.pin:
        if withdraw <= user_data.balance:
            user_data.balance=user_data.balance-withdraw
            db.session.add(user_data)
            db.session.commit()
            return jsonify(UserSerializer.serialize(user_data))
        else:
            return "Insufficient Funds"  

    else:
        return 'Incorrect PIN!!!'


