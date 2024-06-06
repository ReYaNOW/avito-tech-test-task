from datetime import date

from fastapi import APIRouter, Depends, Query
from sqlalchemy import insert, select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from stats_counter.database import get_async_session
from stats_counter.statistics.models import Statistic
from stats_counter.statistics.schemas import (
    StatisticCreate,
    StatisticList,
    OrderByEnum,
)

router = APIRouter(prefix='/statistics', tags=['Statistic'])


@router.get(
    '/',
    summary='Get statistics from date range',
    response_model=list[StatisticList],
)
async def get_specific_statistic(
    from_: date | None = Query(None, alias="from"),
    to: date = None,
    order_by: OrderByEnum = 'date',
    session: AsyncSession = Depends(get_async_session),
):
    query = select(Statistic)
    if from_:
        query = query.where(Statistic.date >= from_)
    if to:
        query = query.where(Statistic.date <= to)

    result = await session.execute(
        query.order_by(Statistic.__table__.columns[order_by])
    )
    return result.scalars().all()


@router.post('/', summary='Add statistic')
async def add_statistic(
    new_statistic: StatisticCreate,
    session: AsyncSession = Depends(get_async_session),
):
    stmt = insert(Statistic).values(**new_statistic.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}


@router.delete('/', summary='Remove all statistics')
async def remove_all_statistics(
    session: AsyncSession = Depends(get_async_session),
):
    stmt = delete(Statistic)
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}
