## main.py
from mcq_generator import MCQGenerator
from ui import UI

class Main:
    def __init__(self):
        self.mcq_generator = MCQGenerator()
        self.ui = UI(self.mcq_generator)

    def main(self):
        # Get user input for the number and type of MCQs
        user_input = self.ui.get_user_input()
        number = user_input["number"]
        type = user_input["type"]
        customize = user_input["customize"]

        # Generate MCQs based on the user input
        if customize:
            mcqs = self.mcq_generator.customize_mcq(number, type)
        else:
            mcqs = self.mcq_generator.generate_mcq(number, type)

        self.ui.display_mcq(mcqs)


if __name__ == "__main__":
    main = Main()
    main.main()
    
