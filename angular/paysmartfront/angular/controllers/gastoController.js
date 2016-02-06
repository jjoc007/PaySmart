app.controller('GastoController', ['$scope','$http', 'CONFIG', function($scope,$http,CONFIG) {
        
		$scope.gasto = {};
 
        $scope.update = function() {
			$http({
			  method: 'POST',
			  url: CONFIG.API_REST_PYTHON+'Gasto',
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