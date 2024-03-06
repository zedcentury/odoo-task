# -*- coding: utf-8 -*-
# from odoo import http


# class MyStudent(http.Controller):
#     @http.route('/my_student/my_student', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_student/my_student/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_student.listing', {
#             'root': '/my_student/my_student',
#             'objects': http.request.env['my_student.my_student'].search([]),
#         })

#     @http.route('/my_student/my_student/objects/<model("my_student.my_student"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_student.object', {
#             'object': obj
#         })

