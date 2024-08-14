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

beer_menu = [
    [InlineKeyboardButton(text="Стаут", callback_data="stout"),
    InlineKeyboardButton(text="Лагер", callback_data="lager")],
    [InlineKeyboardButton(text="Эль", callback_data="ale"),
    InlineKeyboardButton(text="Вайс", callback_data="whish")],
    [InlineKeyboardButton(text="Бланш", callback_data="blanch"),
    InlineKeyboardButton(text="Ипа", callback_data="ipa")],
    [InlineKeyboardButton(text="🔎 Метод производства", callback_data="beer_info")]
]
beer_menu = InlineKeyboardMarkup(inline_keyboard=beer_menu)

stout_menu = [
    [InlineKeyboardButton(text="Guinness ", callback_data="guinness"),
    InlineKeyboardButton(text="Eventide", callback_data="eventide")],
    [InlineKeyboardButton(text="Albion", callback_data="albion"),
    InlineKeyboardButton(text="Ballantine stout", callback_data="ballantine_stout")],
    [InlineKeyboardButton(text="Black sheep", callback_data="black_sheep"),
    InlineKeyboardButton(text="O'Hara's irish Stout Nitro", callback_data="Oharas_stout")],
    [InlineKeyboardButton(text="Fuller's Black Cab stout", callback_data="black_cab"),
    InlineKeyboardButton(text="Belheven Mccallum's", callback_data="belheven")]
    [InlineKeyboardButton(text="Все о наших стаутах", callback_data="stout_info")]
]
stout_menu = InlineKeyboardMarkup(inline_keyboard=stout_menu)