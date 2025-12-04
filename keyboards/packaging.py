from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню упаковки
def get_packaging_main_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="ПАКЕТЫ", callback_data="packaging_bags"), 
             InlineKeyboardButton(text="КОРОБКИ", callback_data="packaging_boxes")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Пакеты - выбор типа
def get_bag_type_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Бумажные пакеты", callback_data="bag_paper"), 
             InlineKeyboardButton(text="ПВД пакеты", callback_data="bag_pvd")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Бумажные пакеты
def get_bag_paper_print_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Печать с одной стороны пакета", callback_data="bag_paper_print_one_side")],
            [InlineKeyboardButton(text="Печать с 2 сторон с одного макета", callback_data="bag_paper_print_two_sides_same")],
            [InlineKeyboardButton(text="Печать с 2 сторон разные макеты", callback_data="bag_paper_print_two_sides_different")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_bag_paper_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="220×330×70 мм", callback_data="bag_paper_220x330x70"), 
             InlineKeyboardButton(text="195×320×90 мм", callback_data="bag_paper_195x320x90")],
            [InlineKeyboardButton(text="100×330×100 мм", callback_data="bag_paper_100x330x100"), 
             InlineKeyboardButton(text="170×220×70 мм", callback_data="bag_paper_170x220x70")],
            [InlineKeyboardButton(text="70×330×70 мм", callback_data="bag_paper_70x330x70"), 
             InlineKeyboardButton(text="130×220×70 мм", callback_data="bag_paper_130x220x70")],
            [InlineKeyboardButton(text="120×140×70 мм", callback_data="bag_paper_120x140x70"), 
             InlineKeyboardButton(text="210×210×100 мм", callback_data="bag_paper_210x210x100")],
            [InlineKeyboardButton(text="210×210×80 мм", callback_data="bag_paper_210x210x80"), 
             InlineKeyboardButton(text="330×220×70 мм", callback_data="bag_paper_330x220x70")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_bag_paper_lamination_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Матовое", callback_data="bag_paper_matte"), 
             InlineKeyboardButton(text="Глянцевое", callback_data="bag_paper_glossy")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_bag_paper_grommets_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Золото", callback_data="bag_paper_grommets_gold"), 
             InlineKeyboardButton(text="Серебро", callback_data="bag_paper_grommets_silver")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_bag_paper_handle_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Белые", callback_data="bag_paper_handle_white"), 
             InlineKeyboardButton(text="Чёрные", callback_data="bag_paper_handle_black")],
            [InlineKeyboardButton(text="Красные", callback_data="bag_paper_handle_red"), 
             InlineKeyboardButton(text="Синие", callback_data="bag_paper_handle_blue")],
            [InlineKeyboardButton(text="Зелёные", callback_data="bag_paper_handle_green"), 
             InlineKeyboardButton(text="Жёлтые", callback_data="bag_paper_handle_yellow")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# ПВД пакеты
def get_bag_pvd_print_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1+0", callback_data="bag_pvd_print_1_0"), 
             InlineKeyboardButton(text="1+1", callback_data="bag_pvd_print_1_1")],
            [InlineKeyboardButton(text="2+0", callback_data="bag_pvd_print_2_0"), 
             InlineKeyboardButton(text="2+2", callback_data="bag_pvd_print_2_2")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_bag_pvd_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="20×30 см", callback_data="bag_pvd_20x30"), 
             InlineKeyboardButton(text="30×40 см", callback_data="bag_pvd_30x40")],
            [InlineKeyboardButton(text="40×50 см", callback_data="bag_pvd_40x50"), 
             InlineKeyboardButton(text="50×60 см", callback_data="bag_pvd_50x60")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Коробки - выбор материала
def get_box_material_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Коробки из мелованного картона", callback_data="box_cardboard"), 
             InlineKeyboardButton(text="Коробки из микро-гофры", callback_data="box_corrugated")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Коробки из мелованного картона
def get_box_cardboard_print_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Без печати", callback_data="box_cardboard_no_print"), 
             InlineKeyboardButton(text="Полноцветная печать", callback_data="box_cardboard_full_color")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

# Коробки из микро-гофры
def get_box_corrugated_format_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="95×55×90 мм", callback_data="box_corrugated_95x55x90"), 
             InlineKeyboardButton(text="115×95×65 мм", callback_data="box_corrugated_115x95x65")],
            [InlineKeyboardButton(text="180×55×55 мм", callback_data="box_corrugated_180x55x55"), 
             InlineKeyboardButton(text="360×150×50 мм", callback_data="box_corrugated_360x150x50")],
            [InlineKeyboardButton(text="415×160×60 мм", callback_data="box_corrugated_415x160x60"), 
             InlineKeyboardButton(text="200×200×10 мм", callback_data="box_corrugated_200x200x10")],
            [InlineKeyboardButton(text="Индивидуальный размер", callback_data="box_corrugated_custom")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_box_corrugated_color_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Белый", callback_data="box_corrugated_white"), 
             InlineKeyboardButton(text="Коричневый", callback_data="box_corrugated_brown")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )

def get_box_corrugated_logo_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Без нанесения", callback_data="box_corrugated_no_logo"), 
             InlineKeyboardButton(text="С нанесением", callback_data="box_corrugated_with_logo")],
            [InlineKeyboardButton(text="💬 Написать менеджеру", callback_data="write_manager"), 
             InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
        ]
    )