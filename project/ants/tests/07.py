test = {
  'name': 'Problem 7',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': 'All Ant types have a blocks_path attribute that is inherited from the Ant superclass',
          'choices': [
            r"""
            All Ant types have a blocks_path attribute that is inherited from
            the Ant superclass
            """,
            'Only the NinjaAnt has a blocks_path attribute',
            'None of the Ant subclasses have a blocks_path attribute',
            'All Ant types except for NinjaAnt have a blocks_path attribute'
          ],
          'hidden': False,
          'locked': False,
          'question': 'Which Ant types have a blocks_path attribute?'
        },
        {
          'answer': 'blocks_path is True for every Ant subclass except NinjaAnt',
          'choices': [
            'blocks_path is True for every Ant subclass except NinjaAnt',
            'blocks_path is False for every Ant subclass except NinjaAnt',
            'blocks_path is True for all Ants',
            'blocks_path is False for all Ants'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What is the value of blocks_path for each Ant subclass?'
        },
        {
          'answer': "When there is an Ant whose blocks_path attribute is True in the Bee's place",
          'choices': [
            "When there is an Ant in the Bee's place",
            r"""
            When there is an Ant whose blocks_path attribute is True in the
            Bee's place
            """,
            "When there is not an NinjaAnt in the Bee's place",
            "When there are no Ants in the Bee's place"
          ],
          'hidden': False,
          'locked': False,
          'question': 'When is the path of a Bee blocked?'
        },
        {
          'answer': "Reduces the Bee's armor by the NinjaAnt's damage attribute",
          'choices': [
            "Reduces the Bee's armor by the NinjaAnt's damage attribute",
            "Reduces the Bee's armor to 0",
            "Nothing, the NinjaAnt doesn't damage Bees",
            "Blocks the Bee's path"
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does a NinjaAnt do to each Bee that flies in its place?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing NinjaAnt parameters
          >>> ninja = NinjaAnt()
          >>> ninja.armor
          1
          >>> NinjaAnt.food_cost
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing NinjaAnts do not block bees
          >>> p0 = colony.places["tunnel_0_0"]
          >>> p1 = colony.places["tunnel_0_1"]  # p0 is p1's exit
          >>> bee = Bee(2)
          >>> ninja = NinjaAnt()
          >>> thrower = ThrowerAnt()
          >>> p0.add_insect(thrower)            # Add ThrowerAnt to p0
          >>> p1.add_insect(bee)
          >>> p1.add_insect(ninja)              # Add the Bee and NinjaAnt to p1
          >>> bee.action(colony)
          >>> bee.place is ninja.place          # Did NinjaAnt block the Bee from moving?
          False
          >>> bee.place is p0
          True
          >>> ninja.armor
          1
          >>> bee.action(colony)
          >>> bee.place is p0                   # Did ThrowerAnt block the Bee from moving?
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing NinjaAnt strikes all bees in its place
          >>> test_place = colony.places["tunnel_0_0"]
          >>> for _ in range(3):
          ...     test_place.add_insect(Bee(2))
          >>> ninja = NinjaAnt()
          >>> test_place.add_insect(ninja)
          >>> ninja.action(colony)   # should strike all bees in place
          >>> [bee.armor for bee in test_place.bees]
          [1, 1, 1]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing NinjaAnt strikes all bees, even if some expire
          >>> test_place = colony.places["tunnel_0_0"]
          >>> for _ in range(3):
          ...     test_place.add_insect(Bee(1))
          >>> ninja = NinjaAnt()
          >>> test_place.add_insect(ninja)
          >>> ninja.action(colony)   # should strike all bees in place
          >>> len(test_place.bees)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing damage is looked up on the instance
          >>> place = colony.places["tunnel_0_0"]
          >>> bee = Bee(900)
          >>> place.add_insect(bee)
          >>> buffNinja = NinjaAnt()
          >>> buffNinja.damage = 500  # Sharpen the sword
          >>> place.add_insect(buffNinja)
          >>> buffNinja.action(colony)
          >>> bee.armor
          400
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing Ninja ant does not crash when left alone
          >>> ninja = NinjaAnt()
          >>> colony.places["tunnel_0_0"].add_insect(ninja)
          >>> ninja.action(colony)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing Bee does not crash when left alone
          >>> bee = Bee(3)
          >>> colony.places["tunnel_0_1"].add_insect(bee)
          >>> bee.action(colony)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
