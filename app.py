from fastapi import FastAPI, HTTPException
from question_generator import QuestionGenerator
from pydantic import BaseModel
from typing import Union
from enum import Enum
from fastapi.responses import JSONResponse


class Modes(str, Enum):
    CHOICE1 = "all"
    CHOICE2 = "single"
    CHOICE3 = "interval"

class status(str, Enum):
    CHOICE1 = True
    CHOICE2 = False

app = FastAPI()
global generator 

class ReturnType(BaseModel):
     status:status 
     reason: str
     questions: list


class InputData(BaseModel):
    # Define the input data model using Pydantic
    mode: Modes
    url : str
    num_questions :str
    page_number: Union[int, None] = None
    interval:  Union[int, None] = 1

# def generate_functions(input_data: InputData):
#     status = False
#     reason = ""
#     questions = []
#     try:
#         questions = generator.generate_mcq_questions_all_text(url=input_data.url, n =input_data.num_questions )
#         status = True
        
#     except Exception as e:
#         reason = "Exception" + str(e)
#     return status, reason,questions


@app.post("/get_mcq_questions")
async def run_function(input_data: InputData):
    questions = []
    status = False
    reason = ""
    url = input_data.url
    num = input_data.num_questions


    try:
        if input_data.mode == 'all':
            questions = generator.generate_mcq_questions_all_text(url=url, n = num)
            status  =  True
        elif input_data.page_number:
            if input_data.mode == 'single':
                
                    questions = generator.generate_mcq_questions_single_page(url=url, page_number=input_data.page_number, n = num)
                    status = True
                   
            elif input_data.mode == 'interval':
                    questions = generator.generate_mcq_questions_page_interval(url = url, page_number=input_data.page_number, n= num, interval = input_data.interval)
                    status = True
        else:
            reason = "Please provide a param page_number"

        print(questions)

        # return result
    except HTTPException as e:
        reason = "Exception " + str(e.detail)
        # return {"error": e.detail}
    except Exception as e:
        reason = "Exception " + str(e)
        # return {"error": str(e)}
    return JSONResponse({
         'status':status,
         'reason': reason,
         'questions': questions
    })

if __name__ == "__main__":
    import uvicorn
    generator = QuestionGenerator()
    uvicorn.run(app, host="127.0.0.1", port=8000)
