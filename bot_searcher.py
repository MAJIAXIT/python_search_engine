import os
from searcher.main import *
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from config import bot_token
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=storage)


class States(StatesGroup):
    waiting_for_directory = State()
    waiting_for_query = State()
    waiting_for_search_type = State()


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    """React on command /start"""
    await message.answer("Hello!\nEnter some command.")


@dp.message_handler(commands=["directories"])
async def directories_command(message: types.Message):
    """React on command /directories"""
    answer = ''
    directories = os.listdir('directories')
    for directory in directories:
        answer += f'`{directory}`\n\n'
    if answer == '':
        answer = 'Directories folder is empty'
    await message.answer(answer, parse_mode=types.ParseMode.MARKDOWN)


@dp.message_handler(commands=["search"], state=None)
async def search_command(message: types.Message):
    """React on command /search"""
    """Request a catalog for search"""
    string = ''
    directories = os.listdir('directories')
    for directory in directories:
        string += f'`{directory}`\n\n'
    if string == '':
        string = 'Directories folder is empty'

    await message.answer('Enter the directory to search:\n' + string, parse_mode=types.ParseMode.MARKDOWN)
    await States.waiting_for_directory.set()


@dp.message_handler(state=States.waiting_for_directory)
async def input_directory(message: types.Message, state: FSMContext):
    """Request a querry for search"""
    directory = message.text

    await state.update_data(directory=directory)

    if directory in os.listdir('directories'):
        await message.answer('Enter the search query.')
        await States.next()
    else:
        await message.answer('There is no such directory.')


@dp.message_handler(state=States.waiting_for_query)
async def input_directory(message: types.Message, state: FSMContext):
    """Request a search type for search"""
    query = message.text

    await state.update_data(query=query)

    await message.answer('Enter the search type (`and`, `or`).', parse_mode=types.ParseMode.MARKDOWN)

    await States.next()


@dp.message_handler(state=States.waiting_for_search_type)
async def input_directory(message: types.Message, state: FSMContext):
    """Show the search results"""
    await message.answer('Searching...', reply=False)

    data = await state.get_data()
    directory = data['directory']
    query = data['query']
    search_type = message.text

    if '&' in query:
        search_type = 'and'
    if '|' in query:
        search_type = 'or'

    answer = search_on_directory(directory, query, search_type)

    reply_text = ''
    if len(answer) > 1:
        for page in answer:
            reply_text += page + '\n'
    else:
        reply_text = str(answer[0]) + '\nNo search results'

    if len(reply_text) > 4096:
        for x in range(0, len(reply_text), 4096):
            await message.answer(reply_text[x:x+4096], reply=False)
    else:
        await message.answer(reply_text, reply=False)

    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp)
