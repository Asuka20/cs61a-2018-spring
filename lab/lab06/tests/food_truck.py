test = {
  'name': 'Food Truck',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> class FoodTruck(MonsterTruck):
          ...    delicious = 'meh'
          ...    def serve(self):
          ...        if FoodTruck.size == 'delicious':
          ...            print('Yum!')
          ...        if self.food != 'Tacos':
          ...            return 'But no tacos...'
          ...        else:
          ...            return 'Mmm!'
          >>> taco_truck = FoodTruck('Tacos', 'Truck')
          >>> taco_truck.food = 'Guacamole'
          >>> taco_truck.serve() # Type Error if an error occurs and Nothing if nothing is displayed
          b0ffc1b07af4eb85e09c4128f5bf5207
          # locked
          >>> taco_truck.food = taco_truck.make
          >>> FoodTruck.size = taco_truck.delicious
          >>> taco_truck.serve() # Type Error if an error occurs and Nothing if nothing is displayed
          084d4fea107bee8c8124cf8d541ff942
          # locked
          >>> taco_truck.size = 'delicious'
          >>> taco_truck.serve() # Type Error if an error occurs and Nothing if nothing is displayed
          084d4fea107bee8c8124cf8d541ff942
          # locked
          >>> FoodTruck.pop_tire() # Type Error if an error occurs and Nothing if nothing is displayed
          34db8258c24aff02f4e0aeaa32af407b
          # locked
          >>> FoodTruck.pop_tire(taco_truck) # Type Error if an error occurs and Nothing if nothing is displayed
          75e7eb45dffa5d30654f02570401dfe8
          # locked
          >>> taco_truck.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          238e48b17a8085331a1d671045b7a572
          179a547aff949801cac7a48bc120aa4d
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
