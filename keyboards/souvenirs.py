from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню сувениров
def get_souvenirs_main_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="РУЧКИ С ЛОГОТИПОМ", callback_data="souvenirs_pens"), 
             InlineKeyboardButton(text="ФУТБОЛКИ", callback_data="souvenirs_tshirts")],
            [InlineKeyboardButton(text="КРУЖКИ", callback_data="souvenirs_mugs")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Ручки
def get_pen_material_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Пластик", callback_data="pen_plastic"), 
             InlineKeyboardButton(text="Металл", callback_data="pen_metal"), 
             InlineKeyboardButton(text="Крафт (картон)", callback_data="pen_craft")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_pen_color_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Синий", callback_data="pen_blue"), 
             InlineKeyboardButton(text="Красный", callback_data="pen_red"), 
             InlineKeyboardButton(text="Черный", callback_data="pen_black")],
            [InlineKeyboardButton(text="Белый", callback_data="pen_white"), 
             InlineKeyboardButton(text="Серебристый", callback_data="pen_silver"), 
             InlineKeyboardButton(text="Золотистый", callback_data="pen_gold")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_pen_application_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Лазерная гравировка", callback_data="pen_laser_engraving"), 
             InlineKeyboardButton(text="УФ-печать", callback_data="pen_uv_print")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Футболки
def get_tshirt_size_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="XS", callback_data="tshirt_xs"), 
             InlineKeyboardButton(text="S", callback_data="tshirt_s"), 
             InlineKeyboardButton(text="M", callback_data="tshirt_m")],
            [InlineKeyboardButton(text="L", callback_data="tshirt_l"), 
             InlineKeyboardButton(text="XL", callback_data="tshirt_xl"), 
             InlineKeyboardButton(text="XXL", callback_data="tshirt_xxl")],
            [InlineKeyboardButton(text="XXXL", callback_data="tshirt_xxxl")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_tshirt_material_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Хлопок 100% (белый)", callback_data="tshirt_cotton_100_white")],
            [InlineKeyboardButton(text="Хлопок 100% (черный)", callback_data="tshirt_cotton_100_black")],
            [InlineKeyboardButton(text="Хлопок 50% / Полиэстер 50% (белый)", callback_data="tshirt_cotton_poly_white")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_tshirt_print_position_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="На груди", callback_data="tshirt_print_chest"), 
             InlineKeyboardButton(text="На спине", callback_data="tshirt_print_back")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Кружки
def get_mug_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Кружка белая", callback_data="mug_white"), 
             InlineKeyboardButton(text="Кружка цветная внутри, цветная ручка", callback_data="mug_colored")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_mug_print_position_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="С одной стороны", callback_data="mug_print_one_side"), 
             InlineKeyboardButton(text="По кругу", callback_data="mug_print_around"), 
             InlineKeyboardButton(text="С двух сторон", callback_data="mug_print_two_sides")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_mug_packaging_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Без упаковки", callback_data="mug_no_packaging"), 
             InlineKeyboardButton(text="Подарочная коробка", callback_data="mug_gift_box")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )