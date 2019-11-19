from odoo import fields, api, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    date_valid = fields.Date(string="Fecha de validez")