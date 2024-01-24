from flask import Flask, request, jsonify
from question_generator import QuestionGenerator, ChatWithPDF
from PDFCrawler import PDFURLCrawler
from enum import Enum

app = Flask(__name__)

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
def generate_questions():
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
@app.route("/crawl", methods=["POST"])
def crawl_urls():
    data = request.json
    pdf_urls = []
    status = True
    reason = ""
    url = data["url"]
    depth = data.get('depth', 1)
    if request.method == 'POST':

        try:
            
            pdf_urls = crawler.crawl(url=url, limit = depth, base_url=url)
            status = True
            
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
            'data': pdf_urls
        })
@app.route("/chat", methods=["POST"])
def chatwithpdf():
    data = request.json
    print("entered")
    # data = []
    answer = ""
    status = True
    reason = ""
    url = data["url"]
    page_no = 0
    chat_history = []
    if request.method == 'POST':

        try:
            chat_history = data.get('chat_history', [])
            question = data.get("question", "")
            if data["mode"] == 'all':
                answer = chat.chat_with_whole_pdf(url=url, question=question, chat_history=chat_history)
                status = False
            elif data.get("page_number"):
                if data["mode"] == 'single':
                    answer = chat.chat_with_single_page(url=url, page_number=data["page_number"], question=question, chat_history=chat_history)
                    status = False
                elif data["mode"] == 'interval':
                    answer = chat.chat_with_single_page(url=url, page_number=data["page_number"],  interval=data["interval"], question=question, chat_history=chat_history)
                    status = False
                else:
                    reason = "Please provide  a correct mode"
            else:
                reason = "Please provide a param page_number"

            print(answer)
        except Exception as e:
            reason = "Exception " + str(e)
            print(reason)
    

        if status == False:
            message = "Success"
        else:
            message = "Failure"
        response_data = {
        'guid': 0,
        'answer':answer 
    }
        return jsonify({
            'error': status,
            # 'reason': reason,
            'message': message,
            'status': 200,
            'response_data': response_data
        })
@app.route("/hello", methods=["GET"])
def hello_world():
    return jsonify({
            'status': True,
            'reason': ""
        }) 

if __name__ == "__main__":
    generator = QuestionGenerator()
    chat = ChatWithPDF()
    crawler = PDFURLCrawler()
    app.run(debug=True, host='127.0.0.1', port=8000)
