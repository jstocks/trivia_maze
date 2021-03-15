import unittest
from multiple_choice_question import MultipleChoiceQuestion
from short_ans_question import ShortAnsQuestion
from true_false_question import TrueFalseQuestion
from db_access import *

database = r"python_sqlite.db"


class QuestionTests(unittest.TestCase):
    """
    Tests for answer verification in Question Class.
    """

    def test_multiple_choice_wrong_ans(self):
        q_a = get_q_a(database, 1)
        question = MultipleChoiceQuestion(q_a[0][1], q_a[1], q_a[2])
        ans = ' the aphelion'
        result = question.verify_ans(ans)
        self.assertEqual(False, result, "Error: Answer verification")

    def test_multiple_choice_correct_ans(self):
        q_a = get_q_a(database, 1)
        question = MultipleChoiceQuestion(q_a[0][1], q_a[1], q_a[2])
        ans = ' the equinox'
        result = question.verify_ans(ans)
        self.assertEqual(True, result, "Error: Answer verification")

    def test_true_false_wrong_ans(self):
        q_a = get_q_a(database, 55)
        question = TrueFalseQuestion(q_a[0][1], q_a[1])
        ans = ' True'
        result = question.verify_ans(ans)
        self.assertEqual(False, result, "Error: Answer verification")

    def test_true_false_correct_ans(self):
        q_a = get_q_a(database, 55)
        question = TrueFalseQuestion(q_a[0][1], q_a[1])
        ans = ' False'
        result = question.verify_ans(ans)
        self.assertEqual(True, result, "Error: Answer verification")

    def test_short_ans_wrong_ans(self):
        q_a = get_q_a(database, 65)
        question = ShortAnsQuestion(q_a[0][1], q_a[1])
        ans = ' wave'
        result = question.verify_ans(ans)
        self.assertEqual(False, result, "Error: Answer verification")

    def test_short_ans_correct_ans(self):
        q_a = get_q_a(database, 65)
        question = ShortAnsQuestion(q_a[0][1], q_a[1])
        ans = 'wavelength'
        result = question.verify_ans(ans)
        self.assertEqual(True, result, "Error: Answer verification")
