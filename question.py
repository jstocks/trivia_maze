from abc import ABC, abstractmethod


class Question(ABC):
    """
       Abstract base class for a shape, should not be
       used for a concrete object.
    """

    def __init__(self, question="", correct_ans=""):
        self.question = question
        self.__correct_ans = correct_ans

    @abstractmethod
    def get_question(self):
        pass

    def verify_ans(self, ans):
        return True if ans == self.__correct_ans else False

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is Question:
            attrs = set(dir(subclass))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented
