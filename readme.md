# Application Documentation

## Setup

1. Install Python==3.9.0 (Prefferably)
2. Install requirements (by navigating to the folder)
```
    pip install -r requirements.text
```

3. run the app
```
    python app.py
```

HOST 
`http://127.0.0.1:8000` (localhost)

## Question Generation

endpoint = `/get_mcq_questions`

### Input Parameters 

1. mode = `['all', 'single', 'interval']` Any one of these 

    a.`all`: When you want to extract entire text from a PDF 
    b. `single`: When you want to extract text from a single page  
    c. `interval`: When you want to extract +-n pages from a target page

2. url = A string of `public` url for a PDF file hosted on a google drive  
3. num_questions = Number of questions you want to be created  
4. page_number  = Specific to `single` and `interval` format, specifies target page  
5. interval = Specific to `interval` formatm specifies target interval  

#### input parameters
```
{
    "url": "https://drive.google.com/file/d/1TGEgTeDQAS2NyS36_KXv1ZyIcA0tFTvr/view?usp=drive_link",
    "num_questions": 5,
    "mode": "interval",
    "page_number": 2,
    "interval":2
}
```

#### Output format

```
{
    "status": true,
    "reason": "",
    "questions": [
        {
            "question": "What is the first step in urine formation?",
            "options": [
                "Reabsorption",
                "Secretion",
                "Glomerular filtration",
                "Ultra filtration"
            ],
            "answer": "Glomerular filtration"
        },
        {
            "question": "What is the average amount of blood filtered by the kidneys per minute?",
            "options": [
                "500-600 ml",
                "700-800 ml",
                "900-1000 ml",
                "1100-1200 ml"
            ],
            "answer": "1100-1200 ml"
        },
        {
            "question": "Which type of nephron has a loop of Henle that runs deep into the medulla?",
            "options": [
                "Cortical nephrons",
                "Juxta medullary nephrons",
                "Glomerular nephrons",
                "Peritubular nephrons"
            ],
            "answer": "Juxta medullary nephrons"
        },
        {
            "question": "What are the major forms of nitrogenous wastes excreted by animals?",
            "options": [
                "Ammonia, urea, and uric acid",
                "Carbon dioxide, water, and ions",
                "Proteins, fats, and carbohydrates",
                "Sodium, potassium, and chloride"
            ],
            "answer": "Ammonia, urea, and uric acid"
        },
        {
            "question": "What is the excretory structure in Platyhelminthes, rotifers, some annelids and the cephalochordate – Amphioxus?",
            "options": [
                "Nephridia",
                "Malpighian tubules",
                "Protonephridia or flame cells",
                "Antennal glands"
            ],
            "answer": "Protonephridia or flame cells"
        }
    ]
}
```
## Chat With PDF

endpoint = `/chat`

### Input Parameters 

1. mode = `['all', 'single', 'interval']` Any one of these 

    a.`all`: When you want to extract entire text from a PDF 
    b. `single`: When you want to extract text from a single page  
    c. `interval`: When you want to extract +-n pages from a target page

2. url = A string of `public` url for a PDF file hosted on a google drive  
3. question = quetion asked by user 
4. page_number  = Specific to `single` and `interval` format, specifies target page  
5. interval = Specific to `interval` formatm specifies target interval  
6. chat_history = A list of tuples with question answer pairs 

#### input parameters
```
{
    "url": "https://ncert.nic.in/textbook/pdf/kebo116.pdf",
    "question": "what is this page about",
    "mode": "interval",
    "page_number": 2,
    "interval":2,
    "chat_history": [(question, answer), (question, answer)]
}
```

#### Output format

```
{
    "error": false,
    "message": "Success",
    "reason": "Exception name 'questions' is not defined",
    "response_data": {
        "answer": "This page is primarily about the functions and structures of the kidney, with a focus on the processes of filtration, reabsorption, and secretion. It details how the glomerulus filters blood and forms filtrate in the Bowman’s capsule, and how reabsorption of the filtrate takes place in different parts of the nephrons. It also discusses the role of the juxta glomerular apparatus (JGA) in regulating the Glomerular Filtration Rate (GFR). The page further explains the process of dialysis and kidney transplantation as methods for treating kidney failure. It also defines certain kidney conditions such as renal calculi and glomerulonephritis. The page includes a detailed explanation of the function of the tubules, including the Proximal Convoluted Tubule (PCT), Henle’s Loop, Distal Convoluted Tubule (DCT), and Collecting Duct. It also discusses the mechanism of concentration of the filtrate, particularly the role of Henle’s loop and vasa recta in producing a concentrated urine. Lastly, the page includes exercises and questions for further understanding of the topic.",
        "guid": 0
    },
    "status": 200
}
```
    



