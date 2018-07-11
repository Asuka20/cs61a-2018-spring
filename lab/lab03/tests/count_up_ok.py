test = {
  'name': 'count_up_ok',
  'points': 0,
  'suites': [
    {
      'type': 'concept',
      'scored': False,
      'cases': [
      {
          'question': r"""
          Consider another function that prints from 1 to n:
          >>> count_up(5)
          1
          2
          3
          4
          5

          And here's how we define it:
          def count_up(n):
              i = 1
              if i == n:
                  return
              print(i)
              i += 1
              count_up(n-1)

          What's is wrong with this definition?
          """,
          'choices': [
            'Should use return i instead of print(i)',
            'The variable i resets back to 1 for each function call, printing 1 all the time',
            'The return statement before the recursive call is missing',
            'The recursive call should be count_up(n+1)',
          ],
          'answer': 'The variable i resets back to 1 for each function call, printing 1 all the time',
        },
        {
          'question': r"""
          Consider a count up function that prints from 1 to n:
          >>> count_up(5)
          1
          2
          3
          4
          5

          And here's how we define it:
          def count_up(n):
              if n <= 0:
                  return
              else:
                  count_up(n)
                  print(n)

          What is wrong with this definition?
          """,
          'choices': [
            'The variable n does not change, causing a infinite loop',
            'The return statement in the recursive case is missing',
            'i is a local variable, which is not allowed in recursive functions',
            'Should use return i instead of print(i)',
          ],
          'answer': 'The variable n does not change, causing a infinite loop',
        },
      ]
    }
  ]
}
