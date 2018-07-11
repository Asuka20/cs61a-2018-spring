test = {
  'name': 'Problem 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Remember that the mean should return a decimal value
          >>> # If any line causes an error, write AssertionError
          >>> mean([0])
          0.0
          >>> mean([1, 2, 3, 4, 5])
          3.0
          >>> mean([3, 1, -2, 7])
          2.25
          >>> mean([1] * 100000)
          1.0
          >>> mean([2, 4, 6, 8] * 1000000)
          5.0
          >>> mean([])
          AssertionError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from utils import mean
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
