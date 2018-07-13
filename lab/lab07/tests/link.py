test = {
  'name': 'Link',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab07 import *
          >>> link = Link(1000)
          >>> link.first
          edb6f8e1ec6e1bc0b2deae8f8cd333bf
          # locked
          >>> link.rest is Link.empty
          a60487f0dcc07e26f48fbf3cf021859d
          # locked
          >>> link = Link(1000, 2000)
          795bceccbca635277a3bbfa64bc9dba0
          # locked
          >>> link = Link(1000, Link())
          795bceccbca635277a3bbfa64bc9dba0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from lab07 import *
          >>> link = Link(1, Link(2, Link(3)))
          >>> link.first
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> link.rest.first
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> link.rest.rest.rest is Link.empty
          a60487f0dcc07e26f48fbf3cf021859d
          # locked
          >>> link.first = 9001
          >>> link.first
          2c9f5ddf74d01d9aa3f7f14577718d55
          # locked
          >>> link.rest = link.rest.rest
          >>> link.rest.first
          9a023de211dac9bf8558350f5fa3bdca
          # locked
          >>> link = Link(1)
          >>> link.rest = link
          >>> link.rest.rest.rest.rest.first
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> link = Link(2, Link(3, Link(4)))
          >>> link2 = Link(1, link)
          >>> link2.first
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> link2.rest.first
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from lab07 import *
          >>> link = Link(5, Link(6, Link(7)))
          >>> link.second
          5c5050141c04dffb4cedd647366d0e59
          # locked
          >>> link.rest.second
          54668fb96734d9b52a588e4f9ab6ed24
          # locked
          >>> link.second = 10
          >>> link                  # Look at the __repr__ method of Link
          ba6f0265220da502b423775245c4349d
          # locked
          >>> link.second = Link(8, Link(9))
          >>> link.second.first
          2ce69256b3a4325ad04f8cf5c5dd6244
          # locked
          >>> print(link)          # Look at the __str__ method of Link
          8b1e8882564f5717d6fb3792e8ea129f
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
