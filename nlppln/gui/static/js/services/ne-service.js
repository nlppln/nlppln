'use strict';

angular
  .module('nlppln')
  .factory('neService', neService);

neService.$inject = ['$rootScope', '$http'];

function neService($rootScope, $http) {
  var service = {
    namedEntities: namedEntities,
    texts: texts,
    overviewNamedEntities: overviewNamedEntities,
    getText: getText,
    namedEntitiesText: namedEntitiesText,
    loadText: loadText,
    neColor: neColor,
    currentText: null,
    sentences: [],
    neDataText: [],
    color: d3.scaleOrdinal(d3.schemeCategory10).domain(['PER', 'LOC', 'ORG', ''])
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

  function getText(text) {
    return $http.get('/text/' + text);
  }

  function namedEntitiesText(text) {
    return $http.get('/named_entities_text/' + text);
  }

  function loadText(text) {
    service.currentText = text;
    $rootScope.$broadcast('currentText');

    // Get text + ner info to display
    getText(text).then(function (data) {
      //console.log(data);
      service.sentences = d3.nest()
        .key(function(d) { return d.sentence; })
        .entries(data.data.data);
      $rootScope.$broadcast('sentences');
    });

    namedEntitiesText(text).then(function (data) {
      //console.log(data);
      service.neDataText = data.data.data;
      $rootScope.$broadcast('neDataText');
    });
  }

  function neColor(token) {
    if('ne' in token){
      var type = token.ne;
      if(type==='NE'){
        type = '';
      }
      return {'background-color': service.color(type)};
    }
    return {};
  }

  return service;
}
