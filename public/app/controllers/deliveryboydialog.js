angular.module('DeliveryApp')
	.controller('DeliveryBoyDialogCtrl', ['$scope', '$mdDialog', 'Fireback', function($scope, $mdDialog, Fireback){
		$scope.deliveryBoys = [];
		$scope.data = {
			selectedBoy: ""
		};

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

		$scope.cancel = function() {
			$mdDialog.cancel();
		};

		$scope.assign = function() {
			$mdDialog.hide($scope.data.selectedBoy);
		};
	}]);