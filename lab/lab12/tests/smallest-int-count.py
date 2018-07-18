test = {
  'name': 'smallest-int-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int_count LIMIT 50;
          1|101
          2|13
          3|10
          4|9
          5|5
          6|7
          7|6
          8|3
          9|4
          10|6
          11|5
          12|7
          13|5
          14|3
          15|2
          16|2
          17|11
          18|1
          19|3
          20|1
          21|2
          22|6
          23|12
          24|1
          25|3
          26|1
          27|3
          28|1
          29|5
          31|8
          32|1
          33|2
          34|3
          37|3
          38|2
          41|2
          42|2
          43|1
          44|1
          45|1
          46|1
          52|1
          53|3
          54|1
          55|1
          56|1
          58|1
          59|1
          61|2
          63|1
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
