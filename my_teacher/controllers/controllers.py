# -*- coding: utf-8 -*-
# from odoo import http


# class MyTeacher(http.Controller):
#     @http.route('/my_teacher/my_teacher', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_teacher/my_teacher/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_teacher.listing', {
#             'root': '/my_teacher/my_teacher',
#             'objects': http.request.env['my_teacher.my_teacher'].search([]),
#         })

#     @http.route('/my_teacher/my_teacher/objects/<model("my_teacher.my_teacher"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_teacher.object', {
#             'object': obj
#         })

