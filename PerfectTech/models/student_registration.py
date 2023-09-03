from odoo import fields, models, api


class StudentRegistration(models.Model):
    _name = 'student.registration'
    _description = 'Student Registration'

    name = fields.Char(string='Registration Number', required=True, readonly=True,
                       default=lambda self: self.env['ir.sequence'].next_by_code('student.registration'))
    student_id = fields.Many2one('res.partner', string='Student', required=True, domain="[('is_student', '=', True)]")
    phone = fields.Char(string='Phone', related='student_id.phone')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    birth_date = fields.Date(string='Date of Birth', related='student_id.birth_date')
    date = fields.Date(string='Registration Date', required=True, default=fields.datetime.today())
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id,
                                  readonly=True)
    amount = fields.Monetary(string='Registration Fees', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('invoiced', 'Invoiced'),
        ('canceled', 'Canceled')],
        string='State', default='draft', required=True)

    @api.depends('birth_date')
    def _compute_age(self):
        today = fields.Date.today()
        for rec in self:
            if rec.birth_date:
                birth_date = rec.birth_date
                age = today.year - birth_date.year - (
                        (today.month, today.day) < (birth_date.month, birth_date.day))
                rec.age = age
            else:
                rec.age = 0

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_cancel(self):
        for rec in self:
            rec.state = 'canceled'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    registration_id = fields.Many2one('student.invoice', string='Invoice', required='True')

    def action_create_invoice(self):
        for rec in self:
            invoice_data = {
                'registration_id': rec.id,
                'date': fields.Date.today(),
                'amount': rec.amount,

            }
            self.env['student.invoice'].create(invoice_data)

    def open_student_invoice(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Student Invoice',
            'res_model': 'student.invoice',
            'res_id': self.registration_id.id,
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'current',
            'context': {
                'default_registration_id': self.id,
            },
        }
