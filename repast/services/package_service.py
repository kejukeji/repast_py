# coding: utf-8
from .base_service import BaseService

class PackageService(BaseService):
    """
    param:
         session: 事物session
         form_dict: 表单提交数据
         Object: 实体
         args: 实体所有属性（列）
         args2: 需要特殊处理属性
    """
    def create_package(self, session, form_dict, Object, args, args2):
        return self.create_model(session, form_dict, Object, args, args2)

    def update_package(self, session, form_dict, model, args, special_args=None):
        return self.update_model(session, form_dict, model, args, special_args)
