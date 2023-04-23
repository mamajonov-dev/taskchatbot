from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from functions.getweatherinfo import getweatherinfo
from states.botstates import WeatherCityState
from keyboards.default.buttons import backbutton, generatemainmenu


# хендлер для погоды
@dp.message_handler(text=['⛅️ Погода'])
async def getcityname(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Напишите название города ⬇️', reply_markup=backbutton())
    await WeatherCityState.cityname.set()

# хендлер для принимания название города и отпровки информации погоды
@dp.message_handler(state=WeatherCityState.cityname)
async def sendweatherinfo(message: Message, state: FSMContext):
    if message.text == '⬅️ Назад':
        await message.answer('Выберите категорию ⬇️', reply_markup=generatemainmenu())
        await state.finish()
    else:
        try:
            await state.update_data({'cityname': message.text})
            data = await state.get_data()
            city = data['cityname']
            info = getweatherinfo(city)
            await message.answer_photo(photo=info[1], caption=info[0], reply_markup=backbutton())
            await message.answer('Напишите название города ⬇️')
        except:
            await message.answer('Город не найден')
            await message.answer('Напишите название города ⬇️')



