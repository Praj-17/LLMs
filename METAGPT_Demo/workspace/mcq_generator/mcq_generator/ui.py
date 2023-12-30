## ui.py
import tkinter as tk
from mcq_generator import MCQGenerator

class UI:
    def __init__(self, mcq_generator: MCQGenerator):
        self.mcq_generator = mcq_generator
        self.root = tk.Tk()
        self.root.title("MCQ Generator")
        self.mcq_frame = None

    def display_mcq(self, mcq: list):
        """
        Function to display the MCQs in the GUI.
        """
        if self.mcq_frame:
            self.mcq_frame.destroy()
        self.mcq_frame = tk.Frame(self.root)
        self.mcq_frame.pack()
        for i, question in enumerate(mcq):
            q_label = tk.Label(self.mcq_frame, text=f"Q{i+1}: {question['question']}")
            q_label.pack()
            for option in question['options']:
                o_button = tk.Radiobutton(self.mcq_frame, text=option)
                o_button.pack()

    def get_user_input(self) -> dict:
        """
        Function to get the user input for the number and type of MCQs.
        """
        number_label = tk.Label(self.root, text="Number of questions:")
        number_label.pack()
        number_entry = tk.Entry(self.root)
        number_entry.pack()
        type_label = tk.Label(self.root, text="Type of questions:")
        type_label.pack()
        type_entry = tk.Entry(self.root)
        type_entry.pack()
        submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        submit_button.pack()
        self.root.mainloop()
        return {"number": int(number_entry.get()), "type": type_entry.get()}

    def submit(self):
        """
        Function to handle the submit button click event.
        """
        self.root.quit()
