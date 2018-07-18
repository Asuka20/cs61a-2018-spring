test = {
  'name': 'has-cycle',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (has-cycle s)
          #f
          scm> (has-cycle cycle)
          #t
          scm> (has-cycle cycle-within)
          #t
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw11)
      scm> (define s (cons-stream 1 (cons-stream 2 nil)))
      scm> (define cycle (cons-stream 1 (cons-stream 1 cycle)))
      scm> (define cycle-within (cons-stream 1 (cons-stream 2 cycle)))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
