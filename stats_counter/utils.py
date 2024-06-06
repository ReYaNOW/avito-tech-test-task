from faker import Faker

from stats_counter.statistics.schemas import StatisticCreate


def generate_data(amount):
    fake = Faker()

    new_data = []
    for _ in range(amount):
        data = StatisticCreate(
            date=fake.date_between(start_date='-1y', end_date='today'),
            views=fake.random_int(min=50, max=200),
            clicks=fake.random_int(min=5, max=20),
            cost=fake.pydecimal(left_digits=4, right_digits=2, positive=True),
        )
        new_data.append(data.dict())
    return new_data
