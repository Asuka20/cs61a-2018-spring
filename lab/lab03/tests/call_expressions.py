test = {
  'name': 'Call Expressions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from operator import add
          >>> def double(x):
          ...     return x + x
          >>> def square(y):
          ...     return y * y
          >>> def f(z):
          ...     add(square(double(z)), 1)
          >>> f(4)
          Nothing
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def foo(x, y):
          ...     print("x or y")
          ...     return x or y
          >>> a = foo
          Nothing
          >>> b = foo()
          Error
          >>> c = a(print("x"), print("y"))
          x
          y
          x or y
          >>> print(c)
          None
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def welcome():
          ...     print('welcome to')
          ...     return 'hello'
          >>> def cs61a():
          ...     print('cs61a')
          ...     return 'world'
          >>> print(welcome(), cs61a())
          welcome to
          cs61a
          hello world
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
