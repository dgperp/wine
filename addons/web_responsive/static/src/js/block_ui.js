/** @odoo-module **/
import { BlockUI } from "@web/core/ui/block_ui";
const { Component, tags, useState } = owl;

BlockUI.template = tags.xml`
    <div t-att-class="state.blockUI ? 'o_blockUI' : ''">
      <t t-if="state.blockUI">
        <div>
            <img style="" src="/web_responsive/static/src/img/runcat.gif" alt="Loading..."/>
        </div>
      </t>
    </div>`;
