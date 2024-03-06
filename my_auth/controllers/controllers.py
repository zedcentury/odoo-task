# -*- coding: utf-8 -*-
from odoo import http


class MyAuth(http.Controller):
    @http.route('/users/auth')
    def index(self, **kw):
        login = kw.get('login')
        password = kw.get('password')

        if not (login and password):
            return 'Invalid username and/or password'

        data = http.request.env['res.users'].sudo().search([('login', '=', login)])

        if bool(data):
            http.request.session.authenticate(http.request.session.db, login, password)
            return http.request.redirect('/')
        else:
            http.request.env['res.users'].sudo().create({
                'name': login,
                'login': login,
                'password': password
            })
            return http.request.redirect(f'/users/auth?login={login}&password={password}')
