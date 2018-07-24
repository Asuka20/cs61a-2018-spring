test = {
  'name': 'Problem 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': 'A single tile that an Ant can be placed on and that connects to other Places',
          'choices': [
            r"""
            A single tile that an Ant can be placed on and that connects to
            other Places
            """,
            'The entire space where the game takes place',
            'The tunnel that bees travel through',
            'Where the bees start out in the game'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does a Place represent in the game?'
        },
        {
          'answer': 'When the entrance of that Place instance (another Place instance) is initialized',
          'choices': [
            r"""
            When the entrance of that Place instance (another Place instance)
            is initialized
            """,
            r"""
            When the exit of that Place instance (another Place instance) is
            initalized
            """,
            'When the Place instance is initialized',
            'Never, it is always set to None'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          When is the entrance attribute of a Place instance set to another
          Place?
          """
        }
      ],
      'scored': True,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Simple test for Place
          >>> place0 = Place('place_0')
          >>> print(place0.exit)
          None
          >>> print(place0.entrance)
          None
          >>> place1 = Place('place_1', place0)
          >>> place1.exit is place0
          True
          >>> place0.entrance is place1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing if entrances are properly initialized
          >>> tunnel_len = 9
          >>> for entrance in colony.bee_entrances:
          ...     num_places = 0
          ...     place = entrance
          ...     while place is not colony.queen:
          ...         num_places += 1
          ...         assert place.entrance is not None,\
          ...                 '{0} has no entrance'.format(place.name)
          ...         place = place.exit
          ...     assert num_places == tunnel_len,\
          ...             'Found {0} places in tunnel instead of {1}'.format(num_places,tunnel_len)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing if exits and entrances are different
          >>> for place in colony.places.values():
          ...     assert place is not place.exit,\
          ...             "{0}'s exit leads to itself".format(place.name)
          ...     assert place is not place.entrance,\
          ...             "{0}'s entrance leads to itself".format(place.name)
          ...     if place.exit and place.entrance:
          ...         assert place.exit is not place.entrance,\
          ...                 "{0}'s entrance and exit are the same".format(place.name)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(make_test_assault_plan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
