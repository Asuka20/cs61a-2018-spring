test = {
  'name': 'obedience',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM obedience LIMIT 10;
          7|Image 1
          7|Image 5
          the number 7 below.|Image 1
          7|Image 2
          7|Image 2
          the number 7 below.|Image 1
          the number 7 below.|Image 5
          7|Image 1
          You're not the boss of me!|Image 4
          7|Image 4
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
