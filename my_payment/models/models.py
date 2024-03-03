from odoo import models, fields


class MyPayment(models.Model):
    _name = 'my_payment'
    _description = 'Payment model'

    student = fields.Many2one(string='Student', comodel_name='my_student', required=True)
    price = fields.Integer(string='Price', required=True)
    comment = fields.Text(string='Comment')
