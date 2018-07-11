test = {
  'name': 'Dictionaries',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
          >>> pokemon['pikachu']
          25
          >>> len(pokemon)
          3
          >>> pokemon['jolteon'] = 135
          >>> pokemon['mew'] = 25
          >>> len(pokemon)
          4
          >>> 'mewtwo' in pokemon
          False
          >>> 'pikachu' in pokemon
          True
          >>> 25 in pokemon
          False
          >>> 148 in pokemon.values()
          True
          >>> 151 in pokemon.keys()
          False
          >>> 'mew' in pokemon.keys()
          True
          >>> pokemon['ditto'] = pokemon['jolteon']
          >>> pokemon['ditto']
          135
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> letters = {'a': 1, 'b': 2, 'c': 3}
          >>> 'a' in letters
          True
          >>> 2 in letters
          False
          >>> sorted(list(letters.keys()))
          ['a', 'b', 'c']
          >>> sorted(list(letters.items()))
          [('a', 1), ('b', 2), ('c', 3)]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> food = {'bulgogi': 10, 'falafel': 4, 'ceviche': 7}
          >>> food['ultimate'] = food['bulgogi'] + food['ceviche']
          >>> food['ultimate']
          17
          >>> len(food)
          4
          >>> food['ultimate'] += food['falafel']
          >>> food['ultimate']
          21
          >>> food['bulgogi'] = food['falafel']
          >>> len(food)
          4
          >>> 'gogi' in food
          False
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
