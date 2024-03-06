# -*- coding: utf-8 -*-
# from odoo import http


# class MySalary(http.Controller):
#     @http.route('/my_salary/my_salary', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_salary/my_salary/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_salary.listing', {
#             'root': '/my_salary/my_salary',
#             'objects': http.request.env['my_salary.my_salary'].search([]),
#         })

#     @http.route('/my_salary/my_salary/objects/<model("my_salary.my_salary"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_salary.object', {
#             'object': obj
#         })

