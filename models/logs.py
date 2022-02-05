from odoo import fields, models


class PatientLogs(models.Model):
    _name = "hms.logs"
    _description = "Logs of Patient History"
    _rec_name = "created_by"
    created_by = fields.Char(string="Created By")
    date = fields.Date(string="Last Modified in")
    description = fields.Text(string="Description")
    patient_id = fields.Many2one(comodel_name='hms.patient')
