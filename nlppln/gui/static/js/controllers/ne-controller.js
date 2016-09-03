'use strict';

angular
  .module('nlppln')
  .controller('NEController', function ($scope, neService) {
    var neCtrl = this;

    neCtrl.numNamedEntities = 0;
    neCtrl.numTexts = 0;

    neCtrl.render = function () {
      neService.namedEntities().then(function (data) {
        //console.log(data);

        neCtrl.numNamedEntities = data.data.data.length;

        $('#nerdata').DataTable({
          data: data.data.data,
          columns: [
            { 'data': 'text', 'title': 'Text' },
            { 'data': 'word', 'title': 'Word' },
            { 'data': 'ner', 'title': 'NE Type' }
          ]
        });
      });

      neService.texts().then(function (data) {
        //console.log(data);
        neCtrl.numTexts = data.data.data.length;
      });
    };

    neCtrl.render();
});
