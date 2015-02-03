angular.module('todoApp', [])

.controller('TodoController', ['$scope', function ($scope) {
    $scope.todos = [];
    $scope.addTodo = function () {
        $scope.todos.push({text: $scope.todoText, done: false});
        $scope.todoText = '';
    };
    $scope.remaining = function () {
        return _.filter($scope.todos, function (todo) {
            return todo.done === false;
        }).length;
    };
    $scope.archive = function () {
        $scope.todos = _.filter($scope.todos, function (todo) {
            return todo.done === false;
        });
    };
}]);
