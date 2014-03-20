# coding: UTF-8

from ..models.group import Group
from flask.ext import restful

class GetGroup(restful.Resource):
    '''获取区域'''
    @staticmethod
    def get():
        group = Group.query.filter().all()
        json = []
        for i in range(len(group)):
            json.append([group[i].id, group[i].name])
        return json