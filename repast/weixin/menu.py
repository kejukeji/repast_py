# coding: utf-8
import urllib
import urllib2
from urllib import urlencode
import json
import sys
from repast.weixin.webchat import WebChat
from repast.setting.wbb import BASE_URL

reload(sys)
sys.setdefaultencoding('UTF-8')

appid = 'wx55970915710ceae8'
secret = '0a9fcd79087745628d8eb5dd5fb9c418'

webChat = WebChat('1234',appid,secret)
menu = """
{
   "button": [
       {
            "type":"view",
           "name":"主页",
           "url":"%s/restful/group"
       },
       {
           "type":"click",
           "name": "进度",
           "key": "schedule"
       },
       {
           "type": "click",
           "name": "我的",
           "key": "my"
       }
       ]
}
""" %(BASE_URL)
#webChat.delete_menu()
webChat.create_menu(menu)