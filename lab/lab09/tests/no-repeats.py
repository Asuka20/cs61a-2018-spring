test = {
  'name': 'no-repeats',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (no-repeats (list 5 4 2))
          (5 4 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (no-repeats (list 5 4 5 4 2 2))
          (5 4 2)
          scm> (no-repeats (list 5 5 5 5 5))
          (5)
          scm> (no-repeats ())
          ()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (no-repeats '(5 4 3 2 1))
          (5 4 3 2 1)
          scm> (no-repeats '(5 4 3 2 1 1))
          (5 4 3 2 1)
          scm> (no-repeats '(5 5 4 3 2 1))
          (5 4 3 2 1)
          scm> (no-repeats '(12))
          (12)
          scm> (no-repeats '(1 1 1 1 1 1))
          (1)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab09)
      scm> (load 'lab09_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
