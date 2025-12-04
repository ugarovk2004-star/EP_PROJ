from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню полиграфии (обновленное)
def get_polygraphy_main_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="ВИЗИТКИ", callback_data="business_cards"), 
             InlineKeyboardButton(text="БЛОКНОТЫ", callback_data="notebooks")],
            [InlineKeyboardButton(text="БУКЛЕТЫ", callback_data="booklets"), 
             InlineKeyboardButton(text="КАЛЕНДАРИ", callback_data="calendars")],
            [InlineKeyboardButton(text="КАТАЛОГИ", callback_data="catalogs"), 
             InlineKeyboardButton(text="КОНВЕРТЫ", callback_data="envelopes")],
            [InlineKeyboardButton(text="ЛИСТОВКИ", callback_data="leaflets"), 
             InlineKeyboardButton(text="ТЕТРАДИ", callback_data="notebooks_school")],
            [InlineKeyboardButton(text="ПЕЧАТЬ НА САМОКЛЕЙКЕ", callback_data="sticker_print"), 
             InlineKeyboardButton(text="ПЛАКАТЫ", callback_data="posters")],
            [InlineKeyboardButton(text="СЕРТИФИКАТЫ", callback_data="certificates"), 
             InlineKeyboardButton(text="СТИКЕРЫ С ПЛОТТЕРНОЙ РЕЗКОЙ", callback_data="plotter_stickers")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# ТЕТРАДИ
def get_notebook_school_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A6", callback_data="notebook_school_a6"), 
             InlineKeyboardButton(text="A5", callback_data="notebook_school_a5")],
            [InlineKeyboardButton(text="A4", callback_data="notebook_school_a4"), 
             InlineKeyboardButton(text="А3", callback_data="notebook_school_a3")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_notebook_school_stitching_position_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="По короткому краю", callback_data="notebook_school_short_edge"), 
             InlineKeyboardButton(text="По длинному краю", callback_data="notebook_school_long_edge")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_notebook_school_binding_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Пружина", callback_data="notebook_school_spring"), 
             InlineKeyboardButton(text="Скрепка", callback_data="notebook_school_staple")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_notebook_school_cover_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Офсетная 80 г/м²", callback_data="notebook_school_cover_offset_80")],
            [InlineKeyboardButton(text="Мелованная бумага 115 г/м²", callback_data="notebook_school_cover_coated_115"), 
             InlineKeyboardButton(text="Мелованная бумага 130 г/м²", callback_data="notebook_school_cover_coated_130")],
            [InlineKeyboardButton(text="Мелованная бумага 150 г/м²", callback_data="notebook_school_cover_coated_150"), 
             InlineKeyboardButton(text="Мелованная бумага 170 г/м²", callback_data="notebook_school_cover_coated_170")],
            [InlineKeyboardButton(text="Мелованная бумага 250 г/м²", callback_data="notebook_school_cover_coated_250"), 
             InlineKeyboardButton(text="Мелованная бумага 300 г/м²", callback_data="notebook_school_cover_coated_300")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_notebook_school_cover_print_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Печать ч/б односторонняя (1+0) только для ВХИ 80гр.", callback_data="notebook_school_cover_bw_single")],
            [InlineKeyboardButton(text="Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.", callback_data="notebook_school_cover_bw_double")],
            [InlineKeyboardButton(text="Цветная односторонняя (4+0)", callback_data="notebook_school_cover_color_single"), 
             InlineKeyboardButton(text="Цветная двухсторонняя (4+4)", callback_data="notebook_school_cover_color_double")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_notebook_school_backing_print_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Печать ч/б односторонняя (1+0) только для ВХИ 80гр.", callback_data="notebook_school_back_bw_single")],
            [InlineKeyboardButton(text="Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.", callback_data="notebook_school_back_bw_double")],
            [InlineKeyboardButton(text="Цветная односторонняя (4+0)", callback_data="notebook_school_back_color_single"), 
             InlineKeyboardButton(text="Цветная двухсторонняя (4+4)", callback_data="notebook_school_back_color_double")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_notebook_school_inner_block_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Офсетная 80 г/м²", callback_data="notebook_school_inner_offset_80")],
            [InlineKeyboardButton(text="Мелованная бумага 115 г/м²", callback_data="notebook_school_inner_coated_115"), 
             InlineKeyboardButton(text="Мелованная бумага 130 г/м²", callback_data="notebook_school_inner_coated_130")],
            [InlineKeyboardButton(text="Мелованная бумага 150 г/м²", callback_data="notebook_school_inner_coated_150"), 
             InlineKeyboardButton(text="Мелованная бумага 170 г/м²", callback_data="notebook_school_inner_coated_170")],
            [InlineKeyboardButton(text="Мелованная бумага 250 г/м²", callback_data="notebook_school_inner_coated_250")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_notebook_school_inner_print_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Печать ч/б односторонняя (1+0) только для ВХИ 80гр.", callback_data="notebook_school_inner_bw_single")],
            [InlineKeyboardButton(text="Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.", callback_data="notebook_school_inner_bw_double")],
            [InlineKeyboardButton(text="Цветная односторонняя (4+0)", callback_data="notebook_school_inner_color_single"), 
             InlineKeyboardButton(text="Цветная двухсторонняя (4+4)", callback_data="notebook_school_inner_color_double")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# КАТАЛОГИ
def get_catalog_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A5", callback_data="catalog_a5"), 
             InlineKeyboardButton(text="A4", callback_data="catalog_a4"), 
             InlineKeyboardButton(text="А3", callback_data="catalog_a3")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_catalog_stitching_position_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="По короткому краю", callback_data="catalog_short_edge"), 
             InlineKeyboardButton(text="По длинному краю", callback_data="catalog_long_edge")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_catalog_binding_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Пружина", callback_data="catalog_spring"), 
             InlineKeyboardButton(text="Скрепка", callback_data="catalog_staple")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_catalog_cover_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Офсетная 80 г/м²", callback_data="catalog_cover_offset_80")],
            [InlineKeyboardButton(text="Мелованная бумага 115 г/м²", callback_data="catalog_cover_coated_115"), 
             InlineKeyboardButton(text="Мелованная бумага 130 г/м²", callback_data="catalog_cover_coated_130")],
            [InlineKeyboardButton(text="Мелованная бумага 150 г/м²", callback_data="catalog_cover_coated_150"), 
             InlineKeyboardButton(text="Мелованная бумага 170 г/м²", callback_data="catalog_cover_coated_170")],
            [InlineKeyboardButton(text="Мелованная бумага 250 г/м²", callback_data="catalog_cover_coated_250"), 
             InlineKeyboardButton(text="Мелованная бумага 300 г/м²", callback_data="catalog_cover_coated_300")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_catalog_cover_print_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Печать ч/б односторонняя (1+0) только для ВХИ 80гр.", callback_data="catalog_cover_bw_single")],
            [InlineKeyboardButton(text="Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.", callback_data="catalog_cover_bw_double")],
            [InlineKeyboardButton(text="Цветная односторонняя (4+0)", callback_data="catalog_cover_color_single"), 
             InlineKeyboardButton(text="Цветная двухсторонняя (4+4)", callback_data="catalog_cover_color_double")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_catalog_backing_print_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Печать ч/б односторонняя (1+0) только для ВХИ 80гр.", callback_data="catalog_back_bw_single")],
            [InlineKeyboardButton(text="Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.", callback_data="catalog_back_bw_double")],
            [InlineKeyboardButton(text="Цветная односторонняя (4+0)", callback_data="catalog_back_color_single"), 
             InlineKeyboardButton(text="Цветная двухсторонняя (4+4)", callback_data="catalog_back_color_double")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_catalog_inner_block_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Офсетная 80 г/м²", callback_data="catalog_inner_offset_80")],
            [InlineKeyboardButton(text="Мелованная бумага 115 г/м²", callback_data="catalog_inner_coated_115"), 
             InlineKeyboardButton(text="Мелованная бумага 130 г/м²", callback_data="catalog_inner_coated_130")],
            [InlineKeyboardButton(text="Мелованная бумага 150 г/м²", callback_data="catalog_inner_coated_150"), 
             InlineKeyboardButton(text="Мелованная бумага 170 г/м²", callback_data="catalog_inner_coated_170")],
            [InlineKeyboardButton(text="Мелованная бумага 250 г/м²", callback_data="catalog_inner_coated_250")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_catalog_inner_print_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Печать ч/б односторонняя (1+0) только для ВХИ 80гр.", callback_data="catalog_inner_bw_single")],
            [InlineKeyboardButton(text="Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.", callback_data="catalog_inner_bw_double")],
            [InlineKeyboardButton(text="Цветная односторонняя (4+0)", callback_data="catalog_inner_color_single"), 
             InlineKeyboardButton(text="Цветная двухсторонняя (4+4)", callback_data="catalog_inner_color_double")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Визитки
def get_business_card_print_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Офсетная", callback_data="business_card_offset"), 
             InlineKeyboardButton(text="Цифровая", callback_data="business_card_digital")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_business_card_offset_color_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="4+0 (односторонние)", callback_data="business_card_offset_4_0"), 
             InlineKeyboardButton(text="4+4 (двусторонние)", callback_data="business_card_offset_4_4")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_business_card_offset_quantity_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1000 шт.", callback_data="business_card_offset_1000"), 
             InlineKeyboardButton(text="2500 шт.", callback_data="business_card_offset_2500")],
            [InlineKeyboardButton(text="5000 шт.", callback_data="business_card_offset_5000"), 
             InlineKeyboardButton(text="10000 шт.", callback_data="business_card_offset_10000")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_business_card_digital_paper_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Картон 310 г/м²", callback_data="business_card_digital_cardboard_310"), 
             InlineKeyboardButton(text="Лен", callback_data="business_card_digital_linen")],
            [InlineKeyboardButton(text="Маджестик", callback_data="business_card_digital_majestic"), 
             InlineKeyboardButton(text="Фактурная", callback_data="business_card_digital_textured")],
            [InlineKeyboardButton(text="Плайк", callback_data="business_card_digital_plyk")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_business_card_digital_lamination_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Без ламинации", callback_data="business_card_digital_no_lamination"), 
             InlineKeyboardButton(text="Глянцевая", callback_data="business_card_digital_gloss_lamination"), 
             InlineKeyboardButton(text="Матовая", callback_data="business_card_digital_matte_lamination")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_business_card_digital_quantity_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="50 шт.", callback_data="business_card_digital_50"), 
             InlineKeyboardButton(text="100 шт.", callback_data="business_card_digital_100"), 
             InlineKeyboardButton(text="200 шт.", callback_data="business_card_digital_200")],
            [InlineKeyboardButton(text="300 шт.", callback_data="business_card_digital_300"), 
             InlineKeyboardButton(text="1000 шт.", callback_data="business_card_digital_1000")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Блокноты
def get_notebook_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A6", callback_data="notebook_a6"), 
             InlineKeyboardButton(text="A5", callback_data="notebook_a5"), 
             InlineKeyboardButton(text="A4", callback_data="notebook_a4")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_notebook_inner_block_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Офсетная 80 г/м² без печати", callback_data="notebook_inner_offset_no_print")],
            [InlineKeyboardButton(text="Офсетная 80 г/м² с цветной печатью", callback_data="notebook_inner_offset_color")],
            [InlineKeyboardButton(text="Офсетная 80 г/м² с Ч/Б печатью", callback_data="notebook_inner_offset_bw")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_notebook_cover_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Мелованная бумага 250 г/м² с печатью", callback_data="notebook_cover_coated_250_print")],
            [InlineKeyboardButton(text="Мелованная бумага 300 г/м² с печатью", callback_data="notebook_cover_coated_300_print")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_notebook_backing_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="С печатью", callback_data="notebook_back_print"), 
             InlineKeyboardButton(text="Без печати", callback_data="notebook_back_no_print")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_notebook_stitching_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="По короткому краю", callback_data="notebook_stitch_short"), 
             InlineKeyboardButton(text="По длинному краю", callback_data="notebook_stitch_long")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_notebook_pages_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="20 стр.", callback_data="notebook_pages_20"), 
             InlineKeyboardButton(text="40 стр.", callback_data="notebook_pages_40")],
            [InlineKeyboardButton(text="60 стр.", callback_data="notebook_pages_60"), 
             InlineKeyboardButton(text="80 стр.", callback_data="notebook_pages_80")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Буклеты
def get_booklet_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A4 (в сложенном виде)", callback_data="booklet_a4_folded"), 
             InlineKeyboardButton(text="A5 (в сложенном виде)", callback_data="booklet_a5_folded")],
            [InlineKeyboardButton(text="A6 (в сложенном виде)", callback_data="booklet_a6_folded"), 
             InlineKeyboardButton(text="Евроформат (в сложенном виде)", callback_data="booklet_euro_folded")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_booklet_paper_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Мелованная 115 г/м²", callback_data="booklet_paper_115"), 
             InlineKeyboardButton(text="Мелованная 130 г/м²", callback_data="booklet_paper_130")],
            [InlineKeyboardButton(text="Мелованная 150 г/м²", callback_data="booklet_paper_150"), 
             InlineKeyboardButton(text="Мелованная 250 г/м²", callback_data="booklet_paper_250")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_booklet_color_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="4+0 (односторонняя)", callback_data="booklet_color_4_0"), 
             InlineKeyboardButton(text="4+4 (двухсторонняя)", callback_data="booklet_color_4_4")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_booklet_fold_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Один сгиб", callback_data="booklet_fold_one"), 
             InlineKeyboardButton(text="Два сгиба", callback_data="booklet_fold_two"), 
             InlineKeyboardButton(text="Гармошка", callback_data="booklet_fold_accordion")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Календари
def get_calendar_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Квартальный", callback_data="calendar_quarterly"), 
             InlineKeyboardButton(text="Домик", callback_data="calendar_house")],
            [InlineKeyboardButton(text="Карманный (кратно 8 шт.)", callback_data="calendar_pocket"), 
             InlineKeyboardButton(text="Перекидной А4", callback_data="calendar_flip_a4")],
            [InlineKeyboardButton(text="Перекидной А3", callback_data="calendar_flip_a3")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Конверты
def get_envelope_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Евроконверт", callback_data="envelope_euro"), 
             InlineKeyboardButton(text="Формат C5", callback_data="envelope_c5")],
            [InlineKeyboardButton(text="Формат C6", callback_data="envelope_c6"), 
             InlineKeyboardButton(text="Конверт для CD", callback_data="envelope_cd")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Листовки
def get_leaflet_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A4 (210×297 мм)", callback_data="leaflet_a4"), 
             InlineKeyboardButton(text="A5 (148×210 мм)", callback_data="leaflet_a5")],
            [InlineKeyboardButton(text="A6 (105×148 мм)", callback_data="leaflet_a6"), 
             InlineKeyboardButton(text="A7 (74×105 мм)", callback_data="leaflet_a7")],
            [InlineKeyboardButton(text="Евроформат (210×99 мм)", callback_data="leaflet_euro")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_leaflet_paper_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Мелованная 115 г/м²", callback_data="leaflet_paper_115"), 
             InlineKeyboardButton(text="Мелованная 130 г/м²", callback_data="leaflet_paper_130")],
            [InlineKeyboardButton(text="Мелованная 150 г/м²", callback_data="leaflet_paper_150"), 
             InlineKeyboardButton(text="Офсетная 80 г/м²", callback_data="leaflet_paper_offset_80")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Печать на самоклейке
def get_sticker_material_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Пленка белая мат.", callback_data="sticker_film_white_matte"), 
             InlineKeyboardButton(text="Пленка белая гл.", callback_data="sticker_film_white_glossy")],
            [InlineKeyboardButton(text="Пленка прозрач. мат.", callback_data="sticker_film_clear_matte"), 
             InlineKeyboardButton(text="Пленка прозрач. гл.", callback_data="sticker_film_clear_glossy")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_sticker_print_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A4 (210×297 мм)", callback_data="sticker_print_a4"), 
             InlineKeyboardButton(text="A3 (297×420 мм)", callback_data="sticker_print_a3"), 
             InlineKeyboardButton(text="SRA3 (320×450 мм)", callback_data="sticker_print_sra3")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_sticker_cutting_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Да", callback_data="sticker_cutting_yes"), 
             InlineKeyboardButton(text="Нет", callback_data="sticker_cutting_no")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Плакаты
def get_poster_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A3 (297×420 мм) - цифровая печать", callback_data="poster_a3_digital")],
            [InlineKeyboardButton(text="A2 (420×594 мм) - интерьерная печать", callback_data="poster_a2_interior")],
            [InlineKeyboardButton(text="A1 (594×841 мм) - интерьерная печать", callback_data="poster_a1_interior")],
            [InlineKeyboardButton(text="A0 (841×1189 мм) - интерьерная печать", callback_data="poster_a0_interior")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_poster_paper_type_a3_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Офсетная 80 г/м²", callback_data="poster_a3_offset_80"), 
             InlineKeyboardButton(text="Мелованная 115 г/м²", callback_data="poster_a3_coated_115")],
            [InlineKeyboardButton(text="Мелованная 130 г/м²", callback_data="poster_a3_coated_130"), 
             InlineKeyboardButton(text="Мелованная 150 г/м²", callback_data="poster_a3_coated_150")],
            [InlineKeyboardButton(text="Мелованная 170 г/м²", callback_data="poster_a3_coated_170"), 
             InlineKeyboardButton(text="Мелованная 250 г/м²", callback_data="poster_a3_coated_250")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_poster_cutting_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Подрезка нужна", callback_data="poster_cutting_yes"), 
             InlineKeyboardButton(text="Подрезка не нужна", callback_data="poster_cutting_no")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_poster_paper_type_large_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Постерная бумага 150 г/м²", callback_data="poster_large_150"), 
             InlineKeyboardButton(text="Постерная бумага 200 г/м²", callback_data="poster_large_200")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Сертификаты
def get_certificate_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A4 (210×297 мм)", callback_data="certificate_a4"), 
             InlineKeyboardButton(text="A5 (148×210 мм)", callback_data="certificate_a5")],
            [InlineKeyboardButton(text="A6 (105×148 мм)", callback_data="certificate_a6"), 
             InlineKeyboardButton(text="Евроформат (210×99 мм)", callback_data="certificate_euro")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_certificate_paper_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Мелованная 150 г/м²", callback_data="certificate_paper_150"), 
             InlineKeyboardButton(text="Мелованная 170 г/м²", callback_data="certificate_paper_170"), 
             InlineKeyboardButton(text="Мелованная 250 г/м²", callback_data="certificate_paper_250")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_certificate_lamination_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Без ламинации", callback_data="certificate_no_lamination"), 
             InlineKeyboardButton(text="Глянцевая", callback_data="certificate_gloss_lamination"), 
             InlineKeyboardButton(text="Матовая", callback_data="certificate_matte_lamination")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Стикеры с плоттерной резкой
def get_sticker_pack_material_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Пленка белая мат.", callback_data="sticker_pack_film_white_matte"), 
             InlineKeyboardButton(text="Пленка белая гл.", callback_data="sticker_pack_film_white_glossy")],
            [InlineKeyboardButton(text="Пленка прозрач. мат.", callback_data="sticker_pack_film_clear_matte"), 
             InlineKeyboardButton(text="Пленка прозрач. гл.", callback_data="sticker_pack_film_clear_glossy")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_sticker_pack_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="A4 (210×297 мм)", callback_data="sticker_pack_a4"), 
             InlineKeyboardButton(text="A3 (297×420 мм)", callback_data="sticker_pack_a3")],
            [InlineKeyboardButton(text="A5 стикерпак (148×210 мм)", callback_data="sticker_pack_a5"), 
             InlineKeyboardButton(text="A6 стикерпак (105×148 мм)", callback_data="sticker_pack_a6")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_sticker_pack_color_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="4+0 (односторонняя)", callback_data="sticker_pack_color_4_0")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_sticker_pack_cut_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Да (включена в стоимость)", callback_data="sticker_pack_cut_yes")],
            [InlineKeyboardButton(text="Нет (только печать)", callback_data="sticker_pack_cut_no")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )