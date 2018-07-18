test = {
  'name': 'has-cycle-constant',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (has-cycle-constant s)
          #f
          scm> (has-cycle-constant cycle)
          #t
          scm> (has-cycle-constant cycle-within)
          #t
          scm> (define long (cons-stream 1 long))
          long
          scm> (define (stream-add s n) (if (= n 0) s (cons-stream n (stream-add s (- n 1)))))
          stream-add
          scm> (define long (stream-add long 1000))
          long
          scm> (has-cycle-constant long)
          #t
          scm> (define cycle-free (stream-add nil 1000))
          cycle-free
          scm> (has-cycle-constant cycle-free)
          #f
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw11)
      scm> (define s (cons-stream 1 (cons-stream 1 nil)))
      scm> (define cycle (cons-stream 1 (cons-stream 2 cycle)))
      scm> (define cycle-within (cons-stream 1 (cons-stream 2 cycle)))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
