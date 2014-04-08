# coding: UTF-8
import logging
from flask import flash
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.babel import gettext
from wtforms.fields import TextField, FileField, TextAreaField
from repast.util.others import form_to_dict
from repast.models.brand import Brand
from repast.services.common_service import GetName

from repast.models.database import db
from repast.util.others import form_to_dict
from repast.services.brand_service import BrandService

log = logging.getLogger("flask-admin.sqla")

class BrandView(ModelView):
    '''品牌'''
    page_size = 20 # 每页条数
    column_display_pk = True # 显示外键
    can_create = True # 能否创建
    can_edit = True # 能否更改

    #column_display_all_relations = ('id','group_id', True)
    column_searchable_list = ('name','description','group',)
    column_exclude_list = ('group_id','description','email','id')

    create_template = 'admin_page/brand_create.html'
    edit_template = 'admin_page/brand_edit.html'
    list_template = 'admin_page/brand_list.html'

    column_labels = dict(
        name = u'品牌名',
        description = u'介绍',
        manager = u'管理人',
        tel = u'电话',
        email = u'邮箱',
        group = u'集团',
        group_id = u'集团'
    )

    column_descriptions = dict(
        name = u'品牌名称',
        description = u'品牌简单介绍',
        manager = u'负责管理此品牌',
        tel = u'手机号码',
        email = u'电子邮箱',
        group = u'所属集团',
        group_id = u'所属集团'
    )

    def __init__(self, db, **kwargs):
        super(BrandView, self).__init__(Brand, db, **kwargs)

    # 描述字段为文本域
    form_overrides = dict(
        description = TextAreaField
    )

    def scaffold_form(self):
        form_class = super(BrandView, self).scaffold_form()
        delattr(form_class, 'group')
        return form_class

    def create_model(self, form):
        '''添加集团'''
        #try:
        #    form_dict = form_to_dict(form)
        #    group = self._get_brand(form_dict)
        #    self.session.add(group)
        #    self.session.commit()
        #except Exception, ex:
        #    flash(gettext('Failed to create model. %(error)s', error=str(ex)), 'error')
        #    logging.exception('Failed to create model')
        #    self.session.rollback()
        #    return False
        #return True
        form_dict = form_to_dict(form)
        brand = BrandService.insert_brand(self.session, form_dict)
        return brand


    def update_model(self, form, model):
        '''添加集团'''
        try:
            form_dict = form_to_dict(form)
            group_name = GetName._get_group(form_dict)
            form_dict['group'] = group_name
            model.update(**form_dict)
            self.session.commit()
        except Exception, ex:
            flash(gettext('Failed to update model. %(error)s', error=str(ex)), 'error')
            logging.exception('Failed to update model')
            self.session.rollback()
            return False
        return True

    def _get_brand(self, form_dict):
        group_name = GetName._get_group(form_dict)
        return Brand(name=form_dict['name'],
                     description=form_dict['description'],
                     group_id=form_dict['group_id'],
                     group=group_name,
                     manager=form_dict['manager'],
                     tel=form_dict['tel'],
                     email=form_dict['email'])