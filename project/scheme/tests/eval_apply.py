test = {
  'name': 'Understanding scheme.py',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'A primitive expression or a list expression',
          'choices': [
            'A primitive expression or a list expression',
            'A pair or a list',
            'A special form or a call expression',
            'A primitive expression or a special form'
          ],
          'hidden': False,
          'locked': False,
          'question': 'A Scheme expression can be either...'
        },
        {
          'answer': 'env.lookup(expr)',
          'choices': [
            'env.lookup(expr)',
            'expr.first',
            'scheme_symbolp(expr)',
            'SPECIAL_FORMS[first](rest, env)'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What expression in the body of scheme_eval finds the value of a name?'
        },
        {
          'answer': 'Check if the first element in the list is a symbol and that that symbol is in the dictionary SPECIAL_FORMS',
          'choices': [
            r"""
            Check if the first element in the list is a symbol and
                        that that symbol is in the dictionary SPECIAL_FORMS
            """,
            'Check if the first element in the list is a symbol',
            'Check if the expression is in the dictionary SPECIAL_FORMS'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          How do we know if a given list expression is a special
                      form?
          """
        },
        {
          'answer': 'SchemeError("1 is not callable")',
          'choices': [
            'SchemeError("malformed list: (1)")',
            'SchemeError("1 is not callable")',
            'AssertionError',
            'SchemeError("unknown identifier: 1")'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What exception should be raised for the expression (1)?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
