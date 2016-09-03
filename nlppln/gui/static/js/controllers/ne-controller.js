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
      });

      neService.overviewNamedEntities().then(function (data) {
        $('#nerdata').DataTable({
          data: data.data.data,
          columns: [
            { 'data': 'text', 'title': 'Text' },
            { 'data': 'PER', 'title': 'Person' },
            { 'data': 'LOC', 'title': 'Location' },
            { 'data': 'ORG', 'title': 'Organization' },
            { 'data': 'NE', 'title': 'Unspecified' }
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
