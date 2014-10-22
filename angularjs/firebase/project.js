angular.module('project', ['ngRoute', 'firebase'])

.value('fbUrl', 'https://dazzling-fire-5075.firebaseio.com/')

.factory('Projects', ['$firebase', 'fbUrl', function ($firebase, fbUrl) {
    return $firebase(new Firebase(fbUrl)).$asArray();
}])

.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/', {
            controller: 'ListController'
            templateUrl: 'views/list.html'
        })
        .when('/edit/:projectId', {
            controller: 'EditController'
            templateUrl: 'views/detail.html'
        })
        .when('/new', {
            controller: 'CreateController'
            templateUrl: 'views/detail.html'
        })
        .otherwise({
            redirectTo: '/'
        });
}])

