import datetime
import json

from flask import Blueprint, request, jsonify, abort

from app.api.code_msg import code, msg
from app import db
from ..admin.model import Commodity_repertory, User

admin_api = Blueprint('admin_api',__name__)

@admin_api.route('/')
def hello_world():
    # api = APITest('http://127.0.0.1:5001')
    # data = api.login('12345678901', '123456')
    # print(data.get('message'))

    return "admin_api"

@admin_api.route('/addrepertory',methods=['POST'])
def addRepertory():

    print(request.get_json(force=True))
    json_obj = request.get_json(force=True)
    # print(json_obj)

    list = json_obj["json"]

    # 除了插入到仓库 还需要插入到商品列表和赠品列表
    # 目前完成了插入到仓库
    try:
        for dict in list:
            rep = dict2obj(Commodity_repertory(), dict)
            rep.time = datetime.datetime.now()
            db.session.add(rep)
    except Exception as e:
        return jsonify({"code":"201"})

    db.session.commit()


    # print(rep.name)
    # print(rep.weight)
    # print(rep.operator)
    # print(rep.purchase_price)

    # name = request.get_json().get('name')
    # purchase_price = request.get_json().get('purchase_price')
    # operator = request.get_json().get('operator')
    # weight = request.get_json().get('weight')
    #
    # repertory = Commodity_repertory(name,purchase_price,operator,weight)
    # repertory.time = datetime.datetime.now()
    # try:
    #     db.session.add(repertory)
    #     db.session.commit()
    #     return jsonify({code: "200"})
    # except Exception as e:
    #     print(e)
    #     return jsonify({code: "201", msg: "error"})

    return jsonify({"code":"200"})

# dict转obj，先初始化一个obj
def dict2obj(obj,dict):
    obj.__dict__.update(dict)
    return obj
# @admin_api.before_request
# def before_request():
#     if request.get_json() == None:
#         print("fdafda")
#         abort(4000)
#     return

