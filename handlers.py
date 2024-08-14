from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

import kb
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == "beer")
async def text_of_beer(callback: types.CallbackQuery):
    await callback.message.answer(text.beer)

@router.callback_query(F.data == "whisky")
async def text_of_whisky(callback: types.CallbackQuery):
    await callback.message.answer(text.whisky)

@router.callback_query(F.data == "gin")
async def text_of_gin(callback: types.CallbackQuery):
    await callback.message.answer(text.gin)

@router.callback_query(F.data == "vodka")
async def text_of_vodka(callback: types.CallbackQuery):
    await callback.message.answer(text.vodka)

@router.callback_query(F.data == "tequila")
async def text_of_tequila(callback: types.CallbackQuery):
    await callback.message.answer(text.tequila)

@router.callback_query(F.data == "rum")
async def text_of_rum(callback: types.CallbackQuery):
    await callback.message.answer(text.rum)

@router.callback_query(F.data == "search")
async def text_of_search(callback: types.CallbackQuery):
    await callback.message.answer(text.search)

