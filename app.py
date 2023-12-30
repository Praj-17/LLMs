from fastapi import FastAPI, HTTPException
from question_generator import QuestionGenerator
from pydantic import BaseModel, Optional
from enum import Enum
from fastapi.responses import JSONResponse


class StatusEnum(str, Enum):
    CHOICE1 = "all"
    CHOICE2 = "single"
    CHOICE3 = "interval"

app = FastAPI()
global generator 
generator = QuestionGenerator()

class InputData(BaseModel):
    # Define the input data model using Pydantic
    mode: str
    url : str
    num_questions :str
    page_number: Optional[int] = None
    interval:  Optional[int] = 1

def generate_functions(input_data: InputData):
    status = False
    reason = ""
    questions = []
    try:
        questions = generator.generate_mcq_questions_all_text(url=input_data.url, n =input_data.num_questions )
        status = True
        
    except Exception as e:
        reason = "Exception" + str(e)
    return status, reason,questions


@app.post("/get_mcq_questions", response_model=dict)
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
        if input_data.page_number:
            if input_data.mode == 'single':
                
                    questions = generator.generate_mcq_questions_single_page(url=url, page_number=input_data.page_number, n = num)
                    status = True
                   
            elif input_data.mode == 'interval':
                    questions = generator.generate_mcq_questions_page_interval(url = url, page_number=input_data.page_number, n= num)
                    status = True
        else:
            reason = "Please provide a param page_number"


        # return result
    except HTTPException as e:
        reason = "Exception" + str(e.detail)
        # return {"error": e.detail}
    except Exception as e:
        reason = "Exception" + str(e)
        # return {"error": str(e)}
    return JSONResponse({
         'status':status,
         'reason': reason,
         'questions': questions
    })

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
