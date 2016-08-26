import unittest
from .questions import QuestionStructure


class TestQuestionStructure(unittest.TestCase):
    def test_is_instance(self):
        obj = QuestionStructure('Q1', 'A1', 'C1')
        self.assertIsInstance(obj, QuestionStructure)

    def test_empty_string_answer(self):
        obj2 = QuestionStructure('Q2', 'A2', '')
        self.assertTrue('You haven\'t answered the question', obj2)

if __name__ == "__main__":
    unittest.main()
