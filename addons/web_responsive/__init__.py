# -*- coding: utf-8 -*-
import base64

from odoo import api, SUPERUSER_ID
from odoo.modules.module import get_module_resource

from . import models


def icons_post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    menu_items = env['ir.ui.menu'].with_context(lang='en_US').search([('parent_id', '=', False)])

    for menu in menu_items:
        img_path = get_module_resource('web_responsive', 'static', 'src', 'img', 'module_icons', f'{menu.name}.png')
        print(img_path)
        if img_path:
            menu.write({'web_icon_data': base64.b64encode(open(img_path, "rb").read())})
