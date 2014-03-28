# coding: UTF-8
from repast.models.database import db

class BaseService(object):
    '''基本增删改查'''
    def create_model(self, model):
        db.add(model)
        db.commit()

    def update_model(self, model, **kwargs):
        try:
            model.update(kwargs)
            db.commit()
        except:
            db.rollback()


    def get_model_by_id(self, id):
        ''''''
