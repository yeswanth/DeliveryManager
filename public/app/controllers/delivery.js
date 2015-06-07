angular.module('DeliveryApp')
	.controller('DeliveryBoysCtrl', ['$scope', 'Fireback', function($scope, Fireback){
		$scope.deliveryBoys = [];

		$scope.$watchCollection(function() {
			return Fireback.getDeliveryBoys();
		}, function(newVal, oldVal) {
			if (typeof newVal !== 'undefined') {
				tempOrders = Fireback.getDeliveryBoys();
				$scope.deliveryBoys = [];
				angular.forEach(tempOrders, function(value, key) {
					$scope.deliveryBoys.push(value);
				});
			}
		});
	}]);