from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from functions.convertorvalut import get_currency, getcurrencysmybols
from states.botstates import ConvertState
from keyboards.default.buttons import backbutton, generatemainmenu



# Обработчик текстовых сообщений для конвертации валют
@dp.message_handler(text='💰 Конвертер валют')
async def getfromvalut(message: Message):
    data = getcurrencysmybols()
    data = data['symbols']
    text = ''
    for k, v in data.items():
        text += f'{k} - {v}\n'
    await message.answer(f'Напишите название валюты, которое откуда конвертировать\n{text}', reply_markup=backbutton())
    await message.answer('Напишите название валюты, которое откуда конвертировать. Например: USD')

    await ConvertState.from_val.set() #

# хендлер, который ловить state ConvertState.from_val
@dp.message_handler(state=ConvertState.from_val)
async def getfromvalut(message: Message, state: FSMContext):
    chat_id = message.chat.id
    text = message.text
    data = getcurrencysmybols()
    data = data['symbols']
    fromvalut = None
    for k in data.keys():
        if text.upper() == k:
            fromvalut = k
    if text.upper() == fromvalut:
        await state.update_data({'fromvalut': fromvalut.upper()})
        await bot.send_message(chat_id, 'Введите сумму в цифрах', reply_markup=backbutton())
        await ConvertState.amount.set()
    elif text == '⬅️ Назад':
        await message.answer('Главное меню. Выберите категорию ⬇️', reply_markup=generatemainmenu())
        await state.finish()
    else:
        await message.answer(
            '❌ Неопознанная валюта. Выбирайте из вариантов. Напишите только название валюты. Например: USD')
        await ConvertState.from_val.set()


# хендлер, который ловить state ConvertState.amount
@dp.message_handler(state=ConvertState.amount)
async def getamount(message: Message, state: FSMContext):
    amount = message.text
    if amount.isdigit():
        await state.update_data({'amount': amount})
        await message.answer('Напишите название валюты, которое куда конвертировать. Например: RUB', reply_markup=backbutton())
        await ConvertState.to_val.set()
    elif message.text == '⬅️ Назад':
        await message.answer('Главное меню. Выберите категорию ⬇️', reply_markup=generatemainmenu())
        await state.finish()
    else:
        await message.answer('Введите сумму только в цифрах без пробелов')
        await ConvertState.amount.set()

# хендлер, который ловить state ConvertState.to_val

@dp.message_handler(state=ConvertState.to_val)
async def gettovalut(message: Message, state: FSMContext):
    chat_id = message.chat.id
    text = message.text
    data = getcurrencysmybols()
    data = data['symbols']
    to_valut = None
    for k in data.keys():
        if text.upper() == k:
            to_valut = k
    if text.upper() == to_valut:
        await state.update_data({'tovalut': to_valut})
        data = await state.get_data()
        from_val = data['fromvalut']
        amount = data['amount']
        to_val = data['tovalut']
        await bot.send_message(chat_id, get_currency(from_val, to_val, amount), reply_markup=generatemainmenu())
        await state.finish()
    elif text == '⬅️ Назад':
        await message.answer('Главное меню. Выберите категорию ⬇️', reply_markup=generatemainmenu())
        await state.finish()
    else:
        await message.answer(
            '❌ Неопознанная валюта. Выбирайте из вариантов. Напишите только название валюты. Например: USD')
        await ConvertState.to_val.set()




