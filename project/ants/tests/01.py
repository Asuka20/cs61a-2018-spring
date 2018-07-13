test = {
  'name': 'Problem 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'b11e19127a1cf83e285f83984cae6d4f',
          'choices': [
            r"""
            Placing an ant into the colony will decrease the colony's total
            available food by that ant's food_cost
            """,
            r"""
            Each turn, each Ant in the colony eats food_cost food from the
            colony's total available food
            """,
            r"""
            Each turn, each Ant in the colony adds food_cost food to the
            colony's total available food
            """
          ],
          'hidden': False,
          'locked': True,
          'question': 'What is the purpose of the food_cost attribute?'
        },
        {
          'answer': 'a2025d9f82f64cc8a211c3dbc92f507b',
          'choices': [
            'class, all Ants of the same subclass cost the same to deploy',
            'class, all Ants cost the same to deploy no matter what type of Ant it is',
            'instance, the food_cost of an Ant depends on the location it is placed',
            'instance, the food_cost of an Ant is randomized upon initialization'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What type of attribute is food_cost?'
        }
      ],
      'scored': True,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> HarvesterAnt.food_cost
          20d533d3e06345c8bd7072212867f2d1
          # locked
          >>> ThrowerAnt.food_cost
          81a7d27d1a4a958871bb97b545b871db
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing HarvesterAnt action
          >>> # Note that initializing an Ant here doesn't cost food, only
          >>> # deploying an Ant in the game simulation does
          >>> #
          >>> hive = Hive(make_test_assault_plan())
          >>> colony = AntColony(None, hive, ant_types(), dry_layout, (1, 9))
          >>> colony.food = 4
          >>> harvester = HarvesterAnt()
          >>> harvester.action(colony)
          >>> colony.food
          62674984f877ec783f37e8b8b9c264d0
          # locked
          >>> harvester.action(colony)
          >>> colony.food
          50ae32be3e31df6c59633df7fdfb3a72
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
