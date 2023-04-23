from aiogram.dispatcher.filters.state import State, StatesGroup


# state для погоды
class WeatherCityState(StatesGroup):
    cityname = State()


# state для конвертации валют
class ConvertState(StatesGroup):
    from_val = State()
    amount = State()
    to_val = State()


# state для картинки животных
class AnimalsPicture(StatesGroup):
    animal = State()


# state для опроса
class PollState(StatesGroup):
    typepoll = State()
    question = State()
    correctanswer = State()
    answers = State()
