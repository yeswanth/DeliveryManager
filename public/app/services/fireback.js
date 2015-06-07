angular.module('DeliveryApp')
	.factory('Fireback', ['$firebaseObject', function($firebaseObject) {
		var ordersRef = new Firebase("https://delivery-manager.firebaseio.com/orders");
		var deliveryBoysRef = new Firebase("https://delivery-manager.firebaseio.com/deliveryboys");

		var orders = $firebaseObject(ordersRef);
		var deliveryBoys = $firebaseObject(deliveryBoysRef);

		return {
			getOrders: function() {
				return orders;
			},
			getDeliveryBoys: function() {
				return deliveryBoys;
			}
		};
	}]);