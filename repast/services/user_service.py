# coding: UTF-8

from repast.models.user import User
from repast.models.database import db
from repast.services.base_service import BaseService


class UserService(BaseService):
    '''用户'''
    def create_user(self, nickname, openid, picture_url):

        user = User(nick_name=nickname, openid=openid, picture_url=picture_url)
        return self.create_model(user)

    def update_user(self, longitude, latitude, openid):
        '''修改'''
        user = self.get_user_by_openid(openid)
        user.update(longitude=longitude,latitude=latitude)
        db.commit()

    def get_user_by_openid(self, openid):
        '''根据openid得到用户'''
        user = User.query.filter(User.openid == openid).first()
        return user

    def check_user_by_openid(self, openid, nickname, picture_url):
        user = self.get_user_by_openid(openid)
        if user:
            return user
        else:
            user = self.create_user(nickname, openid, picture_url)
            return user



    def get_location_and_save(self, openid, longitude, latitude):
        '''获取用户地址位置，并且保存'''
        user = self.get_user_by_openid(openid)
        user.update(longitude=longitude,latitude=latitude)
        db.commit()




def insert_user(nickname, openid, img_url):
    user = User(nick_name=nickname, openid=openid, picture_url=img_url)
    db.add(user)
    db.commit()

def get_user_by_id(id):
    user = User.query.filter(User.id == id).first()
    return user


if __name__ == '__main__':
    user_service = UserService()
    #user_service.create_user('温饱思淫欲,','aiwe13k4h3qfakf','kflsdjflk')
    #user_service.update_user(111,111,'aiwe13k4h3qfakf')
    #user = user_service.check_user_by_openid('hgdhghgdh', '温饱思淫欲，','kjklfjlka')
    #print user.nick_name

