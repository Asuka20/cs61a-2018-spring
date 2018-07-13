test = {
  'name': 'Attributes',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class Foo:
          ...     a = 10
          ...     def __init__(self, a):
          ...         self.a = a
          >>> class Bar(Foo):
          ...     b = 1
          >>> a = Foo(5)
          >>> b = Bar(2)
          >>> a.a
          3595d1fdbdda5f2ecaa323401627e273
          # locked
          >>> b.a
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> Foo.a
          8be8039fce6ea3657f1a0a9143efa89d
          # locked
          >>> Bar.b
          802285b020b27240a3824a7e42f8cc8c
          # locked
          >>> Bar.a
          8be8039fce6ea3657f1a0a9143efa89d
          # locked
          >>> b.b
          802285b020b27240a3824a7e42f8cc8c
          # locked
          >>> Foo.c = 15
          >>> Foo.c
          fb7891bbea16434eb7fc817790a6b564
          # locked
          >>> a.c
          fb7891bbea16434eb7fc817790a6b564
          # locked
          >>> b.c
          fb7891bbea16434eb7fc817790a6b564
          # locked
          >>> Bar.c
          fb7891bbea16434eb7fc817790a6b564
          # locked
          >>> b.b = 3
          >>> b.b
          a6a221ff20ce085ab4bedaca5044f971
          # locked
          >>> Bar.b
          802285b020b27240a3824a7e42f8cc8c
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
