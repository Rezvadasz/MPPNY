from pydantic import BaseModel


class Cpu(BaseModel):
    model: str
    PTS1: float
    PTS2: float
    PTS4: float
    PTS8: float
    PTS64: float
    samples: int