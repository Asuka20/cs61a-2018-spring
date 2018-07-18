test = {
  'name': 'lets-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from fa17favnum;
          69|66
          sqlite> SELECT * from fa17favpets;
          dog|57
          cat|33
          dragon|14
          panda|14
          tiger|14
          lion|13
          penguin|12
          dolphin|10
          john denero|9
          elephant|8
          sqlite> SELECT * from sp18favpets;
          dog|47
          cat|20
          tiger|16
          panda|11
          dragon|9
          dolphin|5
          elephant|5
          hedgehog|5
          monkey|5
          capybara|4
          sqlite> SELECT * from sp18dog;
          dog|47
          sqlite> SELECT * from sp18alldogs;
          dog|55
          sqlite> SELECT * from obedienceimages;
          7|Image 1|24
          7|Image 2|28
          7|Image 3|19
          7|Image 4|39
          7|Image 5|12
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
