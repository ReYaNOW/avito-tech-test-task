from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from stats_counter.database import get_async_session
from stats_counter.statistics.models import Statistic
from stats_counter.statistics.router import router
from stats_counter.utils import generate_data

app = FastAPI(title='Statistic counter')

app.include_router(router)


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')


@app.post(
    '/fill_db', summary='Fill database with random data', tags=['Testing']
)
async def fill_db(
    amount: int,
    session: AsyncSession = Depends(get_async_session),
):
    new_data = generate_data(amount)

    stmt = insert(Statistic).values(new_data)
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}
