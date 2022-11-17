import logging

from fastapi import APIRouter

from schemas.win_loss_deposit import DepositResponse
from cruds import win_loss_deposit

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get('/deposits', response_model=DepositResponse)
async def read_deposits(league_kbn: int = None, term: int = None):
    result = await win_loss_deposit.get_list(league_kbn, term)
    return result
