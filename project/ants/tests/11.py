test = {
  'name': 'Problem 11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'If the insect is not watersafe, its armor is reduced to 0. Otherwise, nothing happens.',
          'choices': [
            r"""
            If the insect is not watersafe, its armor is reduced to 0.
            Otherwise, nothing happens.
            """,
            "The insect's armor is reduced to 0.",
            'Nothing happens.',
            'The insect goes for a swim.'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What happens when an insect is added to a Water Place?'
        },
        {
          'answer': 'class attribute',
          'choices': [
            'class attribute',
            'instance attribute'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What type of attribute should "watersafe" be?'
        },
        {
          'answer': 'reduce_armor, in the Insect class',
          'choices': [
            'reduce_armor, in the Insect class',
            'remove_insect, in the Place class',
            'sting, in the Bee class',
            'remove_ant, in the AntColony class'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          What method deals damage to an Insect and removes it from its place
          if its armor reaches 0?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing water with Ants
          >>> test_ants = [HarvesterAnt(), Ant(), ThrowerAnt()]
          >>> test_water = Water('Water Test1')
          >>> for test_ant in test_ants:
          ...     test_water.add_insect(test_ant)
          ...     assert test_ant.armor == 0,\
          ...             '{0} should have 0 armor'.format(test_ant)
          ...     assert test_water.ant is None,\
          ...             '{0} not removed from water'.format(test_ant)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing water with soggy (non-watersafe) bees
          >>> test_bee = Bee(1000000)
          >>> test_bee.watersafe = False    # Make Bee non-watersafe
          >>> test_water = Water('Water Test2')
          >>> test_water.add_insect(test_bee)
          >>> assert test_bee.armor == 0,\
          ...         '{0} should have 0 armor'.format(test_bee)
          >>> assert len(test_water.bees) == 0,\
          ...         '{0} not removed from water'.format(test_bee)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing water with watersafe bees
          >>> test_bee = Bee(1)
          >>> test_water = Water('Water Test3')
          >>> test_water.add_insect(test_bee)
          >>> assert test_bee.armor == 1,\
          ...         '{0} should not drown'.format(test_bee)
          >>> assert test_bee in test_water.bees,\
          ...         '{0} should not have been removed from place'.format(test_bee)
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing water inheritance
          >>> def new_add_insect(self, insect):
          ...     raise NotImplementedError()
          
          >>> Place.add_insect = new_add_insect
          >>> test_bee = Bee(1)
          >>> test_water = Water('Water Test4')
          >>> passed = False
          >>> try:
          ...     test_water.add_insect(test_bee)
          ... except NotImplementedError:
          ...     passed = True
          >>> passed
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ### Make sure to place the ant before watering it!
          >>> def new_add_insect(self, insect):
          ...     raise NotImplementedError()
          
          >>> Place.add_insect = new_add_insect
          >>> test_ant = HarvesterAnt()
          >>> test_water = Water('Water Test5')
          >>> passed = False
          >>> try:
          ...     test_water.add_insect(test_ant)
          ... except NotImplementedError:
          ...     passed = True
          >>> passed
          True
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
      >>> old_add_insect = Place.add_insect
      """,
      'teardown': r"""
      >>> Place.add_insect = old_add_insect
      """,
      'type': 'doctest'
    }
  ]
}
