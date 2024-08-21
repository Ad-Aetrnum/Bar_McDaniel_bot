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
    InlineKeyboardButton(text="Бланш и Вайс", callback_data="weisse")],
    [InlineKeyboardButton(text="Ипа", callback_data="ipa"),
    InlineKeyboardButton(text="Крик и Сидр", callback_data="cidre")],
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
    [InlineKeyboardButton(text="🇮🇪 Nocturne Export / porter 6% 🍺", callback_data="nocturne")], 
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
    [InlineKeyboardButton(text="🇧🇪 Monk's cafe / brown ale 5,5% 🍺", callback_data="monks_cafe")],
    [InlineKeyboardButton(text="🇫🇷 D'Atour Brune / brown ale 6,4% 🍺", callback_data="datour")],
    [InlineKeyboardButton(text="🇬🇧 Nog / dark ale 4,6%🍺", callback_data="nog")],
    [InlineKeyboardButton(text="🇬🇧 Theakston XB / bitter 4,2% 🍺", callback_data="theakston_xb")],
    [InlineKeyboardButton(text="🇬🇧 Nelson's /bitter 4,5% 🍺", callback_data="nelsona")],
    # [InlineKeyboardButton(text="🍾Fuller's London pride (amber ale)🍾", callback_data="london_pride")],
    # [InlineKeyboardButton(text="🍾Rodenbach Grand Cru🍾", callback_data="rodenbach")],
    # [InlineKeyboardButton(text="🍾Kilkenny(red ale)🍾", callback_data="kilkenny")],
    [InlineKeyboardButton(text="Все о наших элях", callback_data="ale_info")]
]
ale_menu = InlineKeyboardMarkup(inline_keyboard=ale_menu)

lager_menu = [
    [InlineKeyboardButton(text="🇩🇪 Stanly Cooper 5,2% 🍺", callback_data="stanly_cooper")],
    [InlineKeyboardButton(text="🇩🇪 Bayreuther hell / hell 4,9% 🍺", callback_data="bayreuther")],
    [InlineKeyboardButton(text="🇨🇿 Zubr / pilsner 4,6% 🍺", callback_data="zubr")],
    [InlineKeyboardButton(text="🇷🇺 Buddy lager/ Чешский медведь 4,7% 🍺", callback_data="buddy_lager")],
    [InlineKeyboardButton(text="Все о наших лагерах", callback_data="lager_info")]
]

lager_menu = InlineKeyboardMarkup(inline_keyboard=lager_menu)

ipa_menu = [
    [InlineKeyboardButton(text="🏴󠁧󠁢󠁳󠁣󠁴󠁿Punk IPA 5,6% 🍺", callback_data="punk_ipa")],
    [InlineKeyboardButton(text="🇩🇪 Maisel & Friends 6,3% 🍺", callback_data="maisel_friends")],
    [InlineKeyboardButton(text="Все о наших Ипах", callback_data="ipa_info")]
]

ipa_menu = InlineKeyboardMarkup(inline_keyboard=ipa_menu)

weisse_menu = [
    [InlineKeyboardButton(text="🇧🇪 Steenbruge Blanche 5% 🍺", callback_data="steenbruge_blanche")],
    [InlineKeyboardButton(text="🇩🇪 Maisel Weisse 5,1% 🍺", callback_data="maisel_friends")],
    [InlineKeyboardButton(text="🇷🇺 Buddy Wheat/ Edelweiss 4,9% 🍺", callback_data="buddy_wheat")],
    [InlineKeyboardButton(text="Все о наших мутных", callback_data="weiss_info")]

]

weisse_menu = InlineKeyboardMarkup(inline_keyboard=weisse_menu)

cidre_menu = [
    [InlineKeyboardButton(text="🇧🇾 Royal Cidre Apple / semi-dri 5% 🍺", callback_data="royal_apple")],
    [InlineKeyboardButton(text="🇧🇾 Roayal Cidre Pear/ semi-sweet 5% 🍺", callback_data="royal_pear")],
    [InlineKeyboardButton(text="🇧🇪 Boon Kriek 4% 🍺", callback_data="boon_kriek")],
    [InlineKeyboardButton(text="🇧🇪 St. Louis 4% 🍺", callback_data="st.louis")],
    [InlineKeyboardButton(text="Все о наших фруктовых", callback_data="cidre_info")]

]

cidre_menu = InlineKeyboardMarkup(inline_keyboard=cidre_menu)