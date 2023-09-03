from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Partners(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean(string='Is Student')
    birth_date = fields.Date(string='Birth Date', required=True)

    @api.constrains('birth_date')
    def _check_age_constraint(self):
        for partner in self:
            if partner.birth_date:
                today = fields.Date.today()
                age = today.year - partner.birth_date.year - (
                        (today.month, today.day) < (partner.birth_date.month, partner.birth_date.day))
                if age < 4 or age > 5:
                    raise ValidationError("Age should be between 4 and 5 years old at today.")
