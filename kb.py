from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="Пиво", callback_data="beer"),
    InlineKeyboardButton(text="Виски", callback_data="whisky")],
    [InlineKeyboardButton(text="Джин", callback_data="gin"),
    InlineKeyboardButton(text="Ром", callback_data="rum")],
    [InlineKeyboardButton(text="Водка", callback_data="vodka"),
    InlineKeyboardButton(text="текила", callback_data="tequila")],
    [InlineKeyboardButton(text="🔎 Поиск", callback_data="search")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])