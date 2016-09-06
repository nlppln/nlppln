'use strict';

angular
  .module('nlppln')
  .controller('NETextController', function ($scope, neService) {
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
