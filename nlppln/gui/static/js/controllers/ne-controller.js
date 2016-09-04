'use strict';

angular
  .module('nlppln')
  .controller('NEController', function ($scope, neService) {
    var neCtrl = this;

    neCtrl.numNamedEntities = 0;
    neCtrl.numTexts = 0;

    neCtrl.sentences = [];

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

      // Get text + ner info to display
      neService.getText().then(function (data) {
        //console.log(data);
        neCtrl.sentences = d3.nest()
          .key(function(d) { return d.sentence; })
          .entries(data.data.data);
        console.log(neCtrl.sentences);
      });

    };

    neCtrl.render();
});
