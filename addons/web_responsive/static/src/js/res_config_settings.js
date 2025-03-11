odoo.define('base.settings.renderer', function (require) {
   "use strict";
   
   var BaseSettingRenderer = require('base.settings').Renderer;

   var Renderer = BaseSettingRenderer.include({
   

    /**
     * @override
     */
    _initModules: function () {
      var self = this;
      this.modules = [];
      _.each(this.$('.app_settings_block'), function (settingView, index) {
          var group = !$(settingView).hasClass('o_invisible_modifier');
          var isNotApp = $(settingView).hasClass('o_not_app');
          if(group && !isNotApp) {
              var data = $(settingView).data();
              data.string = $(settingView).attr('string') || data.string;
              self.modules.push({
                  key: data.key,
                  string: data.string,
               //   imgurl: self._getAppIconUrl(data.string),
                  imgurl: "",
              });
         }  else {
               $(settingView).remove();
            }
         });
   },

      /**
       * @override
       */
      _getAppIconUrl: function (module) {
         return module === "General Settings" ? "/web_responsive/static/src/img/module_icons/Settings.png" : "/web_responsive/static/src/img/module_icons/" + module + ".png";
      },

   })
   
   return {
       Renderer: Renderer,
   };
});
