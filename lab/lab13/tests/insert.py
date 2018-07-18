test = {
  'name': 'insert',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (insert 1 '(2))
          (1 2)
          scm> (insert 2 '(1))
          (1 2)
          scm> (insert 5 '(2 4 6 8))
          (2 4 5 6 8)
          scm> (insert 1000 '(1 2 3 4 5 6))
          (1 2 3 4 5 6 1000)
          scm> (insert -10 '(-2 0 2))
          (-10 -2 0 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (tail-list n so-far)
          ....   (if (= n 0)
          ....       so-far
          ....       (tail-list (- n 1) (cons 1 so-far))))
          tail-list
          scm> (define big-list (tail-list 500 '()))
          big-list
          scm> (define result (insert 4 big-list)) ; Test for tail recursion
          result
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
