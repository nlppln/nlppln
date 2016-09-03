'use strict';

angular
  .module('nlppln')
  .factory('neService', neService);

neService.$inject = ['$http'];

function neService($http) {
  var service = {
    namedEntities: namedEntities,
    texts: texts
  };

  function namedEntities() {
    var url = '/named_entities';
    return $http.get(url);
  }

  function texts() {
    var url = '/texts';
    return $http.get(url);
  }

  return service;
}
