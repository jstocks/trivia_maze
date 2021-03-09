from abc import ABC, abstractmethod


class Question(ABC):
    """
       Abstract base class for a shape, should not be
       used for a concrete object.
    """

    def __init__(self, question="", correct_ans=""):

        # connect to sqlite database file
        # get question line
        # question = conn.exec("select statement")
        #

        # with the data row from sqlite
        # fill up the question and the answer to the class properties
        self.question = question
        self.__answers = None
        self.__correct_ans = correct_ans

    @abstractmethod
    def get_question(self):
        return self.question

    def verify_ans(self, ans):
        return ans.lower().strip() == self.__correct_ans.lower().strip()

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is Question:
            attrs = set(dir(subclass))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented
