from odoo import api, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _get_combination_info(self, combination=False, product_id=False, add_qty=1, pricelist=False, parent_combination=False, only_template=False):
        res = super()._get_combination_info(combination, product_id, add_qty, pricelist, parent_combination, only_template)
        website_id = self._context.get('website_id')
        website = self.env['website'].browse(website_id) if website_id else False
        if website:
            res['website_id'] = website
        if res.get('product_id', False):
            product = self.env['product.product'].browse(product_id)
            res['description_ecommerce'] = product.description
            if res.get('website_id') and res['website_id'].warehouse_id:
                res['free_qty_available'] = str(product.with_context(warehouse=res['website_id'].warehouse_id.id).free_qty)
            else:
                res['free_qty_available'] = str(product.free_qty)
        if res.get('product_template_id', False):
            product_template = self.env['product.template'].browse(res['product_template_id'])
            res['product_template_obj'] = product_template
            if res.get('website_id') and res['website_id'].warehouse_id:
                res['free_qty_available'] = str(product_template.with_context(warehouse=res['website_id'].warehouse_id.id).free_qty)
            else:
                res['free_qty_available'] = str(product_template.free_qty)

        return res

    @api.model
    def _search_fetch(self, search_detail, search, limit, order):
        website_id = self._context.get('website_id')
        contexts = dict(self.env.context)
        if website_id:
            website = self.env['website'].browse(website_id)
            warehouse_id = website.warehouse_id.id
            contexts['warehouse'] = warehouse_id

        return super(ProductTemplate, self.with_context(contexts))._search_fetch(search_detail, search, limit, order)
