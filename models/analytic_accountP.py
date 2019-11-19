from odoo import fields, api, models

class PurchaseOrderLine(models.Model):
	_inherit='purchase.order.line'

	account_analytic_id = fields.Many2one('account.analytic.account', string="Analytic Account", required=True)
	