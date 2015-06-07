angular.module('DeliveryApp')
	.filter('orderstring', function() {
		return function(input) {
			var outputString = "";
			if (typeof input !== 'undefined') {
				angular.forEach(input, function(item, index) {
					outputString = outputString.concat(item.quantity, " ", item.name);
					outputString = outputString.concat(", ");
				});
				outputString = outputString.slice(0, - 2);
			}

			return outputString;
		};
	});