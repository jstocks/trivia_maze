from question import Question
import random

class MultipleChoiceQuestion(Question):
    """
    This creates a subclass Question class.
    """

    def __init__(self, question, correct_ans, options):
        super().__init__(question, correct_ans)
        self.options = random.sample(options, len(options))

    def get_question(self):
        """
        Returns the Question and options
        :return: String
        """
        return self.question, self.options
