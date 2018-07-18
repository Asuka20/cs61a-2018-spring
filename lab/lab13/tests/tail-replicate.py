test = {
  'name': 'tail replicate',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (tail-replicate 3 10)
          (3 3 3 3 3 3 3 3 3 3)
          scm> (tail-replicate 5 0)
          ()
          scm> (tail-replicate 5 1)
          (5)
          scm> (tail-replicate 100 5)
          (100 100 100 100 100)
          scm> (define a (tail-replicate 10 500)) ; Test for tail recursion
          a
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab13)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
