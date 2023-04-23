from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from functions.getrandompicture import getcuteanimals
from states.botstates import AnimalsPicture
from keyboards.default.buttons import backbutton, generatemainmenu, animalsbutton

# хендлер для картинки животных

@dp.message_handler(text='🖼️ Милые животные')
async def getresponse(message: Message, state: FSMContext):
    await message.answer('Чтобы получить картинку, нажмите кнопку ниже ⬇️', reply_markup=animalsbutton())
    await AnimalsPicture.animal.set()

# хендлер для отправки картинки животных

@dp.message_handler(state=AnimalsPicture.animal)
async def sendpicture(message: Message, state: FSMContext):
    text = message.text

    if text == '🖼️ Картинки':
        image = getcuteanimals()

        await message.answer_photo(image, 'Чтобы получить картинку, нажмите кнопку ниже ⬇',
                                   reply_markup=animalsbutton())
        await AnimalsPicture.animal.set()
    elif text == '⬅️ Назад':

        await message.answer('Выберите категорию ⬇️', reply_markup=generatemainmenu())
        await state.finish()
