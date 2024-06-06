from sqlalchemy import Column, Integer, Date, Numeric, Computed
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Statistic(Base):
    __tablename__ = 'statistic'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    views = Column(Integer)
    clicks = Column(Integer)
    cost = Column(Numeric(15, 6))
    cpc = Column(Numeric(15, 3), Computed('cost / NULLIF(clicks, 0)'))
    cpm = Column(Numeric(15, 3), Computed('cost / NULLIF(views, 0) * 1000'))
