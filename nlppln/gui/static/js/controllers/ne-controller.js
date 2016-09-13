'use strict';

angular
  .module('nlppln', ['datatables', 'ngResource'])
  .controller('NEController', function ($scope, neService, DTOptionsBuilder, DTColumnBuilder, $q, $http, $compile) {
    var neCtrl = this;

    // Datatable texts Overview
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

    // Other variables texts overview
    neCtrl.numNamedEntities = 0;
    neCtrl.numTexts = 0;
    neCtrl.texts = [];

    // Datatable Text Details
    neCtrl.dtTDOptions = DTOptionsBuilder.fromFnPromise(function() {
      // start with empty text details table (no text is selected)
      return $q.resolve([]);
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

    // Other variables used to display text details
    neCtrl.currentText = '';
    neCtrl.sentences = [];

    neCtrl.loadText = function(text) {
      console.log('load text '+text);
      neService.loadText(text);
      neCtrl.dtTDInstance.changeData(neService.namedEntitiesText(text));
      $scope.selectTab('text');
    };

    // Datatable NE Overview
    neCtrl.dtNeOptions = DTOptionsBuilder.fromFnPromise(function() {
      return neService.namedEntitiesAggr();
    }).withOption('createdRow', function (row, data) {
      $('td', row).css(neService.neColor({'ne': data.ner}));
      $compile(angular.element(row).contents())($scope);
    })
    .withPaginationType('full_numbers');
    neCtrl.dtNeColumns = [
      DTColumnBuilder.newColumn('ner').withTitle('NE type'),
      DTColumnBuilder.newColumn('word').withTitle('Word(s)'),
      DTColumnBuilder.newColumn('count').withTitle('Frequency'),
      DTColumnBuilder.newColumn('text_count').withTitle('# Texts')
    ];

    $scope.neColor = function(token) {
      return neService.neColor(token);
    };

    $scope.$on('sentences', function() {
      neCtrl.sentences = neService.sentences;
    });

    $scope.$on('currentText', function() {
      neCtrl.currentText = neService.currentText;
    });

    $scope.selectedTab = 'texts';

    $scope.selectTab = function(name){
      console.log('selecting tab ' + name);
      $scope.selectedTab = name;
    };

});
