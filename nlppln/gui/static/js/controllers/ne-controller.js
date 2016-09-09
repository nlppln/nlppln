'use strict';

angular
  .module('nlppln', ['datatables', 'ngResource'])
  .controller('NEController', function ($scope, neService, DTOptionsBuilder, DTColumnBuilder, $q, $http, $compile) {
    var neCtrl = this;

    neCtrl.numNamedEntities = 0;
    neCtrl.numTexts = 0;
    neCtrl.texts = [];
    neCtrl.neDataTexts = [];

    // Datatable NE Overview
    neCtrl.dtOvOptions = DTOptionsBuilder.fromFnPromise(function() {
      var defer = $q.defer();
        $http.get('/overview_named_entities').then(function(result) {
          neCtrl.numNamedEntities = result.data.nes;
          neCtrl.numTexts = result.data.texts.length;
          neCtrl.texts = result.data.texts;
          defer.resolve(result.data.data);
        });
        return defer.promise;
    })
    .withOption('rowCallback', function(nRow, aData, iDisplayIndex, iDisplayIndexFull) {
      // Unbind first in order to avoid any duplicate handler (see https://github.com/l-lin/angular-datatables/issues/87)
        $('td', nRow).unbind('click');
        $('td', nRow).bind('click', function() {
            $scope.$apply(function() {
              console.log(aData);
              neCtrl.loadText(aData.text);
            });
        });
        return nRow;
    })
    .withPaginationType('full_numbers');
    neCtrl.dtOvColumns = [
      DTColumnBuilder.newColumn('text').withTitle('Text'),
      DTColumnBuilder.newColumn('PER').withTitle('Person'),
      DTColumnBuilder.newColumn('LOC').withTitle('Location'),
      DTColumnBuilder.newColumn('ORG').withTitle('Organization'),
      DTColumnBuilder.newColumn('NE').withTitle('Unspecified'),
      DTColumnBuilder.newColumn('total').withTitle('Total')
    ];

    // Datatable Text Details
    neCtrl.dtTDOptions = DTOptionsBuilder.fromFnPromise(function() {
      var text = 'm1-20160726.txt.out.json';
      var defer = $q.defer();
        $http.get('/named_entities_text/' + text).then(function(result) {
          console.log(result.data.data);
          defer.resolve(result.data.data);

        });
        return defer.promise;
    }).withOption('createdRow', function (row, data) {
      $('td', row).css(neService.neColor({'ne': data.ner}));
      $compile(angular.element(row).contents())($scope);
    })
    .withPaginationType('full_numbers');
    neCtrl.dtTDColumns = [
        DTColumnBuilder.newColumn('ner').withTitle('NE type'),
        DTColumnBuilder.newColumn('word').withTitle('Word(s)'),
        DTColumnBuilder.newColumn('text').withTitle('Frequency')
    ];
    neCtrl.dtTDInstance = {};

    neCtrl.currentText = '';
    neCtrl.sentences = [];
    neCtrl.neDataText = [];

    $scope.$on('sentences', function() {
      neCtrl.sentences = neService.sentences;
    });

    $scope.$on('currentText', function() {
      neCtrl.currentText = neService.currentText;
    });

    $scope.$on('neDataText', function() {
      neCtrl.neDataText = neService.neDataText;
    });

    neCtrl.loadText = function(text) {
      console.log('load text '+text);
      neService.loadText(text);
      neCtrl.dtTDInstance.changeData(neService.namedEntitiesText(text));
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

    //neCtrl.render();
});
