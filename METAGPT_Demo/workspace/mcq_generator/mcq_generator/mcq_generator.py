import random
import json

class MCQGenerator:
    def __init__(self):
        self.questions = []
        self.options = []

    def generate_mcq(self, number: int, type: str) -> list:
        """
        Function to generate MCQs based on the number and type provided.
        For simplicity, we are assuming that the type can be 'easy', 'medium', 'hard'.
        Depending on the type, the function will generate MCQs with different complexity.
        """
        mcqs = []
        for i in range(number):
            question = f"{type} question {i+1}"
            options = [f"option {j+1}" for j in range(4)]
            correct_option = random.choice(options)
            mcq = {
                "question": question,
                "options": options,
                "correct_option": correct_option
            }
            mcqs.append(mcq)
        return mcqs

    def customize_mcq(self, number: int, type: str) -> list:
        """
        Function to customize MCQs based on the number and type provided.
        For simplicity, we are assuming that the type can be 'easy', 'medium', 'hard'.
        Depending on the type, the function will generate MCQs with different complexity.
        The customization part is not clear from the context, so for now, we are assuming that
        customization means changing the order of the options randomly.
        """
        mcqs = self.generate_mcq(number, type)
        for mcq in mcqs:
            random.shuffle(mcq["options"])
        return mcqs
