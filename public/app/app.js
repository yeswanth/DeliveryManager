angular.module('DeliveryApp', ['firebase', 'ngMaterial'])
	.config(function($mdIconProvider) {
		$mdIconProvider
			.iconSet('MaterialDesignIcons', 'lib/mdi/fonts/materialdesignicons-webfont.svg');
	});