# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductBrand(models.Model):
    _inherit = 'product.template'

    class_id = fields.Many2one('product.class', string='Class', ondelete='restrict')
    sub_class_id = fields.Many2one('product.sub.class', string='Sub-Class', ondelete='restrict')


class ClassProduct(models.Model):
    _name = 'product.class'

    name = fields.Char(String="Name", required=True)
    product_ids = fields.One2many('product.template', 'class_id')
    sub_class_ids = fields.One2many('product.sub.class', 'class_id')
    description = fields.Text(string='Description')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Class name already exists !"),
    ]


class SubClassProduct(models.Model):
    _name = 'product.sub.class'

    name = fields.Char(String="Name", required=True)
    class_id = fields.Many2one('product.class', string='Class', ondelete='restrict')
    product_ids = fields.One2many('product.template', 'sub_class_id')
    description = fields.Text(string='Description')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Sub-Class name already exists !"),
    ]
