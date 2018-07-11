test = {
  'name': 'Structure',
  'points': 0,
  'suites': [
    {
      'type': 'concept',
      'scored': False,
      'cases': [
        {
          'question': r"""
          Which constructor call creates the following tree structure?
              1
            / | \
           2  3  4
             /
            5
          """,
          'choices': [
            'tree(1, [tree(2), tree(3, [tree(5)]), tree(4)])',
            'tree(1, (tree(2), tree(3, (tree(5))), tree(5)))',
            'tree(2, [tree(1, tree(3, tree(5)))], tree(4))',
            'tree(1, [tree(2), tree(3), tree(4)], tree(5))',
          ],
          'answer': 'tree(1, [tree(2), tree(3, [tree(5)]), tree(4)])',
        },
        {
          'question': r"""
          Which constructor call creates the following tree structure?
                3
              / | \
             6  2  7
            / \
           2   1
          """,
          'choices': [
            'tree(3, [tree(6, [tree(2), tree(1)]), tree(2), tree(7)])',
            'tree(3, tree(6, [tree(2), tree(1)]), tree(2), tree(7))',
            'tree(3, [tree(6), [tree(2), tree(1)], tree(2), tree(7)])',
            'tree(3, tree(6), [tree(2), tree(1)], [tree(2), tree(7)])',
          ],
          'answer': 'tree(3, [tree(6, [tree(2), tree(1)]), tree(2), tree(7)])',
        },
        {
          'question': r"""
          How many branches does the following tree have?
                7
               / \
              2  4
             /|  |
            1 5  2
              |
              3
          """,
          'choices': [
            '2',
            '3',
            '6',
            '7',
          ],
          'answer': '2',
        },
        {
          'question': r"""
          Given the following tree structure, what are all the leaves?
                7
              / | \
             3  2  4
            /  /|
           6  1 5
          """,
          'choices': [
            '6, 1, 5',
            '6, 1, 5, 4',
            '7, 6, 1, 5, 4',
            'None of the above',
          ],
          'answer': '6, 1, 5, 4',
        }
      ]
    }
  ]
}
