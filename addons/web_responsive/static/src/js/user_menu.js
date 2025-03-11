/** @odoo-module **/

import { registry } from "@web/core/registry";
import { documentationItem, supportItem, odooAccountItem} from "@web/webclient/user_menu/user_menu_items";

function forceDocumentationItem(env)  {
    return {};
}

function forceSupportItem(env)  {
    return {};
}

function forceOdooAccountItem(env)  {
    return {};
}

registry.category("user_menuitems").add('documentation', forceDocumentationItem, { force: true })
registry.category("user_menuitems").add('support', forceSupportItem, { force: true })
registry.category("user_menuitems").add('odoo_account', forceOdooAccountItem, { force: true })
