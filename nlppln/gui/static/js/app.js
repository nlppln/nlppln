'use strict';

var app = angular.module('nlppln', [
  'ngResource',
  'ngRoute',
  'ui.bootstrap',
  'ui.date']);

  app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/named_entities.html',
        controller: 'NEController'})
      .otherwise({redirectTo: '/'});
  }]);
