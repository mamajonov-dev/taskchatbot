from aiogram import types
from loader import bot, dp
from aiogram.dispatcher import FSMContext
import aiohttp
import random
from keyboards.default.buttons import generatetypepoll, backbutton, generatemainmenu
from states.botstates import PollState

# хендлер для опроса
@dp.message_handler(text='☑️ Опрос')
async def create_poll(message: types.Message):
    await message.answer('Какой опрос хотите создать? ⬇️', reply_markup=generatetypepoll())
    await PollState.typepoll.set()

# хендлер для принятия тип опроса
@dp.message_handler(state=PollState.typepoll)
async def gettypepoll(message: types.Message, state: FSMContext):
    text = message.text
    if text == 'QUIZ':
        await state.update_data({'typepoll': text})
        await message.answer('Напишите вопрос опроса', reply_markup=backbutton())
        await PollState.question.set()
    elif text == 'REGULAR':
        await state.update_data({'typepoll': text})
        await message.answer('Напишите вопрос опроса', reply_markup=backbutton())
        await PollState.question.set()
    elif text == '⬅️ Назад':
        await message.answer('Выберите категорию ⬇️', reply_markup=generatemainmenu())
        await state.finish()

    else:
        await message.answer('Выберите из вариантов', reply_markup=generatetypepoll())
        await PollState.typepoll.set()

# хендлер для принятия вопрос опроса

@dp.message_handler(state=PollState.question)
async def getquestion(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    if text == '⬅️ Назад':
        await message.answer('Выберите категорию ⬇️', reply_markup=generatemainmenu())
        await state.finish()
    else:
        if data['typepoll'] == 'QUIZ':
            await message.answer('Напишите правильный вариант вопроса', reply_markup=backbutton())
            await state.update_data({'question': text})
            await PollState.correctanswer.set()

        elif data['typepoll'] == 'REGULAR':
            await message.answer(
                'Напишите остальные варианты в таком виде: Например \n\n -ответ\n-ответ\n-ответ  и т.д.',
                reply_markup=backbutton())
            await state.update_data({'question': text})
            await PollState.answers.set()

# хендлер для принятия правильного ответа опроса

@dp.message_handler(state=PollState.correctanswer)
async def getcorrectanswer(message: types.Message, state: FSMContext):
    text = message.text
    if text == '⬅️ Назад':
        await message.answer('Выберите категорию ⬇️', reply_markup=generatemainmenu())
        await state.finish()
    else:
        await message.answer('Напишите остальные варианты в таком виде: Например \n\n -ответ\n-ответ\n-ответ  и т.д.',
                             reply_markup=backbutton())
        await state.update_data({'correctanswer': text})
        await PollState.answers.set()


# хендлер для принятия ответов опроса

@dp.message_handler(state=PollState.answers)
async def getanswer(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    if message.text == '⬅️ Назад':
        await message.answer('Выберите категорию ⬇️', reply_markup=generatemainmenu())
        await state.finish()
    else:
        text = message.text.split('\n')
        await state.update_data({'answers': text})
        data = await state.get_data()
        correctanswer = None
        for key, val in data.items():
            if key == 'correctanswer':
                correctanswer = val
        question = data['question']
        answers = data['answers']
        if correctanswer != None:
            answers.append(correctanswer)
        typepoll = data['typepoll']

        if typepoll == 'QUIZ':
            await bot.send_poll(chat_id, question=question, correct_option_id=correctanswer, options=list(set(answers)),
                                type=types.PollType.QUIZ, reply_markup=generatemainmenu())
        elif typepoll == 'REGULAR':

            await bot.send_poll(chat_id, question=question, options=answers, type=types.PollType.REGULAR,
                                reply_markup=generatemainmenu())
        await state.finish()
