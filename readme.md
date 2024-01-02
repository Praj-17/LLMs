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
    
    


