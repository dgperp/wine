from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    theme_color_brand = fields.Char(
        string='Theme Brand Color'
    )

    theme_color_font_brand = fields.Char(
        string='Theme Brand Font Color'
    )

    theme_color_primary = fields.Char(
        string='Theme Primary Color'
    )

    theme_color_font_primary = fields.Char(
        string='Theme Primary Font Color'
    )

    def _set_value_theme_color(self):
        variables = [
            'o-brand-odoo',
            'o-brand-primary',
            'o-brand-odoo-font',
            'o-brand-primary-font',
        ]
        colors = self.env['web_editor.assets'].get_variables_values(
            '/web_responsive/static/src/scss/primary_variables.scss', 'web._assets_primary_variables', variables
        )
        colors_changed = []
        colors_changed.append(self.theme_color_brand != colors['o-brand-odoo'])
        colors_changed.append(self.theme_color_primary != colors['o-brand-primary'])
        colors_changed.append(self.theme_color_font_brand != colors['o-brand-odoo-font'])
        colors_changed.append(self.theme_color_font_primary != colors['o-brand-primary-font'])

        if (any(colors_changed)):
            variables = [
                {'name': 'o-brand-odoo', 'value': self.theme_color_brand or "#b3e0fd"},
                {'name': 'o-brand-odoo-font', 'value': self.theme_color_font_brand or "#000000"},
                {'name': 'o-brand-primary', 'value': self.theme_color_primary or "#0091B9"},
                {'name': 'o-brand-primary-font', 'value': self.theme_color_font_primary or "#243742"},
            ]
            self.env['web_editor.assets'].replace_variables_values(
                '/web_responsive/static/src/scss/primary_variables.scss', 'web._assets_primary_variables', variables
            )

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self._set_value_theme_color()
        return res

    def _get_value_theme_color(self, vals):
        variables = [
            'o-brand-odoo',
            'o-brand-primary',
            'o-brand-odoo-font',
            'o-brand-primary-font',
        ]
        colors = self.env['web_editor.assets'].get_variables_values(
            '/web_responsive/static/src/scss/primary_variables.scss', 'web._assets_primary_variables', variables
        )
        vals.update({
            'theme_color_brand': colors['o-brand-odoo'],
            'theme_color_primary': colors['o-brand-primary'],
            'theme_color_font_brand': colors['o-brand-odoo-font'],
            'theme_color_font_primary': colors['o-brand-primary-font'],
        })
        return vals

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        self._get_value_theme_color(res)
        return res
