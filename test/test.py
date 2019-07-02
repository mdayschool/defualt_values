
import unittest
from model import scores

class ScoreTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual({'test':0}, scores.score_input('test'))

if __name__ == '__main__':
    unittest.main()
