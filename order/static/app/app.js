angular.module('DeliveryApp', ['firebase', 'ngMaterial'])
	.config(function($interpolateProvider) {
                  $interpolateProvider.startSymbol('{$');
                  $interpolateProvider.endSymbol('$}');
	});
