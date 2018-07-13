test = {
  'name': 'FooBar',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class Foo:
          ...     def print_one(self):
          ...         print('foo')
          ...     def print_two():
          ...         print('foofoo')
          >>> f = Foo()
          >>> f.print_one()
          7074a0568ca671bc694d2144b0fc8cd6
          # locked
          >>> f.print_two()
          8a2fd4e4c3c6dcce2dc631af62ee217a
          # locked
          >>> Foo.print_two()
          627f5160f96889f25547a499ca5bf6dd
          # locked
          >>> class Bar(Foo):
          ...     def print_one(self):
          ...         print('bar')
          >>> b = Bar()
          >>> b.print_one()
          281553bfd1b54a867647d025651f97a5
          # locked
          >>> Bar.print_two()
          627f5160f96889f25547a499ca5bf6dd
          # locked
          >>> Bar.print_one = lambda x: print('new bar')
          >>> b.print_one()
          7cba3a01d7587a7c2b10adbbc860994c
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
