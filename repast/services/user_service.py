# coding: UTF-8

from repast.models.user import User
from repast.models.database import db


def insert_user(nickname, openid, img_url):
    user = User(nick_name=nickname, openid=openid, picture_url=img_url)
    db.add(user)
    db.commit()

if __name__ == '__main__':
    insert_user('温饱思淫欲,','aiwe13k4h3qfakf','kflsdjflk')
