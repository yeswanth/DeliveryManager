angular.module('DeliveryApp')
	.filter('orderstring', function() {
		return function(input) {
			if(input == "received")
			return ;
		};
	});