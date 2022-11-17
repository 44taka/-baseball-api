from datetime import date
from typing import List

from pydantic import BaseModel


class WinLossDeposit(BaseModel):
    id: int
    date: date
    deposit: int
    team_id: int


class DepositDataResponse(BaseModel):
    team_id: int
    team_name: str
    team_color_cd: str
    result: List[int]


class DepositResponse(BaseModel):
    labels: List[date]
    data: List[DepositDataResponse]

