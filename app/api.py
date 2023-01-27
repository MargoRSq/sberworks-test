from datetime import datetime

from fastapi import APIRouter, Depends

from elastic_funcs import count_fileds

router = APIRouter()


async def common_parameters(from_timestamp: int = 0,
                            to_timestamp: int = 0):
    to_timestamp = datetime.now().timestamp()
    return {"from": from_timestamp, "to": to_timestamp}


@router.get('/count')
async def count(commons: dict = Depends(common_parameters)):
    return {"count": count_fileds(index_name="tindex",
                                  from_timestamp=commons['from'],
                                  to_timestamp=commons['to'])}
