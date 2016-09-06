'use strict';

angular
  .module('nlppln')
  .controller('NEController', function ($scope, neService) {
    var neCtrl = this;

    neCtrl.numNamedEntities = 0;
    neCtrl.numTexts = 0;
    neCtrl.texts = [];

    $scope.loadText = function(text) {
      neService.loadText(text);
      $scope.active = 1;
    };

    neCtrl.render = function () {
      neService.overviewNamedEntities().then(function (data) {
        neCtrl.numNamedEntities = data.data.nes;
        neCtrl.numTexts = data.data.texts.length;
        neCtrl.texts = data.data.texts;

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

        $('#nerdata').find('th.PER').css('background-color', neService.color('PER'));
        $('#nerdata').find('th.LOC').css('background-color', neService.color('LOC'));
        $('#nerdata').find('th.ORG').css('background-color', neService.color('ORG'));
        $('#nerdata').find('th.UNSP').css('background-color', neService.color(''));
      });

    };

    neCtrl.render();
});
