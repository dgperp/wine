from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    description_ecommerce = fields.Text(
        'Ecommerce Description', translate=True,
        help="A description of the Ecommerce Product that you want to communicate to your customers. ")
