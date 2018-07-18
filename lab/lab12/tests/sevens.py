test = {
  'name': 'sevens',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM sevens;
          7
          7
          7
          You're not the boss of me!
          7
          seven
          the number 7 below.
          You're not the boss of me!
          7
          7
          7
          7
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
