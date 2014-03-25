# coding: UTF-8
import logging
import os
import Image
from flask.ext.admin.contrib.sqla import ModelView
from flask import request, flash, redirect, url_for
from flask.ext import login
from flask.ext.admin.babel import gettext
from flask.ext.admin.base import expose
from flask.ext.admin.model.helpers import get_mdict_item_or_list
from flask.ext.admin.helpers import validate_form_on_submit
from flask.ext.admin.form import get_form_opts
from wtforms.fields import TextField, FileField, TextAreaField
from wtforms import validators
from werkzeug import secure_filename

from repast.models.group import Group
from repast.models.database import db
from repast.util.others import form_to_dict

log = logging.getLogger("flask-admin.sqla")

class GroupView(ModelView):
    '''集团'''
    page_size = 20 # 每页显示条数
    can_create = True # 能否创建
    can_edit = True # 能否修改

    column_searchable_list = ('name',)
    column_exclude_list = ('email','description',) # 过滤列名
    # 后台列表显示列名，以及修改，新增
    column_labels = dict(
        id = u'ID',
        name = u'集团名',
        description = u'介绍',
        address = u'地址',
        group_person_in_charge = u'负责人',
        tel = u'电话'
    )
    # 列名的描述
    column_descriptions = dict(
        id = u'唯一标识',
        name = u'集团名',
        description = u'集团简单介绍',
        address = u'集团地址',
        group_person_in_charge = u'负责人',
        tel = u'手机号码'
    )

    create_template = 'admin_page/group_create.html'
    edit_template = 'admin_page/group_edit.html'
    # 新增修改，描述为文本域
    form_overrides = dict(
        description = TextAreaField
    )

    def scaffold_form(self):
        form_class = super(GroupView, self).scaffold_form()
        delattr(form_class, 'email')
        return form_class

    def create_model(self, form):
        '''添加集团'''
        try:
            form_dict = form_to_dict(form)
            group = self._get_group(form_dict)
            self.session.add(group)
            self.session.commit()
        except Exception, ex:
            flash(gettext('Failed to create model. %(error)s', error=str(ex)), 'error')
            logging.exception('Failed to create model')
            self.session.rollback()
            return False
        return True

    def update_model(self, form, model):
        '''添加集团'''
        try:
            form_dict = form_to_dict(form)
            model.update(**form_dict)
            self.session.commit()
        except Exception, ex:
            flash(gettext('Failed to update model. %(error)s', error=str(ex)), 'error')
            logging.exception('Failed to update model')
            self.session.rollback()
            return False
        return True

    def __init__(self, db, **kwargs):
        super(GroupView, self).__init__(Group, db, **kwargs)

    def _get_group(self, form_dict):
        return Group(name=form_dict['name'],
                     description=form_dict['description'],
                     address=form_dict['address'],
                     group_person_in_charge=form_dict['group_person_in_charge'],
                     tel=form_dict['tel'])