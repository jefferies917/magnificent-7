from pydantic import BaseModel


class PlayerResponse(BaseModel):
    first_name: str
    last_name: str
    web_name: str
    goals_scored: int
    assists: int
