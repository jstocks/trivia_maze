from question import Question


class ShortAnsQuestion(Question):
    """
    This creates a subclass Question class.
    """

    def __init__(self, question, correct_ans):
        super().__init__(question, correct_ans)

    def get_question(self):
        """
        Returns the Question and options
        :return: String
        """
        return self.question, None
