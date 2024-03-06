from odoo import models, fields


class MyCourse(models.Model):
    _name = "my_course"
    _description = "Course model"

    name = fields.Char("Name", default="Python for beginners", required=True)
    description = fields.Text("Description")
    price = fields.Integer("Price", default=0)
    # is_active = fields.Boolean("Active", default=False)
