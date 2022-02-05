from odoo import fields, models


class HospitalDepartment(models.Model):
    _name = "hms.department"
    _description = "Hospital Department"

    name = fields.Char(string="Dep. Name")
    capacity = fields.Integer(string="Capacity")
    is_opened = fields.Boolean('Is Opened', default=True)

    patients_ids = fields.One2many(comodel_name='hms.patient', inverse_name="customer_id")
