angular.module('DeliveryApp')
	.factory('Fireback', ['$firebaseObject', function($firebaseArray) {
		var ordersRef = new Firebase("https://delivery-manager.firebaseio.com/orders");
		var deliveryBoysRef = new Firebase("https://delivery-manager.firebaseio.com/deliveryboy");

		var orders = $firebaseArray(ordersRef);
		var deliveryBoys = $firebaseArray(deliveryBoysRef);

		return {
			getOrders: function() {
				return orders;
			},
			getDeliveryBoys: function() {
				return deliveryBoys;
			}
		};
	}]);