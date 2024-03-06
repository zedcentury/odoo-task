# -*- coding: utf-8 -*-
# from odoo import http


# class Visa-application-test(http.Controller):
#     @http.route('/visa-application-test/visa-application-test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/visa-application-test/visa-application-test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('visa-application-test.listing', {
#             'root': '/visa-application-test/visa-application-test',
#             'objects': http.request.env['visa-application-test.visa-application-test'].search([]),
#         })

#     @http.route('/visa-application-test/visa-application-test/objects/<model("visa-application-test.visa-application-test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('visa-application-test.object', {
#             'object': obj
#         })

