from odoo import fields, models, api


class StudentInvoice(models.Model):
    _name = 'student.invoice'
    _description = 'Student Invoice'

    name = fields.Char(string='Invoice Number', required=True, default='New Invoice')
    registration_id = fields.Many2one('student.registration', string='Registration')
    date = fields.Date(string='Registration Date', required=True, default=fields.datetime.today())
    amount = fields.Monetary(string='Registration Fees', related='registration_id.amount')
    currency_id = fields.Many2one('res.currency', string='Currency', related='registration_id.currency_id',
                                  readonly=True)
