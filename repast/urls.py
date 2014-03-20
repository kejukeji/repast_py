# coding: UTF-8
from . import app
from flask.ext.admin import Admin
from flask.ext import restful
from .weixin.verify import weixin
from .view.repast import to_repast_by_stores_id
from .view.admin.group import GroupView
from .models.database import db
from .view.admin.index import HomeView
from .view.admin.brand import BrandView
from restfuls.return_group import GetGroup

# 用户管理路径
# app.add_url_rule('url','method_name', method_name, method=('GET','POST'))
app.add_url_rule('/weixin', 'weixin', weixin, methods=('GET','POST'))
app.add_url_rule('/repast/<int:stores_id>', 'repast', to_repast_by_stores_id, methods=('GET','POST'))


# 接口定义
api = restful.Api(app)
api.add_resource(GetGroup, '/restful/group')


# 后台管理路径
admin = Admin(name=u'Home', index_view=HomeView())
admin.init_app(app)

admin.add_view(GroupView(db, name=u'集团', endpoint='group', category=u'管理'))
admin.add_view(BrandView(db, name=u'品牌', endpoint='brand', category=u'管理'))