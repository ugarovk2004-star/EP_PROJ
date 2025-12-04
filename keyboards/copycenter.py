from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Ч/Б печать
def get_bw_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A4", callback_data="bw_a4"), 
             InlineKeyboardButton(text="A3", callback_data="bw_a3")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_bw_print_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Односторонняя", callback_data="bw_single"), 
             InlineKeyboardButton(text="Двусторонняя", callback_data="bw_double")],
            [InlineKeyboardButton(text="Печать брошюры", callback_data="bw_booklet")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_bw_additional_services_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Брошюровка на металлическую пружину", callback_data="bw_spring")],
            [InlineKeyboardButton(text="Пластиковые обложки", callback_data="bw_plastic_covers")],
            [InlineKeyboardButton(text="Скрепление брошюры", callback_data="bw_stapling")],
            [InlineKeyboardButton(text="Пропустить", callback_data="bw_skip_services")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Цветная печать
def get_color_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A7 (74×105 мм)", callback_data="color_a7"), 
             InlineKeyboardButton(text="A6 (105×148 мм)", callback_data="color_a6")],
            [InlineKeyboardButton(text="Евроформат (210×99 мм)", callback_data="color_euro"), 
             InlineKeyboardButton(text="A5 (148×210 мм)", callback_data="color_a5")],
            [InlineKeyboardButton(text="A4 (210×297 мм)", callback_data="color_a4"), 
             InlineKeyboardButton(text="A3 (297×420 мм)", callback_data="color_a3")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_color_paper_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Офсетная 80 г/м²", callback_data="color_offset_80")],
            [InlineKeyboardButton(text="Мелованная 115 г/м²", callback_data="color_coated_115"), 
             InlineKeyboardButton(text="Мелованная 130 г/м²", callback_data="color_coated_130")],
            [InlineKeyboardButton(text="Мелованная 170 г/м²", callback_data="color_coated_170"), 
             InlineKeyboardButton(text="Мелованная 250 г/м²", callback_data="color_coated_250")],
            [InlineKeyboardButton(text="Мелованная 300 г/м²", callback_data="color_coated_300")],
            [InlineKeyboardButton(text="Пленка белая мат.", callback_data="color_film_white_matte"), 
             InlineKeyboardButton(text="Пленка белая гл.", callback_data="color_film_white_glossy")],
            [InlineKeyboardButton(text="Пленка прозрач. мат.", callback_data="color_film_clear_matte"), 
             InlineKeyboardButton(text="Пленка прозрач. гл.", callback_data="color_film_clear_glossy")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_color_additional_services_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Брошюровка на металлическую пружину", callback_data="color_spring")],
            [InlineKeyboardButton(text="Пластиковые обложки", callback_data="color_plastic_covers")],
            [InlineKeyboardButton(text="Скрепление брошюры", callback_data="color_stapling")],
            [InlineKeyboardButton(text="Подрезка", callback_data="color_cutting")],
            [InlineKeyboardButton(text="Пропустить", callback_data="color_skip_services")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Главное меню копицентра (обновленное)
def get_copycenter_main_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Ч/Б ПЕЧАТЬ", callback_data="bw_print"), 
             InlineKeyboardButton(text="ЦВЕТНАЯ ПЕЧАТЬ", callback_data="color_print")],
            [InlineKeyboardButton(text="РИЗОГРАФ", callback_data="risograph")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Ризограф
def get_risograph_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A4", callback_data="riso_a4"), 
             InlineKeyboardButton(text="А3", callback_data="riso_a3")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_risograph_quantity_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="500", callback_data="riso_500"), 
             InlineKeyboardButton(text="1000", callback_data="riso_1000"), 
             InlineKeyboardButton(text="1500", callback_data="riso_1500")],
            [InlineKeyboardButton(text="2000", callback_data="riso_2000"), 
             InlineKeyboardButton(text="3000", callback_data="riso_3000"), 
             InlineKeyboardButton(text="5000", callback_data="riso_5000")],
            [InlineKeyboardButton(text="10000", callback_data="riso_10000")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_risograph_color_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Черный", callback_data="riso_black"), 
             InlineKeyboardButton(text="Красный", callback_data="riso_red"), 
             InlineKeyboardButton(text="Черный/Красный", callback_data="riso_black_red")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_risograph_print_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Односторонняя", callback_data="riso_single"), 
             InlineKeyboardButton(text="Двухсторонний", callback_data="riso_double")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_files_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_comment_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📝 Добавить примечание", callback_data="add_note")],
            [InlineKeyboardButton(text="Пропустить", callback_data="skip_note")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_order_confirmation_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✅ Отправить заказ-подтверждение", callback_data="send_order")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )