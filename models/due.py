from odoo import fields, api, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    date_dueS = fields.Date(string="Fecha de vencimiento")