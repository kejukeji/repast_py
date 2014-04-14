# coding: utf-8
from ..setting.config import *
from ..weixin.webchat import WebChat
from ..services.queue_service import *
from ..services.user_service import *

class PushMessage():
    '''叫号时候推送消息给后面3个人'''
    def push_message(self, queue_id):
        queue = get_q_by_id(queue_id)
        open_id = ''
        if queue:
            user_id = queue.user_id
            user = get_user_by_id(user_id)
            if user:
                open_id = user.openid
        webChat = WebChat('1234', APPID, SECRET)
        content = '很快就要到您呢， 请到餐厅等待。'
        webChat.send_text_message(open_id, content)