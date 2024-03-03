from odoo import models, fields, api


class MyGroup(models.Model):
    _name = 'my_group'
    _description = 'Group model'

    name = fields.Char(string='Name', required=True)
    teacher = fields.Many2one(string='Teacher', comodel_name='my_teacher')
    course = fields.Many2one(string='Course', comodel_name='my_course')
    students = fields.Many2many(string='Students', comodel_name='my_student')
