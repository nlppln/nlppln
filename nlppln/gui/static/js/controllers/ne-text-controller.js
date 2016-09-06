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

    $scope.neColor = function(token) {
      if('ne' in token){
        return {'background-color': neService.color(token.ne)};
      }
      return {};
    };

    ctrl.render = function () {
      $('#nertext').DataTable({
        data: ctrl.neDataText,
        columns: [
          { 'data': 'ner', 'title': 'NE type' },
          { 'data': 'word', 'title': 'Word(s)' },
          { 'data': 'w_id', 'title': 'Frequency' }
        ],
        fnRowCallback: function (nRow, aData) {
          $(nRow).css('background-color', neService.color(aData.ner));
        }
      });

    };

    ctrl.render();
  });
