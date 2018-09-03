import datetime

from flask import Blueprint, request, jsonify, abort

from app.api.code_msg import code, msg
from app import db
from ..admin.model import Commodity_repertory
admin_api = Blueprint('admin_api',__name__)

@admin_api.route('/')
def hello_world():
    # api = APITest('http://127.0.0.1:5001')
    # data = api.login('12345678901', '123456')
    # print(data.get('message'))

    return "admin_api"

@admin_api.route('/addrepertory',methods=['POST'])
def addRepertory():

    # print(request.get_json(force=True))
    name = request.get_json().get('name')
    purchase_price = request.get_json().get('purchase_price')
    operator = request.get_json().get('operator')
    weight = request.get_json().get('weight')

    repertory = Commodity_repertory(name,purchase_price,operator,weight)
    repertory.time = datetime.datetime.now()
    try:
        db.session.add(repertory)
        db.session.commit()
        return jsonify({code: "200"})
    except Exception as e:
        print(e)
        return jsonify({code: "201", msg: "error"})

# @admin_api.before_request
# def before_request():
#     if request.get_json() == None:
#         print("fdafda")
#         abort(4000)
#     return

