# -*- coding: utf-8 -*-
# from odoo import http


# class MyPayment(http.Controller):
#     @http.route('/my_payment/my_payment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_payment/my_payment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_payment.listing', {
#             'root': '/my_payment/my_payment',
#             'objects': http.request.env['my_payment.my_payment'].search([]),
#         })

#     @http.route('/my_payment/my_payment/objects/<model("my_payment.my_payment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_payment.object', {
#             'object': obj
#         })

