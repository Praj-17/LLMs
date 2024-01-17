from flask import Flask, request, jsonify
from question_generator import QuestionGenerator
from enum import Enum

app = Flask(__name__)
generator = QuestionGenerator()

class Modes(Enum):
    CHOICE1 = "all"
    CHOICE2 = "single"
    CHOICE3 = "interval"

class Status(Enum):
    CHOICE1 = True
    CHOICE2 = False

class ReturnType:
    def __init__(self, status, reason, questions):
        self.status = status
        self.reason = reason
        self.questions = questions

class InputData:
    def __init__(self, mode, url, num_questions, page_number=None, interval=1):
        self.mode = mode
        self.url = url
        self.num_questions = num_questions
        self.page_number = page_number
        self.interval = interval

@app.route("/", methods=["POST"])
def run_function():
    data = request.json
    print("entered")
    # data = []
    questions = []
    status = True
    reason = ""
    url = data["url"]
    num = data["num_questions"]
    if request.method == 'POST':

        try:
            if data["mode"] == 'all':
                questions = generator.generate_mcq_questions_all_text(url=url, n=num)
                status = False
            elif data.get("page_number"):
                if data["mode"] == 'single':
                    questions = generator.generate_mcq_questions_single_page(url=url, page_number=data["page_number"], n=num)
                    status = False
                elif data["mode"] == 'interval':
                    questions = generator.generate_mcq_questions_page_interval(url=url, page_number=data["page_number"], n=num, interval=data["interval"])
                    status = False
            else:
                reason = "Please provide a param page_number"

            print(questions)
        except Exception as e:
            reason = "Exception " + str(e)

        if status == False:
            message = "Success"
        else:
            message = "Failure"

        return jsonify({
            'error': status,
            'reason': reason,
            'message': message,
            'data': questions
        })
@app.route("/hello", methods=["GET"])
def hello_world():
    return jsonify({
            'status': True,
            'reason': ""
        }) 

if __name__ == "__main__":
    generator = QuestionGenerator()
    app.run(debug=True, host='127.0.0.1', port=8000)
