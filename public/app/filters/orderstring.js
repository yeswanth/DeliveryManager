angular.module('DeliveryApp')
	.filter('orderstring', function() {
		return function(input) {
			var outputString = "";
			input.forEach(function(item, index) {
				outputString = outputString.concat(item.qty, " ", item.name);
				if(index != (input.length - 1))
					outputString = outputString.concat(", ");
			});

			return outputString;
		};
	});