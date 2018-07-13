test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.color
          'No color yet. You need to paint me.'
          >>> hilfingers_car.paint('black')
          'Tesla Model S is now black'
          >>> hilfingers_car.color
          'black'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_truck = MonsterTruck('Monster Truck', 'XXL')
          >>> hilfingers_car.size
          'Tiny'
          >>> hilfingers_truck.size
          'Monster'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.model
          'Model S'
          >>> hilfingers_car.gas = 10
          >>> hilfingers_car.drive()
          'Tesla Model S goes vroom!'
          >>> hilfingers_car.drive()
          'Tesla Model S cannot drive!'
          >>> hilfingers_car.fill_gas()
          'Tesla Model S gas level: 20'
          >>> hilfingers_car.gas
          20
          >>> Car.gas
          30
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> Car.headlights
          2
          >>> hilfingers_car.headlights
          2
          >>> Car.headlights = 3
          >>> hilfingers_car.headlights
          3
          >>> hilfingers_car.headlights = 2
          >>> Car.headlights
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.wheels = 2
          >>> hilfingers_car.wheels
          2
          >>> Car.num_wheels
          4
          >>> hilfingers_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          'Tesla Model S cannot drive!'
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          >>> Car.drive(hilfingers_car) # Type Error if an error occurs and Nothing if nothing is displayed
          'Tesla Model S cannot drive!'
          >>> MonsterTruck.drive(hilfingers_car) # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = MonsterTruck('Monster', 'Batmobile')
          >>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          'Monster Batmobile goes vroom!'
          >>> MonsterTruck.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.rev(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
