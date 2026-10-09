from pydantic import BaseModel


class CompoundInformation(BaseModel):
    name: str
    formula: str
    molecular_weight: float
    retention_time: float

