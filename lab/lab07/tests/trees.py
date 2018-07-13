test = {
  'name': 'Trees',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t = Tree(1, Tree(2)) # Enter Function if you believe the answer is <function ...>, Error if it errors, and Nothing if nothing is displayed.
          795bceccbca635277a3bbfa64bc9dba0
          # locked
          >>> t = Tree(1, [Tree(2)])
          >>> t.label
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> t.branches[0]
          3cfab44aef7364622af97f6d3659d4bf
          # locked
          >>> t.branches[0].label
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> t.label = t.branches[0].label
          >>> t
          ce508c4f2f51e382468306a9e6676878
          # locked
          >>> t.branches.append(Tree(4, [Tree(8)]))
          >>> len(t.branches)
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> t.branches[0]
          3cfab44aef7364622af97f6d3659d4bf
          # locked
          >>> t.branches[1]
          6461a231248273880caedd2746d49366
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
