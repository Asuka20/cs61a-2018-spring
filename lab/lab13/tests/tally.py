test = {
  'name': 'tally',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (tally '(james))
          ((james . 1))
          scm> (tally '(john john john))
          ((john . 3))
          scm> (tally '(james james jen))
          ((james . 2) (jen . 1))
          scm> (tally '(jane jack jane jane jack jill jane jane))
          ((jane . 5) (jack . 2) (jill . 1))
          scm> (tally '(jane jack jane jane jill jane jane jack))
          ((jane . 5) (jack . 2) (jill . 1))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab13_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
