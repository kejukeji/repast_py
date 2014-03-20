# coding: UTF-8

from ..models.group import Group
from flask.ext import restful
from ..util.session_common import *

class GetGroup(restful.Resource):
    '''获取区域'''
    @staticmethod
    def get():
        fromUserName = get_session('FromUserName')
        group = Group.query.filter().all()
        json = []
        json.append(['openid', fromUserName])
        for i in range(len(group)):
            json.append([group[i].id, group[i].name])
        return json