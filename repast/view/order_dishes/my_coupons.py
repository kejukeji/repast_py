#encoding:utf8
from ...services.do_coupons import DoCoupons
from flask import render_template, request
from ...models.coupons import Coupons
from ...util.session_common import get_session_user
from ...services.user_service import  get_user_by_id




def deal_coupons():
    coupons_id = request.args.get('coupons_id')
    if coupons_id:
        DoCoupons.update_coupons(coupons_id)
        DoCoupons.update_coupons_total(coupons_id)

    arr=DoCoupons.get_coupons()
    for a in arr:
        sale=int(10*a.cou_price/a.price)
        a.sale=sale

    return  render_template('reception/my_coupons.html',
                            arr=arr)

def on_sale():
    all_coupons = Coupons.get_all_coupons()
    user_id = get_session_user()
    user=get_user_by_id(user_id)
    id = []
    if user.coupons_id:
        id=user.coupons_id
        id=id.split(',')
    for a in all_coupons:
        message = "领取"
        if str(a.id) in id:
            message = "已领取"
        a.message = message
        sale= int((10*a.cou_price / a.price))
        a.sale=sale
    return render_template('reception/on_sale.html',
                           all_coupons=all_coupons)

