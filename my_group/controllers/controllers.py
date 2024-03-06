# -*- coding: utf-8 -*-
# from odoo import http


# class MyGroup(http.Controller):
#     @http.route('/my_group/my_group', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_group/my_group/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_group.listing', {
#             'root': '/my_group/my_group',
#             'objects': http.request.env['my_group.my_group'].search([]),
#         })

#     @http.route('/my_group/my_group/objects/<model("my_group.my_group"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_group.object', {
#             'object': obj
#         })

