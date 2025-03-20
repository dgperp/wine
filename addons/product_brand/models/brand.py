# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2021-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################

from odoo import models, fields


class ProductBrand(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one('product.brand', string='Brand', ondelete='restrict')
    brand_name = fields.Char(related='brand_id.name', string='Brand Name')


class BrandProduct(models.Model):
    _name = 'product.brand'

    name = fields.Char(String="Brand Name", required=True)
    brand_image = fields.Binary(attachment=True)
    member_ids = fields.One2many('product.template', 'brand_id')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Brand name already exists !"),
    ]
    # product_count = fields.Char(String='Product Count', compute='get_count_products', store=True)

    # @api.depends('member_ids')
    # def get_count_products(self):
    #     self.product_count = len(self.member_ids)


class BrandReportStock(models.Model):
    _inherit = 'stock.quant'

    brand_id = fields.Many2one(
        related='product_id.brand_id',
        string='Brand', store=True, readonly=True, ondelete='restrict')


class PurchaseBrandPivot(models.Model):
    _inherit = 'purchase.report'

    brand_id = fields.Many2one('product.brand', string='Brand', ondelete='restrict')

    def _select(self):
        res = super(PurchaseBrandPivot, self)._select()
        query = res.split('t.categ_id as category_id,', 1)
        rese = query[0] + 't.categ_id as category_id,t.brand_id as brand_id,' + query[1]
        return rese

    def _group_by(self):
        res = super(PurchaseBrandPivot, self)._group_by()
        query = res.split('t.categ_id,', 1)
        res = query[0] + 't.categ_id,t.brand_id,' + query[1]
        return res


class BrandPivot(models.Model):
    _inherit = 'sale.report'

    brand_id = fields.Many2one('product.brand', string='Brand', ondelete='restrict')

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['brand_id'] = ", t.brand_id as brand_id"
        groupby += ', t.brand_id'
        return super(BrandPivot, self)._query(with_clause, fields, groupby, from_clause)
