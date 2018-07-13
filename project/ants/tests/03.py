test = {
  'name': 'Problem 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': '8921294332adbef5e6db219b03adedf9',
          'choices': [
            r"""
            The ThrowerAnt finds the nearest place in front of its own place
            that has Bees and throws at a random Bee in that place
            """,
            r"""
            The ThrowerAnt finds the nearest place behind its own place
            that has Bees and throws at a random Bee in that place
            """,
            r"""
            The ThrowerAnt finds the nearest place in either direction that has
            Bees and throws at a random Bee in that place
            """,
            'The ThrowerAnt throws at a random Bee in its own Place'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What Bee should a ThrowerAnt throw at?'
        },
        {
          'answer': '9bd9c23a391f841e8d9e4147c56659a7',
          'choices': [
            "The place's entrance instance attribute",
            "The place's exit instance attribute",
            'Increment the place by 1',
            'Decrement the place by 1'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How do you get the Place object in front of another Place object?'
        },
        {
          'answer': '2ca313dd416803bfaecbcf4a2d1851c1',
          'choices': [
            'The Hive',
            'None',
            'An empty Place'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What is the entrance of the first Place in a tunnel?'
        },
        {
          'answer': '044ef3c0c6fd739b6260fe6f6cae71dd',
          'choices': [
            'None',
            'A random Bee in the Hive',
            'The closest Bee behind the ThrowerAnt'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What should nearest_bee return if there is no Bee in front of the ThrowerAnt in the tunnel?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing nearest_bee
          >>> thrower = ThrowerAnt()
          >>> near_bee = Bee(2) # A Bee with 2 armor
          >>> far_bee = Bee(3)  # A Bee with 3 armor
          >>> ant_place = colony.places['tunnel_0_0']
          >>> near_place = colony.places['tunnel_0_3']
          >>> far_place = colony.places['tunnel_0_6']
          >>> ant_place.add_insect(thrower)
          >>> near_place.add_insect(near_bee)
          >>> far_place.add_insect(far_bee)
          >>> nearest_bee = thrower.nearest_bee(colony.hive)
          >>> nearest_bee.armor
          20d533d3e06345c8bd7072212867f2d1
          # locked
          >>> thrower.action(colony)    # Attack! ThrowerAnts do 1 damage
          >>> near_bee.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> far_bee.armor
          81a7d27d1a4a958871bb97b545b871db
          # locked
          >>> thrower.place is ant_place    # Don't change self.place!
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing nearest_bee
          >>> thrower = ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(thrower)
          >>> place = colony.places['tunnel_0_0']
          >>> near_bee = Bee(2)
          >>> far_bee = Bee(2)
          >>> colony.places["tunnel_0_3"].add_insect(near_bee)
          >>> colony.places["tunnel_0_6"].add_insect(far_bee)
          >>> hive = colony.hive
          >>> thrower.nearest_bee(hive) is far_bee
          False
          >>> thrower.nearest_bee(hive) is near_bee
          True
          >>> thrower.action(colony)    # Attack!
          >>> near_bee.armor            # Should do 1 damage
          1
          >>> thrower.place is place    # Don't change self.place!
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing Nearest bee not in the hive
          >>> thrower = ThrowerAnt()
          >>> colony.places["tunnel_0_0"].add_insect(thrower)
          >>> hive = colony.hive
          >>> bee = Bee(2)
          >>> hive.add_insect(bee)      # Adding a bee to the hive
          >>> thrower.nearest_bee(hive) is bee
          False
          >>> thrower.action(colony)    # Attempt to attack
          >>> bee.armor                 # Bee armor should not change
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Test that ThrowerAnt attacks bees on its own square
          >>> thrower = ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(thrower)
          >>> near_bee = Bee(2)
          >>> colony.places["tunnel_0_0"].add_insect(near_bee)
          >>> thrower.nearest_bee(colony.hive) is near_bee
          True
          >>> thrower.action(colony)   # Attack!
          >>> near_bee.armor           # should do 1 damage
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Test that ThrowerAnt attacks bees at end of tunnel
          >>> thrower = ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(thrower)
          >>> near_bee = Bee(2)
          >>> colony.places["tunnel_0_8"].add_insect(near_bee)
          >>> thrower.nearest_bee(colony.hive) is near_bee
          True
          >>> thrower.action(colony)   # Attack!
          >>> near_bee.armor           # should do 1 damage
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing ThrowerAnt chooses a random target
          >>> thrower = ThrowerAnt()
          >>> colony.places["tunnel_0_0"].add_insect(thrower)
          >>> bee1 = Bee(1001)
          >>> bee2 = Bee(1001)
          >>> colony.places["tunnel_0_3"].add_insect(bee1)
          >>> colony.places["tunnel_0_3"].add_insect(bee2)
          >>> # Throw 1000 times. The first bee should take ~1000*1/2 = ~500 damage,
          >>> # and have ~501 remaining.
          >>> for _ in range(1000):
          ...     thrower.action(colony)
          >>> # Test if damage to bee1 is within 6 standard deviations (~95 damage)
          >>> # If bees are chosen uniformly, this is true 99.9999998% of the time.
          >>> def dmg_within_tolerance():
          ...     return abs(bee1.armor-501) < 95
          >>> dmg_within_tolerance()
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
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
