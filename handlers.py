from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

import kb
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    # await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.beer_menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    # await msg.answer(text.menu, reply_markup=kb.menu)
    await msg.answer(text.menu, reply_markup=kb.beer_menu)


@router.callback_query(F.data == "beer")
async def text_of_beer(callback: types.CallbackQuery):
    await callback.message.answer(text.beer, reply_markup=kb.beer_menu)

@router.callback_query(F.data == "stout")
async def text_of_stout(callback: types.CallbackQuery):
    await callback.message.answer(text.stout, reply_markup=kb.stout_menu)

@router.callback_query(F.data == "ale")
async def text_of_ale(callback: types.CallbackQuery):
    await callback.message.answer(text.ale, reply_markup=kb.ale_menu)

@router.callback_query(F.data == "lager")
async def text_of_lager(callback: types.CallbackQuery):
    await callback.message.answer(text.lager, reply_markup=kb.lager_menu)

@router.callback_query(F.data == "ipa")
async def text_of_ipa(callback: types.CallbackQuery):
    await callback.message.answer(text.ipa, reply_markup=kb.ipa_menu)

@router.callback_query(F.data == "weisse")
async def text_of_weisse(callback: types.CallbackQuery):
    await callback.message.answer(text.ipa, reply_markup=kb.weisse_menu)

@router.callback_query(F.data == "cidre")
async def text_of_stout(callback: types.CallbackQuery):
    await callback.message.answer(text.cidre, reply_markup=kb.cidre_menu)



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

