test = {
  'name': 'matchmaker',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker LIMIT 10;
          wolf|Fur Elise|green|blue
          cat|Smells Like Teen Spirit|purple|purple
          cat|Smells Like Teen Spirit|purple|green
          cat|Smells Like Teen Spirit|purple|blue
          dog|Finesse|navy|red
          dog|Finesse|navy|mint
          dog|Finesse|navy|blue
          dog|Finesse|navy|blue
          elephant|The Middle|purple|yellow
          dog|Finesse|red|mint
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
