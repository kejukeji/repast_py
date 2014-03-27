# coding: UTF-8
from . import app
from flask.ext.admin import Admin
from flask.ext import restful
from .weixin.verify import weixin
from .view.repasts import to_repast_by_stores_id
from .view.admin.group import GroupView
from .models.database import db
from .view.admin.index import HomeView
from .view.admin.brand import BrandView
from restfuls.return_group import *
from .view.admin.stores import StoresView
from .view.admin.queue_setting import QueueSettingView
from .view.admin.admin_login import *
from .view.repasts import *

# 用户管理路径
# app.add_url_rule('url','method_name', method_name, method=('GET','POST'))
app.add_url_rule('/weixin', 'weixin', weixin, methods=('GET','POST'))
app.add_url_rule('/repast/<int:stores_id>', 'repast', to_repast_by_stores_id, methods=('GET','POST'))
app.add_url_rule('/login', 'login_view', login_view, methods=('GET', 'POST'))
app.add_url_rule('/register','login_register', register_view, methods=('GET','POST'))
app.add_url_rule('/call_number','to_call_number', to_call_number, methods=('GET','POST'))
app.add_url_rule('/home','to_home', to_home, methods=('GET','POST'))
app.add_url_rule('/home_page','to_home_page', to_home_page, methods=('GET','POST'))
app.add_url_rule('/login','to_login', to_login, methods=('GET','POST'))
app.add_url_rule('/my_page','to_my_page', to_my_page, methods=('GET','POST'))
app.add_url_rule('/order_dishes','to_order_dishes', to_order_dishes, methods=('GET','POST'))
app.add_url_rule('/my_queue','to_my_queue', to_my_queue, methods=('GET','POST'))
app.add_url_rule('/queue','to_queue', to_queue, methods=('GET','POST'))
app.add_url_rule('/search','to_search', to_search, methods=('GET','POST'))
app.add_url_rule('/search_result','to_search_result', to_search_result, methods=('GET','POST'))


# 接口定义
api = restful.Api(app)
api.add_resource(GetGroup, '/restful/group')
api.add_resource(GetBrand, '/restful/brand/<int:group_id>')
api.add_resource(GetProvince, '/restful/province')
api.add_resource(GetCity, '/restful/city/<int:province_id>')
api.add_resource(GetCounty, '/restful/county/<int:city_id>')
api.add_resource(GetStores, '/restful/stores/<int:brand_id>')


# 后台管理路径
admin = Admin(name=u'Home', index_view=HomeView())
admin.init_app(app)

admin.add_view(GroupView(db, name=u'集团', endpoint='group', category=u'管理'))
admin.add_view(BrandView(db, name=u'品牌', endpoint='brand', category=u'管理'))
admin.add_view(StoresView(db, name=u'餐厅', endpoint='stores', category=u'管理'))
admin.add_view(QueueSettingView(db, name=u'桌型维护', endpoint='queue'))