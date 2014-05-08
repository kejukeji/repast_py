# coding: utf-8
#from flask.ext import restful
#from flask.ext.restful import reqparse
#from repast.util.session_common import set_session_dish,get_session_dish

#class AddDish(restful.Resource):
#    """
#    得到前台用户添加的菜品
#    dish_number 菜品有几份
#    dish_id 添加菜品的id
#    """
#    parse = reqparse.RequestParser()
#    parse.add_argument('dish_number', type=str, required=True)
#    parse.add_argument('dish_id', type=str, required=True)
#    parse.add_argument('package_id', type=str, required=True)
#    parse.add_argument('dish_sort_id', type=str, required=True)
#
#    args = parse.parse_args()
#    dish_number = args['dish_number']
#    dish_id = args['dish_id']
#    package_id = args['package_id']
#    dish_sort_id = args['dish_sort_id']
#    operate = args['operate']
#
#    #用户点菜加减数量操作处理
#    dishes = get_session_dish()
#    for d in dishes:
#        if dish_id == d.id:
#            if operate =="add":
#                d.number = d.number+1
#            elif d.number <1:
#                dishes.remove(d)
#            else:
#                d.number = d.number-1
#    set_session_dish(dishes)