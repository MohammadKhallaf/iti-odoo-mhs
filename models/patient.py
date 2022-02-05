import re
from datetime import date, datetime

from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError

''' Patients' table
field names:
     name           | ID
     firstname      |
     lastname       |
     birthdate      |
     age            |
     email          | Unique & valid
     gender         |
     history        |
     cr_ratio       |
     blood_type     |
     pcr            |
     image          |
     address        |
     department_id  |
     doctors_ids    |
     department_cap |
     state          |
'''


class HospitalPatient(models.Model):
    _name = "hms.patient"
    _description = "Hospital Patient"

    name = fields.Char()
    firstname = fields.Char(string="First name")
    lastname = fields.Char(string="Last name")
    birthdate = fields.Date(string="Date of birth")
    age = fields.Integer(string="Age", compute='_compute_age', store=True)

    @api.depends('birthdate')
    def _compute_age(self):
        if self.birthdate:
            for item in self:
                if item.birthdate > date.today():
                    raise UserError("Birthdate Incorrect!")
                item.age = date.today().year - item.birthdate.year
                if item.age > 30:
                    item.pcr = True

    # valid and unique
    email = fields.Char(string="Email")

    _sql_constraints = [('email_id', 'UNIQUE(email)', "Email must be unique")]

    @api.constrains('email')
    def _check_email(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if not match:
                raise ValidationError('Not a valid email')

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Gender")
    history = fields.Html(string="History")
    cr_ratio = fields.Float(string="CR ratio")
    blood_type = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('o', 'O'),
    ], string="Blood Type")
    pcr = fields.Boolean()
    image = fields.Image(string="Picture")
    address = fields.Text(string="Address")

    department_id = fields.Many2one(comodel_name='hms.department')
    customer_id = fields.Many2one(comodel_name='res.partner')  # to link it to the customer model
    doctors_ids = fields.Many2many("hms.doctor")
    department_cap = fields.Integer(string="Department Capacity", related="department_id.capacity")
    log_ids = fields.One2many(comodel_name='hms.logs', inverse_name="patient_id")

    state = fields.Selection([
        ('other', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),

    ], default='other')

    #
    # @api.onchange('birthdate')
    # def _onchange_birthdate(self):
    #     # if a birthday is entered => check if it is a valid one
    #     if self.birthdate:
    #         if self.birthdate > date.today():
    #             raise UserError("Birthdate Incorrect!")
    #         self.age = date.today().year - self.birthdate.year
    #         if self.age > 30:
    #             self.pcr = True

    def other_state(self):
        self.state = 'other'
        self.create_log()

    def good_state(self):
        self.state = 'good'
        self.create_log()

    def fair_state(self):
        self.state = 'fair'
        self.create_log()

    def serious_state(self):
        self.state = 'serious'
        self.create_log()

    # @api.onchange('state') #=> not working
    def create_log(self):
        if self.state:
            log = {
                'patient_id': self.id,
                'created_by': self.env.user.display_name,
                'date': datetime.now(),
                'description': self.state,
            }
            self.env['hms.logs'].create(log)
