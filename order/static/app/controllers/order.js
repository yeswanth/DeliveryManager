angular.module('DeliveryApp')
	.controller('OrderCtrl', ['$scope', 'Fireback', function($scope, Fireback){
		/*var sampleData = [
			{
				"items": [
					{
						"qty": 6,
						"name": "Christian"
					},
					{
						"qty": 2,
						"name": "Laverne"
					},
					{
						"qty": 8,
						"name": "Joanne"
					}
				],
				"status": "received",
				"area": "Maxwell",
				"lon": 3,
				"lat": 1
			},
			{
				"items": [
					{
						"qty": 1,
						"name": "Lena"
					},
					{
						"qty": 1,
						"name": "Freda"
					},
					{
						"qty": 10,
						"name": "Fanny"
					}
				],
				"status": "waiting",
				"area": "Sondra",
				"lon": 2,
				"lat": 8
			},
			{
				"items": [
					{
						"qty": 3,
						"name": "Fuller"
					},
					{
						"qty": 10,
						"name": "Carole"
					},
					{
						"qty": 10,
						"name": "Louisa"
					},
					{
						"qty": 8,
						"name": "Cook"
					},
					{
						"qty": 4,
						"name": "Kline"
					}
				],
				"status": "waiting",
				"area": "Velasquez",
				"lon": 0,
				"lat": 8
			},
			{
				"items": [
					{
						"qty": 10,
						"name": "Muriel"
					},
					{
						"qty": 5,
						"name": "Vicky"
					},
					{
						"qty": 10,
						"name": "Lott"
					},
					{
						"qty": 9,
						"name": "Sheila"
					}
				],
				"status": "delivered",
				"area": "Eula",
				"lon": 0,
				"lat": 8
			},
			{
				"items": [
					{
						"qty": 4,
						"name": "Anderson"
					},
					{
						"qty": 10,
						"name": "Betty"
					},
					{
						"qty": 6,
						"name": "Munoz"
					},
					{
						"qty": 7,
						"name": "Ware"
					}
				],
				"status": "cooking",
				"area": "Jeanine",
				"lon": 0,
				"lat": 6
			},
			{
				"items": [
					{
						"qty": 4,
						"name": "Hewitt"
					},
					{
						"qty": 3,
						"name": "Valerie"
					}
				],
				"status": "cooking",
				"area": "Holman",
				"lon": 3,
				"lat": 7
			},
			{
				"items": [
					{
						"qty": 10,
						"name": "Lessie"
					},
					{
						"qty": 5,
						"name": "Janell"
					},
					{
						"qty": 5,
						"name": "Valarie"
					},
					{
						"qty": 5,
						"name": "Jessica"
					}
				],
				"status": "waiting",
				"area": "Fitzgerald",
				"lon": 4,
				"lat": 5
			},
			{
				"items": [
					{
						"qty": 3,
						"name": "Shauna"
					}
				],
				"status": "received",
				"area": "Torres",
				"lon": 7,
				"lat": 7
			},
			{
				"items": [
					{
						"qty": 10,
						"name": "Avery"
					},
					{
						"qty": 8,
						"name": "Baird"
					},
					{
						"qty": 6,
						"name": "Gay"
					},
					{
						"qty": 1,
						"name": "Stacy"
					},
					{
						"qty": 4,
						"name": "Brooks"
					}
				],
				"status": "received",
				"area": "Brenda",
				"lon": 3,
				"lat": 0
			},
			{
				"items": [
					{
						"qty": 2,
						"name": "Vazquez"
					},
					{
						"qty": 2,
						"name": "Gibson"
					},
					{
						"qty": 2,
						"name": "Hernandez"
					},
					{
						"qty": 3,
						"name": "Justice"
					},
					{
						"qty": 9,
						"name": "Tami"
					}
				],
				"status": "cooking",
				"area": "Maricela",
				"lon": 2,
				"lat": 2
			}
		];
		$scope.orders = sampleData;*/

		$scope.orders = [];

		$scope.$watchCollection(function() {
			return Fireback.getOrders();
		}, function(newVal, oldVal) {
			if (typeof newVal !== 'undefined') {
				tempOrders = Fireback.getOrders();
				$scope.orders = [];
				angular.forEach(tempOrders, function(value, key) {
					$scope.orders.push(value);
				});
			}
		});
		
	}]);
