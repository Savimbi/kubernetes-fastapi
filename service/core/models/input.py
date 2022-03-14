from turtle import title
from pydantic import BaseModel, Field


class MessageInput(BaseModel):
    message1: str = Field(..., title="Greating")
    message2: str = Field(..., title="Calculation results")
    n: int = Field(..., title="n: a large int")
    largest_prime_factor: int = Field(..., title="Largest prime factor of n")
    elapsed_time: float = Field(..., title="Calculation time (seconds)")
