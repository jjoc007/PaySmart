var app = angular.module('tienda', [])

.config(['$httpProvider', function($httpProvider) {
       
$httpProvider.defaults.withCredentials = true;
$httpProvider.defaults.useXDomain = true;
        delete $httpProvider.defaults.headers.common['X-Requested-With'];
    }
])

.controller('AppCtl', ['$scope','$http', function($scope,$http) {
        
		
		$scope.gasto = {};
 
        $scope.update = function() {
			$http({
			  method: 'POST',
			  url: 'http://localhost:5000/Gasto',
			  data: {gasto:$scope.gasto},
			  withCredentials: false, 
			  
			  headers: { 
        'Access-Control-Allow-Methods' : ['OPTIONS', 'GET', 'POST'],
        'Access-Control-Allow-Credentials' : 'true',
        'Access-Control-Allow-Headers' : 'Content-Type',
        'Access-Control-Allow-Origin': '*'}
			}).then(function(data) {
				//First function handles success
				//$scope.content = response.data;
				console.log(data);
			}, function(data) {
				//Second function handles error
				//$scope.content = "Something went wrong";
				console.log(data);
			});
          console.log($scope.gasto);
        };
 
        $scope.reset = function() {
          $scope.gasto = {};
        };
 
        $scope.reset();
      }]);
