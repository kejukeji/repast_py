# coding: utf-8

import sys
from repast.weixin.webchat import WebChat


reload(sys)
sys.setdefaultencoding('UTF-8')

appid = 'wx55970915710ceae8'
secret = '0a9fcd79087745628d8eb5dd5fb9c418'

webChat = WebChat('1234',appid,secret)
menu = """
{
   "button": [
       {
            "type":"CLICK",
           "name":"主页",
           "key":"home"
       },
       {
           "type":"CLICK",
           "name": "进度",
           "key": "schedule"
       },
       {
           "type": "CLICK",
           "name": "我的",
           "key": "my"
       }
       ]
}
"""
#webChat.delete_menu()
# webChat.create_menu(menu)
#msg = "你好"
#open_id = "oFmv0t6ixCu5Hn_DT0iypHxy6zPQ"
#errmsg = webChat.send_text_message(open_id,msg)
#print errmsg

import Image
im = Image.open('/Users/K/Documents/Code/Python/repast_py/repast/static/images/img/rou.jpg')
im.thumbnail((456, 267))
im.save('/Users/K/Documents/Code/Python/repast_py/repast/static/images/img/rou_thumbnail.png', 'jpeg')