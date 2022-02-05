from odoo import fields, models


class HospitalDoctor(models.Model):
    _name = "hms.doctor"
    _description = "Hospital Doctor"

    name = fields.Char()
    firstname = fields.Char(string="First name")
    lastname = fields.Char(string="Last name")
    image = fields.Image(string="Picture")

    patients_ids = fields.Many2many('hms.patient')
