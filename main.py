from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from nic_analyzer import generate_dashboard_data

app = FastAPI(title="Financial Insight LLM API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class user_data(BaseModel):
    net_income_monthly: float = 30000
    needs_food: float = 5000
    needs_housing: float = 7000
    needs_transport: float = 2000
    needs_utilities: float = 1500
    needs_insurance: float = 800
    needs_debt: float = 3000
    wants_misc: Optional[float] = 0.0  # optional

@app.post("/Financial_Insight")
def financial_insight(data: user_data):
    params = data.dict()
    result = generate_dashboard_data(params)
    return result

