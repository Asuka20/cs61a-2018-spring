test = {
  'name': 'Problem 9',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'answer': 'The Ant instance that is in the same place as itself',
          'choices': [
            'The Ant instance that is in the same place as itself',
            'The Ant instance in the place closest to its own place',
            'A random Ant instance in the colony',
            'All the Ant instances in the colony'
          ],
          'hidden': False,
          'locked': False,
          'question': 'Which Ant does a BodyguardAnt guard?'
        },
        {
          'answer': 'By hiding the ant from Bees and acting in its place',
          'choices': [
            'By hiding the ant from Bees and acting in its place',
            'By attacking Bees that try to attack it',
            "By increasing the ant's armor",
            'By allowing Bees to pass without attacking'
          ],
          'hidden': False,
          'locked': False,
          'question': 'How does a BodyguardAnt guard its ant?'
        },
        {
          'answer': "In the BodyguardAnt's ant instance attribute",
          'choices': [
            "In the BodyguardAnt's ant instance attribute",
            "In the BodyguardAnt's ant class attribute",
            "In its place's ant instance attribute",
            "Nowhere, a BodyguardAnt has no knowledge of the ant that it's protecting"
          ],
          'hidden': False,
          'locked': False,
          'question': 'Where is the ant contained by a BodyguardAnt stored?'
        },
        {
          'answer': 'container is False for every Ant subclass except BodyguardAnt',
          'choices': [
            'container is False for every Ant subclass except BodyguardAnt',
            'container is True for every Ant subclass except BodyguardAnt',
            'container is True for all Ants',
            'container is False for all Ants'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What is the value of the container attribute for each Ant subclass?'
        },
        {
          'answer': 'When exactly one of the Ant instances is a container and the container ant does not already contain another ant',
          'choices': [
            r"""
            When exactly one of the Ant instances is a container and the
            container ant does not already contain another ant
            """,
            'When exactly one of the Ant instances is a container',
            'When both Ant instances are containers',
            'There can never be two Ant instances in the same place'
          ],
          'hidden': False,
          'locked': False,
          'question': 'When are two Ant instances allowed to occupy the same Place?'
        },
        {
          'answer': 'The container Ant',
          'choices': [
            'The container Ant',
            'The Ant being contained',
            'A list containing both Ants',
            'Whichever Ant was placed there first'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          If two Ants occupy the same Place, what is stored in that place's ant
          instance attribute?
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
          >>> # Testing BodyguardAnt parameters
          >>> bodyguard = BodyguardAnt()
          >>> BodyguardAnt.food_cost
          4
          >>> bodyguard.armor
          2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> bodyguard = BodyguardAnt()
          >>> bodyguard.action(colony) # Action without contained ant should not error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing bodyguard performs thrower's action
          >>> bodyguard = BodyguardAnt()
          >>> thrower = ThrowerAnt()
          >>> bee = Bee(2)
          >>> # Place bodyguard before thrower
          >>> colony.places["tunnel_0_0"].add_insect(bodyguard)
          >>> colony.places["tunnel_0_0"].add_insect(thrower)
          >>> colony.places["tunnel_0_3"].add_insect(bee)
          >>> bodyguard.action(colony)
          >>> bee.armor
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing bodyguard performs thrower's action
          >>> bodyguard = BodyguardAnt()
          >>> thrower = ThrowerAnt()
          >>> bee = Bee(2)
          >>> # Place thrower before bodyguard
          >>> colony.places["tunnel_0_0"].add_insect(thrower)
          >>> colony.places["tunnel_0_0"].add_insect(bodyguard)
          >>> colony.places["tunnel_0_3"].add_insect(bee)
          >>> bodyguard.action(colony)
          >>> bee.armor
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing removing a bodyguard doesn't remove contained ant
          >>> place = colony.places['tunnel_0_0']
          >>> bodyguard = BodyguardAnt()
          >>> test_ant = Ant(1)
          >>> place.add_insect(bodyguard)
          >>> place.add_insect(test_ant)
          >>> colony.remove_ant('tunnel_0_0')
          >>> place.ant is test_ant
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing bodyguarded ant keeps instance attributes
          >>> test_ant = Ant()
          >>> def new_action(colony):
          ...     test_ant.armor += 9000
          >>> test_ant.action = new_action
          >>> place = colony.places['tunnel_0_0']
          >>> bodyguard = BodyguardAnt()
          >>> place.add_insect(test_ant)
          >>> place.add_insect(bodyguard)
          >>> place.ant.action(colony)
          >>> place.ant.ant.armor
          9001
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing if we can construct a container besides BodyGuard
          >>> ant = ThrowerAnt()
          >>> ant.container = True
          >>> ant.ant = None
          >>> ant.can_contain(ThrowerAnt())
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing container can contain a special non-container bodyguard
          >>> bodyguard = BodyguardAnt()
          >>> mod_guard = BodyguardAnt()
          >>> mod_guard.container = False
          >>> bodyguard.can_contain(mod_guard)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(AssaultPlan()), dry_layout
      >>> colony = AntColony(None, hive, ant_types(), layout, (1, 9))
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
