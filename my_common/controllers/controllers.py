# -*- coding: utf-8 -*-
# from odoo import http


# class MyCommon(http.Controller):
#     @http.route('/my_common/my_common', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_common/my_common/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_common.listing', {
#             'root': '/my_common/my_common',
#             'objects': http.request.env['my_common.my_common'].search([]),
#         })

#     @http.route('/my_common/my_common/objects/<model("my_common.my_common"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_common.object', {
#             'object': obj
#         })

