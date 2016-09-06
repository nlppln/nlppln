'use strict';

angular
  .module('nlppln')
  .controller('NEController', function ($scope, neService, DTOptionsBuilder, DTColumnDefBuilder) {
    var neCtrl = this;

    neCtrl.numNamedEntities = 0;
    neCtrl.numTexts = 0;
    neCtrl.texts = [];
    neCtrl.neDataTexts = [];

    $scope.loadText = function(text) {
      neService.loadText(text);
      $scope.active = 1;
    };

    $scope.neColor = function(token) {
      return neService.neColor(token);
    };

    neCtrl.render = function () {
      neService.overviewNamedEntities().then(function (data) {
        neCtrl.numNamedEntities = data.data.nes;
        neCtrl.numTexts = data.data.texts.length;
        neCtrl.texts = data.data.texts;
        neCtrl.neDataTexts = data.data.data;
      });
    };

    neCtrl.render();
});
