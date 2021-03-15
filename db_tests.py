from db_access import *
import unittest


database = r"python_sqlite.db"


class DbTests(unittest.TestCase):
    """
    Tests for Database access.
    """

    def test_count(self):
        c = get_question_count(database)
        self.assertEqual(65, c, "Error: Count is not correct.")

    def test_q_a_multiple_choice(self):
        q = get_q_a(database, 1)
        a = [('MULTIPLE CHOICE',
              ' The day on which the Sun’s direct rays cross '
              'the celestial equator is called'), ' the equinox',
             [' the equinox', ' the aphelion', ' the solstice',
              ' the ecliptic']]
        self.assertEqual(a, q, "Error: Get q_a is not working right.")

    def test_q_a_true_false(self):
        q = get_q_a(database, 55)
        a = [('TRUE / FALSE', ' Albert Einstein developed '
                              'the theory of auroral phenomena?'),
             ' False', [' False', ' True (Fredrik Stormer)', None, None]]
        self.assertEqual(a, q, "Error: Get q_a is not working right.")

    def test_short_ans(self):
        q = get_q_a(database, 65)
        a = [('SHORT ANSWER', ' What does the unit of '
                              'angstrom measure?'), ' wavelength',
             [' wavelength', None, None, None]]
        self.assertEqual(a, q, "Error: Get q_a is not working right.")

    def test_q_a_out_of_index(self):
        try:
            q = get_q_a(database, 66)
            self.assertEqual(True, False,
                             "Shouldn't have got here! ")
        except TypeError:
            self.assertEqual(True, True, "Error: Get q_a is not "
                                         "working right.")
