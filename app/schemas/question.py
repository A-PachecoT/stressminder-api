from datetime import datetime
from typing import Annotated, List

from pydantic import BaseModel, Field, conint
from pydantic.types import conint


class QuestionResponse(BaseModel):
    question_number: Annotated[int, conint(ge=1, le=10)] = Field(
        ..., description="Question number (1-10)"
    )
    answer_value: Annotated[int, conint(ge=0, le=4)] = Field(
        ..., description="Answer value (0-4: nunca-siempre)"
    )


class QuestionResponseCreate(QuestionResponse):
    pass


class QuestionResponseDB(QuestionResponse):
    id: int
    user_id: int
    timestamp: datetime

    class Config:
        from_attributes = True


class PSS10Result(BaseModel):
    total_score: int = Field(..., description="Total PSS-10 score")
    stress_level: str = Field(..., description="Stress level interpretation")
    timestamp: datetime
