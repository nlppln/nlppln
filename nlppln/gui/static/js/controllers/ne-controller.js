'use strict';

angular
  .module('nlppln', ['datatables'])
  .controller('NEController', function ($scope, neService, DTOptionsBuilder, DTColumnDefBuilder) {
    var neCtrl = this;

    neCtrl.numNamedEntities = 0;
    neCtrl.numTexts = 0;
    neCtrl.texts = [];
    neCtrl.neDataTexts = [];

    neCtrl.dtOptions = DTOptionsBuilder.newOptions().withPaginationType('full_numbers');
    neCtrl.dtColumnDefs = [
        DTColumnDefBuilder.newColumnDef('text'),
        DTColumnDefBuilder.newColumnDef('PER'),
        DTColumnDefBuilder.newColumnDef('LOC'),
        DTColumnDefBuilder.newColumnDef('ORG'),
        DTColumnDefBuilder.newColumnDef('NE'),
        DTColumnDefBuilder.newColumnDef('total')
    ];

    console.log(neCtrl.dtOptions);
    console.log(neCtrl.dtColumnDefs);

    $scope.loadText = function(text) {
      neService.loadText(text);
      //$scope.active = 1;
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
