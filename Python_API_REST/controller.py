from fastapi import FastAPI
from pydantic import BaseModel
from domain import CompoundInformation
from service import Service

app = FastAPI()


@app.post("/Rt_Prediction/")
def predict_retention_time(data: CompoundInformation):
    data.retention_time = Service().rt_prediction(data).retention_time
    return data
