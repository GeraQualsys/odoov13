from odoo import fields, api, models

class Lead(models.Model):
	_inherit = 'crm.lead'


	currencyy_id = fields.Boolean(string="Dolar")

	show_ccu= fields.Boolean(string="show ccu")

	ccurrency_id=fields.char(string="ingreso en dolares")