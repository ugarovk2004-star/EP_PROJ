from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню интерьерной печати
def get_interior_main_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="ПЛАКАТЫ", callback_data="interior_posters"), 
             InlineKeyboardButton(text="ТАБЛИЧКИ", callback_data="interior_signs")],
            [InlineKeyboardButton(text="КАРТИНЫ НА ХОЛСТЕ", callback_data="interior_canvas"), 
             InlineKeyboardButton(text="ПЕЧАТЬ НА БАННЕРЕ", callback_data="interior_banner")],
            [InlineKeyboardButton(text="ПЕЧАТЬ НА САМОКЛЕЮЩЕЙСЯ ПЛЁНКЕ", callback_data="interior_sticker_film")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Таблички
def get_sign_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Офисные таблички", callback_data="sign_office"), 
             InlineKeyboardButton(text="Уличные таблички", callback_data="sign_outdoor")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_sign_material_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Пластик ПВХ-3 мм", callback_data="sign_pvc_3mm"), 
             InlineKeyboardButton(text="Пластик ПВХ-5 мм", callback_data="sign_pvc_5mm")],
            [InlineKeyboardButton(text="Двухслойный пластик", callback_data="sign_two_layer")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Картины на холсте
def get_canvas_size_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="20×30 см", callback_data="canvas_20x30"), 
             InlineKeyboardButton(text="30×40 см", callback_data="canvas_30x40")],
            [InlineKeyboardButton(text="40×50 см", callback_data="canvas_40x50"), 
             InlineKeyboardButton(text="40×60 см", callback_data="canvas_40x60")],
            [InlineKeyboardButton(text="50×50 см", callback_data="canvas_50x50"), 
             InlineKeyboardButton(text="50×70 см", callback_data="canvas_50x70")],
            [InlineKeyboardButton(text="60×80 см", callback_data="canvas_60x80"), 
             InlineKeyboardButton(text="70×100 см", callback_data="canvas_70x100")],
            [InlineKeyboardButton(text="80×120 см", callback_data="canvas_80x120")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_canvas_framing_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Без подрамника", callback_data="canvas_no_frame"), 
             InlineKeyboardButton(text="Галерейная натяжка", callback_data="canvas_gallery_stretch")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Печать на баннере
def get_banner_print_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Широкоформатная", callback_data="banner_wide_format"), 
             InlineKeyboardButton(text="Интерьерная", callback_data="banner_interior")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_banner_edge_processing_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Без обработки", callback_data="banner_no_edge"), 
             InlineKeyboardButton(text="Укрепление края", callback_data="banner_edge_reinforcement")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_banner_grommets_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Без люверсов", callback_data="banner_no_grommets"), 
             InlineKeyboardButton(text="Люверсы через 30 см", callback_data="banner_grommets_30cm")],
            [InlineKeyboardButton(text="Люверсы через 50 см", callback_data="banner_grommets_50cm")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Печать на самоклейке
def get_interior_sticker_film_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Пленка белая мат.", callback_data="interior_film_white_matte"), 
             InlineKeyboardButton(text="Пленка белая гл.", callback_data="interior_film_white_glossy")],
            [InlineKeyboardButton(text="Пленка прозрач. мат.", callback_data="interior_film_clear_matte"), 
             InlineKeyboardButton(text="Пленка прозрач. гл.", callback_data="interior_film_clear_glossy")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_interior_sticker_processing_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Без обработки", callback_data="interior_no_processing"), 
             InlineKeyboardButton(text="Ламинация", callback_data="interior_lamination")],
            [InlineKeyboardButton(text="Подрезка напечатанного макета", callback_data="interior_cutting"), 
             InlineKeyboardButton(text="Плоттерная резка", callback_data="interior_plotter_cut")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )