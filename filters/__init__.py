from loader import dp
from .isPrivate import IsPrivate


if __name__ == "filters":
    dp.filters_factory.bind(IsPrivate)

