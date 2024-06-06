from decimal import Decimal
from datetime import date
from enum import Enum

from pydantic import BaseModel


class StatisticCreate(BaseModel):
    date: date
    views: int | None = None
    clicks: int | None = None
    cost: Decimal | None = None


class StatisticList(BaseModel):
    id: int
    date: date
    views: int | None
    clicks: int | None
    cost: Decimal | None
    cpc: Decimal | None
    cpm: Decimal | None

    class Config:
        from_attributes = True


class OrderByEnum(str, Enum):
    id = 'id'
    date = 'date'
    views = 'views'
    clicks = 'clicks'
    cost = 'cost'
    cpc = 'cpc'
    cpm = 'cpm'
