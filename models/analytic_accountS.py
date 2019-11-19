from odoo import fields, api, models

class SaleOrder(models.Model):
    _inherit='sale.order'

    analytic_account_id = fields.Many2one('account.analytic.account', string="Analytic Account", required=True)
    