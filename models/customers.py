from odoo import models, fields, api
from odoo.exceptions import *

'''
Link patient model with customers model from CRM module
by adding a new field in customers model called "related_patient_id"
and show this field inside Misc group within sales and purchase tab
'''


class HospitalCustomer(models.Model):
    _inherit = "res.partner"

    related_patient_id = fields.One2many(comodel_name='hms.patient', inverse_name="department_id")
    patient_email = fields.Char(related="related_patient_id.email")



    @api.constrains('email')
    def _check_mail(self):
        is_found = self.env['hms.patient'].search([('email', '=', self.email)])
        if is_found:
            raise ValidationError('Email is already used by a patient')

    # Prevent user to delete a customer if related to a patient
    def unlink(self):
        is_found = self.env['hms.patient'].search([('customer_id', '=', self.id)]).id

        if is_found:
            raise UserError('The customer is connected to a patient')
        else:
            return super(HospitalCustomer, self).unlink()
