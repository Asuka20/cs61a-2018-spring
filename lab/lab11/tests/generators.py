test = {
  'name': 'Generators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def gen():
          ...     print("Starting here")
          ...     i = 0
          ...     while i < 6:
          ...         print("Before yield")
          ...         yield i
          ...         print("After yield")
          ...         i += 1
          >>> next(gen)
          Error
          >>> gen
          Function
          >>> g = gen()
          >>> g
          Generator
          >>> g == iter(g)
          True
          >>> next(g)
          Starting here
          Before yield
          0
          >>> next(g)
          After yield
          Before yield
          1
          >>> next(g)
          After yield
          Before yield
          2
          >>> g2 = gen()
          >>> next(g2)
          Starting here
          Before yield
          0
          >>> iter(g2)
          Generator
          >>> next(iter(g))
          After yield
          Before yield
          3
          >>> next(gen())
          Starting here
          Before yield
          0
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
