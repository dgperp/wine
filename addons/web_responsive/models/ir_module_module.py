import base64

from odoo import models
from odoo.addons.base.models.ir_module import assert_log_admin_access
from odoo.modules.module import get_module_resource


class Module(models.Model):
    _inherit = "ir.module.module"

    def icon_change(self):
        menu_items = self.env['ir.ui.menu'].with_context(lang='en_US').search([('parent_id', '=', False)])

        for menu in menu_items:
            img_path = get_module_resource('web_responsive', 'static', 'src', 'img', 'module_icons', f'{menu.name}.png')

            if img_path:
                menu.write({'web_icon_data': base64.b64encode(open(img_path, "rb").read())})

            module = self.env['ir.module.module'].with_context(lang='en_US').search([('shortdesc', '=', menu.name)])
            if module:
                module.write({'icon': f"/web_responsive/static/src/img/module_icons/{menu.name}.png"})

    @assert_log_admin_access
    def button_immediate_upgrade(self):
        result = super(Module, self).button_immediate_upgrade()
        self.icon_change()
        return result

    @assert_log_admin_access
    def button_immediate_install(self):
        result = super(Module, self).button_immediate_install()
        self.icon_change()
        return result

    @assert_log_admin_access
    def button_immediate_uninstall(self):
        result = super(Module, self).button_immediate_uninstall()
        self.icon_change()
        return result
