from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_photo_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="10×15", callback_data="photo_10x15"), 
             InlineKeyboardButton(text="15×21", callback_data="photo_15x21"), 
             InlineKeyboardButton(text="21×30", callback_data="photo_21x30")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_photo_print_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="С полями (изображение полностью, возможны белые поля)", 
                                  callback_data="photo_with_margins")],
            [InlineKeyboardButton(text="Без полей (изображение займёт всю площадь, возможна обрезка краёв)", 
                                  callback_data="photo_without_margins")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )