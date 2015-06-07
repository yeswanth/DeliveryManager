angular.module('DeliveryApp')
	.controller('OrderCtrl', ['$scope', '$mdDialog', 'Fireback', function($scope, $mdDialog, Fireback){
		$scope.orders = [];

		$scope.$watchCollection(function() {
			return Fireback.getOrders();
		}, function(newVal, oldVal) {
			if (typeof newVal !== 'undefined') {
				tempOrders = Fireback.getOrders();
				$scope.orders = [];
				angular.forEach(tempOrders, function(value, key) {
					value.selectedBoy = '';
					$scope.orders.push(value);
				});
			}
		});
		
		$scope.assignDeliveryBoy = function(order, ev) {
			// $mdDialog.show({})
			// var dialog = $mdDialog.confirm().title("Choose Delivery Boy").content("Ohhh Yeahhhhh").ok("Assign").cancel("Nope").targetEvent(ev);
			$mdDialog.show({
				controller: 'DeliveryBoyDialogCtrl',
				templateUrl: 'app/templates/deliveryboydialog.html',
				targetEvent: ev
			}).then(function(selectedBoy) {
				order.selectedBoy = selectedBoy;
			});
		};
	}]);