'use strict';

angular
  .module('nlppln')
  .controller('NEController', function ($scope, neService) {
    var neCtrl = this;

    neCtrl.numNamedEntities = 0;
    neCtrl.numTexts = 0;

    var color = d3.scaleOrdinal(d3.schemeCategory10)
      .domain(['PER', 'LOC', 'ORG', '']);

    $scope.neColor = function(token) {
      if('ne' in token){
        return {'background-color': color(token.ne)};
      }
      return {};
    };

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
            { 'data': 'PER', 'title': 'Person', 'class': 'PER' },
            { 'data': 'LOC', 'title': 'Location', 'class': 'LOC' },
            { 'data': 'ORG', 'title': 'Organization', 'class': 'ORG' },
            { 'data': '', 'title': 'Unspecified', 'class': 'UNSP' },
            { 'data': 'total', 'title': 'Total' }
          ]
        });

        $('#nerdata').find('th.PER').css('background-color', color('PER'));
        $('#nerdata').find('th.LOC').css('background-color', color('LOC'));
        $('#nerdata').find('th.ORG').css('background-color', color('ORG'));
        $('#nerdata').find('th.UNSP').css('background-color', color(''));
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
        //console.log(neCtrl.sentences);
      });

      neService.namedEntitiesText().then(function (data) {
        //console.log(data);
        $('#nertext').DataTable({
          data: data.data.data,
          columns: [
            { 'data': 'ner', 'title': 'NE type' },
            { 'data': 'word', 'title': 'Word(s)' },
            { 'data': 'w_id', 'title': 'Frequency' }
          ],
          fnRowCallback: function (nRow, aData) {
            $(nRow).css('background-color', color(aData.ner));
          }
        });
      });

    };

    neCtrl.render();
});
