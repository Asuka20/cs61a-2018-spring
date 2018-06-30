test = {
  'name': 'HOF',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def even(f):
          ...     def odd(x):
          ...         if x < 0:
          ...             return f(-x)
          ...         return f(x)
          ...     return odd
          >>> steven = lambda x: x
          >>> stewart = even(steven)
          >>> stewart
          Function
          >>> stewart(61)
          61
          >>> stewart(-4)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Try drawing an environment diagram if you get stuck!
          >>> higher_order_lambda = lambda f: lambda x: f(x)
          >>> def cake():
          ...    print('beets')
          ...    def pie():
          ...        print('sweets')
          ...        return 'cake'
          ...    return pie
          >>> chocolate = cake()
          beets
          >>> chocolate
          Function
          >>> chocolate()
          sweets
          'cake'
          >>> more_chocolate, more_cake = chocolate(), cake
          sweets
          >>> more_chocolate
          'cake'
          >>> def snake(x, y):
          ...    if cake == more_cake:
          ...        return lambda y: x + y
          ...    else:
          ...        return x + y
          >>> snake(10, 20)
          Function
          >>> snake(10, 20)(30)
          40
          >>> cake = 'cake'
          >>> snake(10, 20)
          30
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
