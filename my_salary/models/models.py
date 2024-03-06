from odoo import models, fields


class MySalary(models.Model):
    _name = 'my_salary'
    _description = 'Salary model'

    teacher_id = fields.Many2one(comodel_name='my_teacher', string='Teacher', required=True)
    price = fields.Integer(string='Price')

    def _compute_display_name(self):
        for record in self:
            record.display_name = f'{record.teacher_id.first_name} {record.teacher_id.last_name} - {record.price} so\'m'
