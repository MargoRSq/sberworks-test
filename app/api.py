from datetime import datetime

from fastapi import APIRouter, Depends

from elastic_funcs import get_aggregations

router = APIRouter()


async def common_parameters(from_timestamp: int = 0,
                            to_timestamp: int = 0):
    to_timestamp = datetime.now().timestamp()
    return {"from": from_timestamp, "to": to_timestamp}


@router.get('/count')
async def count(commons: dict = Depends(common_parameters)):
    value = get_aggregations(index_name="tindex",
                             from_timestamp=commons['from'],
                             to_timestamp=commons['to'])['count']
    return {"count": value}


@router.get('/max')
async def max(commons: dict = Depends(common_parameters)):
    value = get_aggregations(index_name="tindex",
                             from_timestamp=commons['from'],
                             to_timestamp=commons['to'])['max']
    return {"max": value}


@router.get('/mean')
async def mean(commons: dict = Depends(common_parameters)):
    aggrs = get_aggregations(index_name="tindex",
                             from_timestamp=commons['from'],
                             to_timestamp=commons['to'])
    values_sum = aggrs['sum']
    values_count = aggrs['count']
    if values_count > 0:
        value = values_sum / values_count
    else:
        value = 0
    return {"mean": value}
