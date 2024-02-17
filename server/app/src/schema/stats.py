from fastapi import FastAPI
from pydantic import BaseModel

from datetime import datetime
import uuid
from typing import List

app = FastAPI()

#model representing a question and response for the second page
class QA(BaseModel):
    question: str #question asked by model
    answer: str  #response from child
    ranking: int #1-10
    reasoning: str #reasoning about ranking from chatGPT


class Semantic(BaseModel):
     postive: float
     neutral: float
     negative: float


#stats for the first page (parent)
class FirstPageStats(BaseModel):
    semantics: Semantic
    



#stats for the second page (parent)
class SecondPageStats(BaseModel):
    avg_response_length: float
    unique_words: int
    response_time: int
    q_and_a: List[QA]

    




    
