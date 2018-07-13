test = {
  'name': 'Orders of Growth',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'ca3b52a52f737de1594b82692c7107d1',
          'choices': [
            'Theta(log(n))',
            'Theta(n)',
            'Theta(n^2)',
            'Theta(2^n)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the order of growth of `is_prime` in terms of `n`?
          
          def is_prime(n):
              for i in range(2, n):
                  if n % i == 0:
                      return False
              return True
          """
        },
        {
          'answer': 'f0e700c9308ddfeac9a7d53c3bea77d7',
          'choices': [
            'Theta(log(n))',
            'Theta(n)',
            'Theta(n^2)',
            'Theta(2^n)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the order of growth of `bar` in terms of `n`?
          
          def bar(n):
              i, sum = 1, 0
              while i <= n:
                  sum += biz(n)
                  i += 1
              return sum
          
          def biz(n):
              i, sum = 1, 0
              while i <= n:
                  sum += i**3
                  i += 1
              return sum
          """
        },
        {
          'answer': '4d74df1689ec204e0068a2decdb74895',
          'choices': [
            'Theta(log(n))',
            'Theta(n)',
            'Theta(n^2)',
            'Theta(2^n)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the order of growth of `foo` in terms of `n`, where `n` is
          the length of `lst`?
          
          def foo(lst, i):
              mid = len(lst) // 2
              if mid == 0:
                  return lst
              elif i > 0:
                  return foo(lst[mid:], -1)
              else:
                  return foo(lst[:mid], 1)
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
