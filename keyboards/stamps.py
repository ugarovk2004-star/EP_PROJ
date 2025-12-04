from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_stamps_main_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="АВТОМАТИЧЕСКАЯ ПЕЧАТЬ", callback_data="stamp_auto"), 
             InlineKeyboardButton(text="КАРМАННАЯ ПЕЧАТЬ", callback_data="stamp_pocket")],
            [InlineKeyboardButton(text="ФАКСИМИЛЕ", callback_data="stamp_facsimile"), 
             InlineKeyboardButton(text="КЛИШЕ БЕЗ ОСНАСТКИ", callback_data="stamp_cliche")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# def get_stamp_type_keyboard():
#     return InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton(text="Автоматическая печать", callback_data="stamp_auto"), 
#              InlineKeyboardButton(text="Карманная печать", callback_data="stamp_pocket")],
#             [InlineKeyboardButton(text="Факсимиле", callback_data="stamp_facsimile"), 
#              InlineKeyboardButton(text="Клише без оснастки", callback_data="stamp_cliche")],
#             [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
#              InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
#         ]
#     )

def get_stamp_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Круглая 30 мм", callback_data="stamp_round_30"), 
             InlineKeyboardButton(text="Круглая 40 мм", callback_data="stamp_round_40")],
            [InlineKeyboardButton(text="Прямоугольный штамп", callback_data="stamp_rectangular")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_stamp_ink_color_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Черный", callback_data="stamp_ink_black"), 
             InlineKeyboardButton(text="Фиолетовый", callback_data="stamp_ink_purple")],
            [InlineKeyboardButton(text="Красный", callback_data="stamp_ink_red"), 
             InlineKeyboardButton(text="Зелёный", callback_data="stamp_ink_green")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )