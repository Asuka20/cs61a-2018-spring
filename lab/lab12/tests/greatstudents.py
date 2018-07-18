test = {
  'name': 'greatstudents',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM greatstudents;
          2/29|blue|dragon|69|12
          12/25|blue|dog|17|7
          12/25|blue|dog|17|15
          1/1|green|dog|3|7
          1/1|blue|dog|11|60
          4/20|white|sloth|11|69
          1/1|black|dog|1|1
          12/25|blue|tiger|17|21
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
