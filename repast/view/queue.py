# coding: UTF-8

from repast.models.queue import Queue
from repast.util.session_common import *

def do_queue(table_type_id):
    '''用户排队'''
    user_id = get_session('user_id') # 得到当前用户id



