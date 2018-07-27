test = {
  'name': 'Writing Tests',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> NUM_TESTS = 5 # number of tests they must write
          >>> NUM_FORMS = 5 # number of special forms they must test
          >>> NUM_PARENS = 20 # number of open parens they must use
          >>> added = run('diff -s tmpl tests.scm | grep "^>" | cut -c 3-')
          >>> FORMS = ['define', 'if', 'quote', 'cond', 'and', 'or', 'begin',
          ... 'let', 'lambda', 'mu']
          >>> added.count("expect ") >= NUM_TESTS
          True
          >>> sum([1 if x in added else 0 for x in FORMS]) >= NUM_TESTS
          True
          >>> added.count("(") >= NUM_PARENS
          True
          """,
          'locked': False,
          'hidden': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import subprocess
      >>> run = lambda cmd: subprocess.run(cmd, shell=True, encoding='utf8',
      ... stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout
      """,
      'teardown': '',
      'type': 'doctest',
    }
  ]
}