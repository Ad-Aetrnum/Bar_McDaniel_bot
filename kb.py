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
    InlineKeyboardButton(text="Эль", callback_data="ale")],
    [InlineKeyboardButton(text="Лагер", callback_data="lager"),
    InlineKeyboardButton(text="Вайс", callback_data="whish")],
    [InlineKeyboardButton(text="Бланш", callback_data="blanch"),
    InlineKeyboardButton(text="Ипа", callback_data="ipa")],
    [InlineKeyboardButton(text="🔎 Метод производства", callback_data="beer_info")]
]
beer_menu = InlineKeyboardMarkup(inline_keyboard=beer_menu)

stout_menu = [
    [InlineKeyboardButton(text="🇮🇪 Guinness 4,2% 🍺", callback_data="guinness")],
    [InlineKeyboardButton(text="🇮🇪 Eventide 4,5% 🍺", callback_data="eventide")],
    [InlineKeyboardButton(text="🇬🇧 Albion 4,8% 🍺", callback_data="albion")],
    [InlineKeyboardButton(text="🇷🇺 Ballantine stout 4,1% 🍺", callback_data="ballantine_stout")],
    [InlineKeyboardButton(text="🇷🇺 Black sheep 4% 🍺", callback_data="black_sheep")],
    [InlineKeyboardButton(text="🇮🇪 O'Connor Chocolate 4,2% 🍺", callback_data="oconnor")],
    # [InlineKeyboardButton(text="🍾Young's Double Chocolate🍾", callback_data="youngs")],
    # [InlineKeyboardButton(text="🍾O'Hara's Irish Stout Nitro🍾", callback_data="oharas_stout")],
    # [InlineKeyboardButton(text="🍾Fuller's Black Cab stout🍾", callback_data="black_cab")],
    # [InlineKeyboardButton(text="🍾Belheven Mccallum's🍾", callback_data="belheven")],
    # [InlineKeyboardButton(text="🍾Murphy's Stout🍾", callback_data="murpys")],
    [InlineKeyboardButton(text="Все о наших стаутах", callback_data="stout_info")]
]
stout_menu = InlineKeyboardMarkup(inline_keyboard=stout_menu)
#разделить на категории
ale_menu = [
    [InlineKeyboardButton(text="🇧🇪 Affligem blond / blonde ale 6,8% 🍺", callback_data="affligem")],
    [InlineKeyboardButton(text="🇷🇺 Ballantaine ale / amber ale 4,7% 🍺", callback_data="ballantain_ale")],
    [InlineKeyboardButton(text="🇧🇪 Palm / pale ale 5,2% 🍺", callback_data="palm")],
    [InlineKeyboardButton(text="🇬🇧 Theakston PA / pale ale 4,5% 🍺", callback_data="theakston_pa")],
    [InlineKeyboardButton(text="🇮🇪 O'Hara's Irish /red ale 4,3%🍾🍺", callback_data="oharas_red")],
    [InlineKeyboardButton(text="🇮🇪 Brougue /red ale 4,4% 🍺", callback_data="brougue")],
    [InlineKeyboardButton(text="🇷🇺 Queen Grace / red ale 5% 🍺", callback_data="queen_grace")],
    [InlineKeyboardButton(text="🇧🇪 Barby Ruby / fruit ale 6% 🍺", callback_data="barby")],
    [InlineKeyboardButton(text="🇧🇪 D'Atour Brune / brown ale 6,4% 🍺", callback_data="datour")],
    [InlineKeyboardButton(text="🇬🇧 Nog / dark ale 4,6%🍺", callback_data="nog")],
    [InlineKeyboardButton(text="🇬🇧 Theakston XB / bitter 4,2% 🍺", callback_data="theakston_xb")],
    [InlineKeyboardButton(text="🇬🇧 Nelson's /bitter 4,5% 🍺", callback_data="nelsona")],
    # [InlineKeyboardButton(text="🍾Fuller's London pride (amber ale)🍾", callback_data="london_pride")],
    # [InlineKeyboardButton(text="🍾Rodenbach Grand Cru🍾", callback_data="rodenbach")],
    # [InlineKeyboardButton(text="🍾Kilkenny(red ale)🍾", callback_data="kilkenny")],
    [InlineKeyboardButton(text="Все о наших элях", callback_data="ale_info")]
]
ale_menu = InlineKeyboardMarkup(inline_keyboard=ale_menu)