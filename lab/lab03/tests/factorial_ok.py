test = {
  'name': 'factorial_ok',
  'points': 0,
  'suites': [
    {
      'type': 'concept',
      'scored': True,
      'cases': [
        {
          'question': r"""
          Consider this implementation of the factorial function:
          def factorial(n):
              if n == 0:
                  return 1
              else:
                  return factorial(n-1)

          What is wrong with it?
          """,
          'choices': [
            'The return statement in the recursive case is missing',
            'The base case is flawed: it should be n <= 0',
            'The recursive call is not combined correctly into the final solution',
            'The variable n does not change, causing a infinite loop',
          ],
          'answer': 'The recursive call is not combined correctly into the final solution',
        },
      ]
    }
  ]
}
