'use strict';

angular
  .module('nlppln')
  .factory('neService', neService);

neService.$inject = ['$http'];

function neService($http) {
  var service = {
    namedEntities: namedEntities,
    texts: texts,
    overviewNamedEntities: overviewNamedEntities,
    getText: getText
  };

  function namedEntities() {
    var url = '/named_entities';
    return $http.get(url);
  }

  function texts() {
    var url = '/texts';
    return $http.get(url);
  }

  function overviewNamedEntities() {
    var url = '/overview_named_entities';
    return $http.get(url);
  }

  function getText() {
    return $http.get('text');
  }

  return service;
}
