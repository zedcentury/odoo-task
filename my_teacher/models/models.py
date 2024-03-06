from odoo import models, fields, api


class MyTeacher(models.Model):
    _name = 'my_teacher'
    _description = 'Teacher model'

    first_name = fields.Char(string='First name', required=True)
    last_name = fields.Char(string='Last name', required=True)
    age = fields.Integer(string='Age')
    phone_number = fields.Char(string='Phone number')
    address = fields.Text(string='Address')

    name = fields.Char(string='Name', compute='_compute_name', store=False)
    full_name = fields.Char(string='Full Name', compute='_compute_full_name', store=False)

    def _compute_display_name(self):
        for record in self:
            record.display_name = f'{record.first_name} {record.last_name}'

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for student in self:
            student.name = "%s %s" % (student.first_name, student.last_name)

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for student in self:
            student.full_name = "%s %s" % (student.first_name, student.last_name)
