# coding: UTF-8
from flask import request, render_template


def to_repast_by_stores_id(stores_id):
    '''根据id到餐厅页面'''
    return render_template('repast.html',
                           stores_id=stores_id)
