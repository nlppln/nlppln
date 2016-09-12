'use strict';

angular
  .module('nlppln', [])
  .controller('TabController', function ($scope) {
    var ctrl = this;

    $scope.selectedTab = 'texts';

    $scope.selectTab = function(name){
      console.log('selecting tab ' + name);
      $scope.selectedTab = name;
    };

});
