# -*- coding: utf-8 -*-
import datetime
import logging

from odoo import http
from odoo.http import request

logger = logging.getLogger(__name__)


class DashboardController(http.Controller):
    @http.route('/statistics', type='json', auth='user')
    def get_statistics(self, **kwargs):
        period = kwargs.get('params').get('period')
        if bool(period):
            domain = [('create_date', '>=', datetime.datetime.now() - datetime.timedelta(days=int(period)))]
        else:
            domain = []
        fields = ['price:sum']

        # Kirimni hisoblash
        payment_data = request.env['my_payment'].read_group(domain, fields, [])
        sum_payment_price = payment_data[0]['price'] if payment_data else 0

        # Chiqimni hisoblash
        salary_data = request.env['my_salary'].read_group(domain, fields, [])
        sum_salary_price = salary_data[0]['price'] if salary_data else 0

        return {
            'kirim': sum_payment_price,
            'chiqim': sum_salary_price,
        }
