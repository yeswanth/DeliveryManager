angular.module('DeliveryApp')
	.factory('Fireback', ['$firebaseObject','$mdToast' , function($firebaseArray, $mdToast) {
		var ordersRef = new Firebase("https://delivery-manager.firebaseio.com/orders");
		var deliveryBoysRef = new Firebase("https://delivery-manager.firebaseio.com/deliveryboy");

		var orders = $firebaseArray(ordersRef);
		var deliveryBoys = $firebaseArray(deliveryBoysRef);

		orders.$watch(function(event) {
			$mdToast.show(
				$mdToast.simple()
					.content('New Order!')
					.position("top right")
					.hideDelay(3000)
			);
		});

		return {
			getOrders: function() {
				return orders;
			},
			getDeliveryBoys: function() {
				return deliveryBoys;
			}
		};
	}]);