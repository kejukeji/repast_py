# coding: UTF-8
from flask import request, render_template
from repast.services.queue_setting_service import *

from repast.util.session_common import *

def do_queue(table_type_id):
    '''用户排队'''
    #user_id = get_session('user_id') # 得到当前用户id
    user_id = 1
    #stores_id = request.args.get('stores_id') # 用户排队的餐厅
    stores_id = 6
    queue = check_queue_by_user_id_and_stores_id(user_id, stores_id, table_type_id) # 判断是否已经存在队列当中
    if queue:
        message = '您已在队列中，当前号码为%s' %(queue.now_queue_number) # 如果存在队列中，提示
        print message
    else:
        queue = create_queue(user_id, stores_id, table_type_id)
        print queue.id


def cancel_queue(queue_id):
    '''取消队列'''
    cancel(queue_id)



if __name__ == '__main__':
    #do_queue(1)
    cancel(1)




