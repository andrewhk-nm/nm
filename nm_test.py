""" Tests for Collection of modules that are useful for my
work at Northwestern Mutual.

Andrew Henning-Kolberg
2016-02-14
"""

import unittest
import nm
from collections import namedtuple

class Test_nmpy(unittest.TestCase):
    """
    """
    def test_Test(self):
        self.assertTrue(True)

    def test_per_week_known_answers(self):
        Tpw = namedtuple('Tpw', ['goal', 'have', 'result'])

        known_answers = {Tpw(300000, 1600, 6631.111111111111),
                         }
        for ans in known_answers:
            self.assertEqual(nm.per_week(ans.goal, ans.have), ans.result)

if __name__ == '__main__':
    unittest.main()
