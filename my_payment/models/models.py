import datetime

from odoo import models, fields, api


class MyPayment(models.Model):
    _name = 'my_payment'
    _description = 'Payment model'

    student_id = fields.Many2one(comodel_name='my_student', string='Student', required=True)
    course_id = fields.Many2one(comodel_name='my_course', string='Course', required=True)
    price = fields.Integer(string='Price', required=True)
    comment = fields.Text(string='Comment')

    # days_ago = fields.Integer(string='Days ago', compute='_compute_days_ago', store=False)

    def _compute_display_name(self):
        for record in self:
            record.display_name = f'{record.price} so\'m'

    # @api.depends('create_date')
    # def _compute_days_ago(self):
    #     for payment in self:
    #         payment.days_ago = (datetime.datetime.now() - payment.create_date).days
