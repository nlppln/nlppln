'use strict';

angular
  .module('nlppln', ['datatables'])
  .controller('NETextController', function ($scope, neService, DTOptionsBuilder, DTColumnDefBuilder) {
    var ctrl = this;

    ctrl.currentText = '';
    ctrl.sentences = [];
    ctrl.neDataText = [];

    $scope.$on('sentences', function() {
      ctrl.sentences = neService.sentences;
    });

    $scope.$on('currentText', function() {
      ctrl.currentText = neService.currentText;
    });

    $scope.$on('neDataText', function() {
      ctrl.neDataText = neService.neDataText;
    });

  });
