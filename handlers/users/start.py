from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.buttons import generatemainmenu
from loader import dp
from aiogram.dispatcher import FSMContext

@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=generatemainmenu())

    await state.finish()


#
#
# # Функция для создания опрос
