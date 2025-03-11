odoo.define('base_backend.FieldResume', function (require) {
"use strict";

    var FieldProgressBar = require('web.basic_fields').FieldProgressBar;

    FieldProgressBar.include({
        _render_value: function (v) {
            this._super.apply(this, arguments);
            var value = this.value || 0;
            this.$('.o_progress').css('border', '1px solid #393939');
            if (value <= 25) {
                this.$('.o_progressbar_complete').css('background-color', '#dc3545');
            }
            else if (value > 25 && value <= 50) {
                this.$('.o_progressbar_complete').css('background-color', '#F7CD1F');
            }
            else if (value > 50 && value <= 75) {
                this.$('.o_progressbar_complete').css('background-color', 'orange');
            }
            else if (value > 75 && value <= 100) {
                this.$('.o_progressbar_complete').css('background-color', '#28a745');
            }
        }
    })

})
