angular.module('project', ['ngRoute', 'firebase'])

.value('fbUrl', 'https://dazzling-fire-5075.firebaseio.com/')

.factory('Projects', ['$firebase', 'fbUrl', function ($firebase, fbUrl) {
    return $firebase(new Firebase(fbUrl)).$asArray();
}])

.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/', {
            controller: 'ListController',
            templateUrl: 'views/list.html'
        })
        .when('/edit/:projectId', {
            controller: 'EditController',
            templateUrl: 'views/detail.html'
        })
        .when('/new', {
            controller: 'CreateController',
            templateUrl: 'views/detail.html'
        })
        .otherwise({
            redirectTo: '/'
        });
}])

.controller('ListController', [
    '$scope', 'Projects',
    function ($scope, Projects) {
        $scope.projects = Projects;
}])

.controller('CreateController', [
    '$scope', '$location', '$timeout', 'Projects',
    function ($scope, $location, $timeout, Projects) {
        Projects.$add($scope.project).then(function (data) {
            $location.path('/');
        });
}])

.controller('EditController', [
    '$scope', '$location', '$routeParams', 'Projects',
    function ($scope, $location, $routeParams, Projects) {
        var projectId = $routeParams.projectId;

        $scope.projects = Projects;
        projectIndex = $scope.projects.$indexFor(projectId);

        $scope.project = $scope.projects[projectIndex];

        $scope.destroy = function() {
            $scope.projects.$remove($scope.project).then(function(data) {
                $location.path('/');
            });
        };

        $scope.save = function() {
            $scope.projects.$save($scope.project).then(function(data) {
               $location.path('/');
            });
        };
}]);
