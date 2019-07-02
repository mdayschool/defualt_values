
import unittest
from model import scores

class ScoreTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual({'test':0}, scores.score_input('test'))
    def test_score_input_test_score_valid(self):
        self.assertEqual({'test':50}, scores.score_input('test', 50))
    def test_score_input_test_score_below_range(self):
        self.assertEqual('Invalid test score, try again!',
                         scores.score_input('test', -1))
    def test_score_input_test_score_above_range(self):
        self.assertEqual('Invalid test score, try again!',
                         scores.score_input('test', 101))
    def test_score_non_numeric(self):
        self.assertEqual('Invalid test score, try again!',
                         scores.score_input('test', 'cat'))
    def test_score_input_invalid_message(self):
        self.assertEqual('This is a valid invalid message!',
                         scores.score_input('test', 101,
                         'This is a valid invalid message!'))

if __name__ == '__main__':
    unittest.main()
