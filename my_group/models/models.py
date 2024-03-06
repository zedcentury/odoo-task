from odoo import models, fields, api


class MyGroup(models.Model):
    _name = 'my_group'
    _description = 'Group model'

    name = fields.Char(string='Name', required=True)
    teacher_id = fields.Many2one(comodel_name='my_teacher', string='Teacher')
    course_id = fields.Many2one(comodel_name='my_course', string='Course')
    student_ids = fields.Many2many(comodel_name='my_student', string='Students')

    number_of_students = fields.Integer(string='Number of students', compute='_compute_number_of_students', store=False)

    @api.depends('student_ids')
    def _compute_number_of_students(self):
        for group in self:
            group.number_of_students = len(group.student_ids)
