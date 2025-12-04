from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from states.order_states import OrderStates
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.polygraphy import *
from keyboards.copycenter import get_files_keyboard, get_comment_keyboard, get_order_confirmation_keyboard
from utils.order_message import create_order_summary

router = Router()

# Обработчик главного меню полиграфии через callback
@router.callback_query(F.data == "polygraphy")
async def polygraphy_main(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.waiting_for_files)
    await state.update_data(previous_menu='main')
    await callback.answer()
    await callback.message.edit_text(
        "Раздел ПОЛИГРАФИЯ. Выберите продукт:",
        reply_markup=get_polygraphy_main_keyboard()
    )

# ВИЗИТКИ
@router.callback_query(F.data == "business_cards")
async def business_cards_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.business_card_print_type)
    await state.update_data(service_type="Визитки", previous_menu='polygraphy')
    await callback.answer()
    await callback.message.edit_text(
        "🎴 ВИЗИТКИ\n\nВыберите тип печати:",
        reply_markup=get_business_card_print_type_keyboard()
    )

# Обработчики визиток - офсетная печать
@router.callback_query(F.data == "business_card_offset")
async def business_cards_offset_selected(callback: CallbackQuery, state: FSMContext):
    await state.update_data(Тип="Офсетная")
    await state.set_state(OrderStates.business_card_offset_color)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите цветность:",
        reply_markup=get_business_card_offset_color_keyboard()
    )

@router.callback_query(F.data.in_(["business_card_offset_4_0", "business_card_offset_4_4"]))
async def business_cards_offset_color_selected(callback: CallbackQuery, state: FSMContext):
    color_map = {
        "business_card_offset_4_0": "4+0 (односторонние)",
        "business_card_offset_4_4": "4+4 (двусторонние)"
    }
    await state.update_data(Цвет=color_map[callback.data])
    await state.set_state(OrderStates.business_card_offset_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите количество:",
        reply_markup=get_business_card_offset_quantity_keyboard()
    )

@router.callback_query(F.data.in_(["business_card_offset_1000", "business_card_offset_2500", 
                                  "business_card_offset_5000", "business_card_offset_10000"]))
async def business_cards_offset_quantity_selected(callback: CallbackQuery, state: FSMContext):
    quantity_map = {
        "business_card_offset_1000": "1000 шт.",
        "business_card_offset_2500": "2500 шт.",
        "business_card_offset_5000": "5000 шт.",
        "business_card_offset_10000": "10000 шт."
    }
    await state.update_data(Количество=quantity_map[callback.data])
    await state.set_state(OrderStates.waiting_for_files)
    await callback.answer()
    await callback.message.edit_text(
        "Теперь прикрепите файлы для печати:",
        reply_markup=get_files_keyboard()
    )

# Обработчики визиток - цифровая печать
@router.callback_query(F.data == "business_card_digital")
async def business_cards_digital_selected(callback: CallbackQuery, state: FSMContext):
    await state.update_data(Тип="Цифровая")
    await state.set_state(OrderStates.business_card_digital_paper)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип бумаги:",
        reply_markup=get_business_card_digital_paper_keyboard()
    )

@router.callback_query(F.data.in_(["business_card_digital_cardboard_310", "business_card_digital_linen",
                                 "business_card_digital_majestic", "business_card_digital_textured",
                                 "business_card_digital_plyk"]))
async def business_cards_digital_paper_selected(callback: CallbackQuery, state: FSMContext):
    paper_map = {
        "business_card_digital_cardboard_310": "Картон 310 г/м²",
        "business_card_digital_linen": "Лен",
        "business_card_digital_majestic": "Маджестик",
        "business_card_digital_textured": "Фактурная",
        "business_card_digital_plyk": "Плайк"
    }
    await state.update_data(Тип_бумаги=paper_map[callback.data])
    await state.set_state(OrderStates.business_card_digital_color)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите цветность:",
        reply_markup=get_business_card_offset_color_keyboard()  # Та же клавиатура
    )

@router.callback_query(F.data.in_(["business_card_digital_no_lamination", "business_card_digital_gloss_lamination",
                                 "business_card_digital_matte_lamination"]))
async def business_cards_digital_lamination_selected(callback: CallbackQuery, state: FSMContext):
    lamination_map = {
        "business_card_digital_no_lamination": "Без ламинации",
        "business_card_digital_gloss_lamination": "Глянцевая",
        "business_card_digital_matte_lamination": "Матовая"
    }
    await state.update_data(Ламинация=lamination_map[callback.data])
    await state.set_state(OrderStates.business_card_digital_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите количество:",
        reply_markup=get_business_card_digital_quantity_keyboard()
    )

@router.callback_query(F.data.in_(["business_card_digital_50", "business_card_digital_100", 
                                  "business_card_digital_200", "business_card_digital_300",
                                  "business_card_digital_1000"]))
async def business_cards_digital_quantity_selected(callback: CallbackQuery, state: FSMContext):
    quantity_map = {
        "business_card_digital_50": "50 шт.",
        "business_card_digital_100": "100 шт.",
        "business_card_digital_200": "200 шт.",
        "business_card_digital_300": "300 шт.",
        "business_card_digital_1000": "1000 шт."
    }
    await state.update_data(Количество=quantity_map[callback.data])
    await state.set_state(OrderStates.waiting_for_files)
    await callback.answer()
    await callback.message.edit_text(
        "Теперь прикрепите файлы для печати:",
        reply_markup=get_files_keyboard()
    )

# БЛОКНОТЫ
@router.callback_query(F.data == "notebooks")
async def notebooks_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.notebook_format)
    await state.update_data(service_type="Блокноты", previous_menu='polygraphy')
    await callback.answer()
    await callback.message.edit_text(
        "📓 БЛОКНОТЫ\n\nВыберите формат:",
        reply_markup=get_notebook_format_keyboard()
    )

@router.callback_query(F.data.in_(["notebook_a6", "notebook_a5", "notebook_a4"]))
async def notebook_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "notebook_a6": "A6",
        "notebook_a5": "A5",
        "notebook_a4": "A4"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.notebook_inner_block)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите внутренний блок:",
        reply_markup=get_notebook_inner_block_keyboard()
    )

@router.callback_query(F.data.in_(["notebook_inner_offset_no_print", "notebook_inner_offset_color",
                                 "notebook_inner_offset_bw"]))
async def notebook_inner_block_selected(callback: CallbackQuery, state: FSMContext):
    inner_map = {
        "notebook_inner_offset_no_print": "Офсетная 80 г/м² без печати",
        "notebook_inner_offset_color": "Офсетная 80 г/м² с цветной печатью",
        "notebook_inner_offset_bw": "Офсетная 80 г/м² с Ч/Б печатью"
    }
    await state.update_data(Внутренний_блок=inner_map[callback.data])
    await state.set_state(OrderStates.notebook_cover_type)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип обложки:",
        reply_markup=get_notebook_cover_type_keyboard()
    )

@router.callback_query(F.data.in_(["notebook_cover_coated_250_print", "notebook_cover_coated_300_print"]))
async def notebook_cover_type_selected(callback: CallbackQuery, state: FSMContext):
    cover_map = {
        "notebook_cover_coated_250_print": "Мелованная бумага 250 г/м² с печатью",
        "notebook_cover_coated_300_print": "Мелованная бумага 300 г/м² с печатью"
    }
    await state.update_data(Обложка=cover_map[callback.data])
    await state.set_state(OrderStates.notebook_backing)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите подложку:",
        reply_markup=get_notebook_backing_keyboard()
    )

@router.callback_query(F.data.in_(["notebook_back_print", "notebook_back_no_print"]))
async def notebook_backing_selected(callback: CallbackQuery, state: FSMContext):
    backing_map = {
        "notebook_back_print": "С печатью",
        "notebook_back_no_print": "Без печати"
    }
    await state.update_data(Подложка=backing_map[callback.data])
    await state.set_state(OrderStates.notebook_stitching)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите позицию сшивания:",
        reply_markup=get_notebook_stitching_keyboard()
    )

@router.callback_query(F.data.in_(["notebook_stitch_short", "notebook_stitch_long"]))
async def notebook_stitching_selected(callback: CallbackQuery, state: FSMContext):
    stitch_map = {
        "notebook_stitch_short": "По короткому краю",
        "notebook_stitch_long": "По длинному краю"
    }
    await state.update_data(Позиция_сшивания=stitch_map[callback.data])
    await state.set_state(OrderStates.notebook_pages)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите количество страниц:",
        reply_markup=get_notebook_pages_keyboard()
    )

@router.callback_query(F.data.in_(["notebook_pages_20", "notebook_pages_40", "notebook_pages_60", "notebook_pages_80"]))
async def notebook_pages_selected(callback: CallbackQuery, state: FSMContext):
    pages_map = {
        "notebook_pages_20": "20 стр.",
        "notebook_pages_40": "40 стр.",
        "notebook_pages_60": "60 стр.",
        "notebook_pages_80": "80 стр."
    }
    await state.update_data(Страниц=pages_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# БУКЛЕТЫ
@router.callback_query(F.data == "booklets")
async def booklets_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.booklet_format)
    await state.update_data(service_type="Буклеты", previous_menu='polygraphy')
    await callback.answer()
    await callback.message.edit_text(
        "📰 БУКЛЕТЫ\n\nВыберите формат готового изделия:",
        reply_markup=get_booklet_format_keyboard()
    )

@router.callback_query(F.data.in_(["booklet_a4_folded", "booklet_a5_folded", "booklet_a6_folded", "booklet_euro_folded"]))
async def booklet_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "booklet_a4_folded": "A4 (в сложенном виде)",
        "booklet_a5_folded": "A5 (в сложенном виде)",
        "booklet_a6_folded": "A6 (в сложенном виде)",
        "booklet_euro_folded": "Евроформат (в сложенном виде)"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.booklet_paper_type)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип бумаги:",
        reply_markup=get_booklet_paper_type_keyboard()
    )

@router.callback_query(F.data.in_(["booklet_paper_115", "booklet_paper_130", "booklet_paper_150", "booklet_paper_250"]))
async def booklet_paper_type_selected(callback: CallbackQuery, state: FSMContext):
    paper_map = {
        "booklet_paper_115": "Мелованная 115 г/м²",
        "booklet_paper_130": "Мелованная 130 г/м²",
        "booklet_paper_150": "Мелованная 150 г/м²",
        "booklet_paper_250": "Мелованная 250 г/м²"
    }
    await state.update_data(Тип_бумаги=paper_map[callback.data])
    await state.set_state(OrderStates.booklet_color)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите цветность:",
        reply_markup=get_booklet_color_keyboard()
    )

@router.callback_query(F.data.in_(["booklet_color_4_0", "booklet_color_4_4"]))
async def booklet_color_selected(callback: CallbackQuery, state: FSMContext):
    color_map = {
        "booklet_color_4_0": "4+0 (односторонняя)",
        "booklet_color_4_4": "4+4 (двухсторонняя)"
    }
    await state.update_data(Цвет=color_map[callback.data])
    await state.set_state(OrderStates.booklet_fold_type)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип сгиба:",
        reply_markup=get_booklet_fold_type_keyboard()
    )

@router.callback_query(F.data.in_(["booklet_fold_one", "booklet_fold_two", "booklet_fold_accordion"]))
async def booklet_fold_type_selected(callback: CallbackQuery, state: FSMContext):
    fold_map = {
        "booklet_fold_one": "Один сгиб",
        "booklet_fold_two": "Два сгиба",
        "booklet_fold_accordion": "Гармошка"
    }
    await state.update_data(Тип_сгиба=fold_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# КАЛЕНДАРИ
@router.callback_query(F.data == "calendars")
async def calendars_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.calendar_type)
    await state.update_data(service_type="Календари", previous_menu='polygraphy')
    await callback.answer()
    await callback.message.edit_text(
        "📅 КАЛЕНДАРИ\n\nВыберите вид календаря:",
        reply_markup=get_calendar_type_keyboard()
    )

@router.callback_query(F.data.in_(["calendar_quarterly", "calendar_house", "calendar_pocket", 
                                  "calendar_flip_a4", "calendar_flip_a3"]))
async def calendar_type_selected(callback: CallbackQuery, state: FSMContext):
    type_map = {
        "calendar_quarterly": "Квартальный",
        "calendar_house": "Домик",
        "calendar_pocket": "Карманный (кратно 8 шт.)",
        "calendar_flip_a4": "Перекидной А4",
        "calendar_flip_a3": "Перекидной А3"
    }
    await state.update_data(Вид=type_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# КОНВЕРТЫ
@router.callback_query(F.data == "envelopes")
async def envelopes_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.envelope_type)
    await state.update_data(service_type="Конверты", previous_menu='polygraphy')
    await callback.answer()
    await callback.message.edit_text(
        "✉️ КОНВЕРТЫ\n\nВыберите тип конверта:",
        reply_markup=get_envelope_type_keyboard()
    )

@router.callback_query(F.data.in_(["envelope_euro", "envelope_c5", "envelope_c6", "envelope_cd"]))
async def envelope_type_selected(callback: CallbackQuery, state: FSMContext):
    type_map = {
        "envelope_euro": "Евроконверт",
        "envelope_c5": "Формат C5",
        "envelope_c6": "Формат C6",
        "envelope_cd": "Конверт для CD"
    }
    await state.update_data(Тип_конверта=type_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# ЛИСТОВКИ
@router.callback_query(F.data == "leaflets")
async def leaflets_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.leaflet_format)
    await state.update_data(service_type="Листовки", previous_menu='polygraphy')
    await callback.answer()
    await callback.message.edit_text(
        "📄 ЛИСТОВКИ\n\nВыберите формат:",
        reply_markup=get_leaflet_format_keyboard()
    )

@router.callback_query(F.data.in_(["leaflet_a4", "leaflet_a5", "leaflet_a6", "leaflet_a7", "leaflet_euro"]))
async def leaflet_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "leaflet_a4": "A4 (210×297 мм)",
        "leaflet_a5": "A5 (148×210 мм)",
        "leaflet_a6": "A6 (105×148 мм)",
        "leaflet_a7": "A7 (74×105 мм)",
        "leaflet_euro": "Евроформат (210×99 мм)"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.leaflet_paper_type)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип бумаги:",
        reply_markup=get_leaflet_paper_type_keyboard()
    )

@router.callback_query(F.data.in_(["leaflet_paper_115", "leaflet_paper_130", "leaflet_paper_150", "leaflet_paper_offset_80"]))
async def leaflet_paper_type_selected(callback: CallbackQuery, state: FSMContext):
    paper_map = {
        "leaflet_paper_115": "Мелованная 115 г/м²",
        "leaflet_paper_130": "Мелованная 130 г/м²",
        "leaflet_paper_150": "Мелованная 150 г/м²",
        "leaflet_paper_offset_80": "Офсетная 80 г/м²"
    }
    await state.update_data(Тип_бумаги=paper_map[callback.data])
    await state.set_state(OrderStates.leaflet_color)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите цветность:",
        reply_markup=get_business_card_offset_color_keyboard()  # Та же клавиатура
    )

@router.callback_query(F.data == "leaflet_color")
async def leaflet_selected(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# ПЕЧАТЬ НА САМОКЛЕЙКЕ
@router.callback_query(F.data == "sticker_print")
async def stickers_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.sticker_material_type)
    await state.update_data(service_type="Печать на самоклейке", previous_menu='polygraphy')
    await callback.answer()
    await callback.message.edit_text(
        "🏷️ ПЕЧАТЬ НА САМОКЛЕЙКЕ\n\nВыберите тип материала:",
        reply_markup=get_sticker_material_type_keyboard()
    )

@router.callback_query(F.data.in_(["sticker_film_white_matte", "sticker_film_white_glossy",
                                 "sticker_film_clear_matte", "sticker_film_clear_glossy"]))
async def sticker_material_type_selected(callback: CallbackQuery, state: FSMContext):
    material_map = {
        "sticker_film_white_matte": "Пленка белая мат.",
        "sticker_film_white_glossy": "Пленка белая гл.",
        "sticker_film_clear_matte": "Пленка прозрач. мат.",
        "sticker_film_clear_glossy": "Пленка прозрач. гл."
    }
    await state.update_data(Материал=material_map[callback.data])
    await state.set_state(OrderStates.sticker_print_format)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите формат печати:",
        reply_markup=get_sticker_print_format_keyboard()
    )

@router.callback_query(F.data.in_(["sticker_print_a4", "sticker_print_a3", "sticker_print_sra3"]))
async def sticker_print_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "sticker_print_a4": "A4 (210×297 мм)",
        "sticker_print_a3": "A3 (297×420 мм)",
        "sticker_print_sra3": "SRA3 (320×450 мм)"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.sticker_cutting)
    await callback.answer()
    await callback.message.edit_text(
        "Вам нужна подрезка?:",
        reply_markup=get_sticker_cutting_keyboard()
    )

@router.callback_query(F.data.in_(["sticker_cutting_yes", "sticker_cutting_no"]))
async def sticker_cutting_selected(callback: CallbackQuery, state: FSMContext):
    cutting_map = {
        "sticker_cutting_yes": "Да",
        "sticker_cutting_no": "Нет"
    }
    await state.update_data(Подрез=cutting_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# ПЛАКАТЫ
@router.callback_query(F.data == "posters")
async def posters_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.poster_format)
    await state.update_data(service_type="Плакаты", previous_menu='polygraphy')
    await callback.answer()
    await callback.message.edit_text(
        "📊 ПЛАКАТЫ\n\nВыберите формат:",
        reply_markup=get_poster_format_keyboard()
    )

@router.callback_query(F.data == "poster_a3_digital")
async def poster_a3_selected(callback: CallbackQuery, state: FSMContext):
    await state.update_data(Формат="A3 (297×420 мм) - цифровая печать")
    await state.set_state(OrderStates.poster_paper_type_a3)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип бумаги:",
        reply_markup=get_poster_paper_type_a3_keyboard()
    )

@router.callback_query(F.data.in_(["poster_a3_offset_80", "poster_a3_coated_115", "poster_a3_coated_130",
                                 "poster_a3_coated_150", "poster_a3_coated_170", "poster_a3_coated_250"]))
async def poster_paper_type_a3_selected(callback: CallbackQuery, state: FSMContext):
    paper_map = {
        "poster_a3_offset_80": "Офсетная 80 г/м²",
        "poster_a3_coated_115": "Мелованная 115 г/м²",
        "poster_a3_coated_130": "Мелованная 130 г/м²",
        "poster_a3_coated_150": "Мелованная 150 г/м²",
        "poster_a3_coated_170": "Мелованная 170 г/м²",
        "poster_a3_coated_250": "Мелованная 250 г/м²"
    }
    await state.update_data(Тип_бумаги=paper_map[callback.data])
    await state.set_state(OrderStates.poster_cutting_a3)
    await callback.answer()
    await callback.message.edit_text(
        "Вам нужна подрезка?:",
        reply_markup=get_poster_cutting_keyboard()
    )

@router.callback_query(F.data.in_(["poster_cutting_yes", "poster_cutting_no"]))
async def poster_cutting_selected(callback: CallbackQuery, state: FSMContext):
    cutting_map = {
        "poster_cutting_yes": "Подрезка нужна",
        "poster_cutting_no": "Подрезка не нужна"
    }
    await state.update_data(Подрез=cutting_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

@router.callback_query(F.data.in_(["poster_a2_interior", "poster_a1_interior", "poster_a0_interior"]))
async def poster_large_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "poster_a2_interior": "A2 (420×594 мм) - интерьерная печать",
        "poster_a1_interior": "A1 (594×841 мм) - интерьерная печать",
        "poster_a0_interior": "A0 (841×1189 мм) - интерьерная печать"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.poster_paper_type_large)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип бумаги:",
        reply_markup=get_poster_paper_type_large_keyboard()
    )

@router.callback_query(F.data.in_(["poster_large_150", "poster_large_200"]))
async def poster_paper_type_large_selected(callback: CallbackQuery, state: FSMContext):
    paper_map = {
        "poster_large_150": "Постерная бумага 150 г/м²",
        "poster_large_200": "Постерная бумага 200 г/м²"
    }
    await state.update_data(Тип_бумаги=paper_map[callback.data])
    await state.set_state(OrderStates.poster_cutting_large)
    await callback.answer()
    await callback.message.edit_text(
        "Вам нужна подрезка?:",
        reply_markup=get_poster_cutting_keyboard()
    )

# СЕРТИФИКАТЫ
@router.callback_query(F.data == "certificates")
async def certificates_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.certificate_format)
    await state.update_data(service_type="Сертификаты", previous_menu='polygraphy')
    await callback.answer()
    await callback.message.edit_text(
        "🏆 СЕРТИФИКАТЫ\n\nВыберите формат:",
        reply_markup=get_certificate_format_keyboard()
    )

@router.callback_query(F.data.in_(["certificate_a4", "certificate_a5", "certificate_a6", "certificate_euro"]))
async def certificate_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "certificate_a4": "A4 (210×297 мм)",
        "certificate_a5": "A5 (148×210 мм)",
        "certificate_a6": "A6 (105×148 мм)",
        "certificate_euro": "Евроформат (210×99 мм)"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.certificate_paper_type)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип бумаги:",
        reply_markup=get_certificate_paper_type_keyboard()
    )

@router.callback_query(F.data.in_(["certificate_paper_150", "certificate_paper_170", "certificate_paper_250"]))
async def certificate_paper_type_selected(callback: CallbackQuery, state: FSMContext):
    paper_map = {
        "certificate_paper_150": "Мелованная 150 г/м²",
        "certificate_paper_170": "Мелованная 170 г/м²",
        "certificate_paper_250": "Мелованная 250 г/м²"
    }
    await state.update_data(Тип_бумаги=paper_map[callback.data])
    await state.set_state(OrderStates.certificate_color)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите цветность бумаги:",
        reply_markup=get_booklet_color_keyboard()
    )

@router.callback_query(F.data.in_(["certificate_no_lamination", "certificate_gloss_lamination", "certificate_matte_lamination"]))
async def certificate_lamination_selected(callback: CallbackQuery, state: FSMContext):
    lamination_map = {
        "certificate_no_lamination": "Без ламинации",
        "certificate_gloss_lamination": "Глянцевая",
        "certificate_matte_lamination": "Матовая"
    }
    await state.update_data(Ламинация=lamination_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# СТИКЕРЫ С ПЛОТТЕРНОЙ РЕЗКОЙ
@router.callback_query(F.data == "plotter_stickers")
async def sticker_packs_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.sticker_pack_material)
    await state.update_data(service_type="Стикеры с плоттерной резкой", previous_menu='polygraphy')
    await callback.answer()
    await callback.message.edit_text(
        "🔖 СТИКЕРЫ С ПЛОТТЕРНОЙ РЕЗКОЙ\n\nВыберите тип материала:",
        reply_markup=get_sticker_pack_material_keyboard()
    )

@router.callback_query(F.data.in_(["sticker_pack_film_white_matte", "sticker_pack_film_white_glossy",
                                 "sticker_pack_film_clear_matte", "sticker_pack_film_clear_glossy"]))
async def sticker_pack_material_selected(callback: CallbackQuery, state: FSMContext):
    material_map = {
        "sticker_pack_film_white_matte": "Пленка белая мат.",
        "sticker_pack_film_white_glossy": "Пленка белая гл.",
        "sticker_pack_film_clear_matte": "Пленка прозрач. мат.",
        "sticker_pack_film_clear_glossy": "Пленка прозрач. гл."
    }
    await state.update_data(Материал=material_map[callback.data])
    await state.set_state(OrderStates.sticker_pack_format)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите формат материала:",
        reply_markup=get_sticker_pack_format_keyboard()
    )

@router.callback_query(F.data.in_(["sticker_pack_a4", "sticker_pack_a3", "sticker_pack_a5", "sticker_pack_a6"]))
async def sticker_pack_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "sticker_pack_a4": "A4 (210×297 мм)",
        "sticker_pack_a3": "A3 (297×420 мм)",
        "sticker_pack_a5": "A5 стикерпак (148×210 мм)",
        "sticker_pack_a6": "A6 стикерпак (105×148 мм)"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.sticker_pack_color)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите цветность печати:",
        reply_markup=get_sticker_pack_color_keyboard()
    )

@router.callback_query(F.data == "sticker_pack_color_4_0")
async def sticker_pack_color_selected(callback: CallbackQuery, state: FSMContext):
    await state.update_data(Цветность="4+0 (односторонняя)")
    await state.set_state(OrderStates.sticker_pack_cutting)
    await callback.answer()
    await callback.message.edit_text(
        "Вам нужна нарезка на плоттере?:",
        reply_markup=get_sticker_pack_cut_keyboard()
    )

@router.callback_query(F.data.in_(["sticker_pack_cut_yes", "sticker_pack_cut_no"]))
async def sticker_pack_cutting_selected(callback: CallbackQuery, state: FSMContext):
    cutting_map = {
        "sticker_pack_cut_yes": "Да (включена в стоимость)",
        "sticker_pack_cut_no": "Нет (только печать)"
    }
    await state.update_data(Нарезка=cutting_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# ТЕТРАДИ
@router.callback_query(F.data == "notebooks_school")
async def notebooks_school_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.notebook_school_format)
    await state.update_data(service_type="Тетради", previous_menu='polygraphy')
    await callback.answer()
    await callback.message.edit_text(
        "📚 ТЕТРАДИ\n\nВыберите формат:",
        reply_markup=get_notebook_school_format_keyboard()
    )

@router.callback_query(F.data.in_(["notebook_school_a6", "notebook_school_a5", "notebook_school_a4", "notebook_school_a3"]))
async def notebook_school_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "notebook_school_a6": "A6",
        "notebook_school_a5": "A5",
        "notebook_school_a4": "A4",
        "notebook_school_a3": "А3"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.notebook_school_stitching_position)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите позицию сшивания:",
        reply_markup=get_notebook_school_stitching_position_keyboard()
    )

@router.callback_query(F.data.in_(["notebook_school_short_edge", "notebook_school_long_edge"]))
async def notebook_school_stitching_selected(callback: CallbackQuery, state: FSMContext):
    stitch_map = {
        "notebook_school_short_edge": "По короткому краю",
        "notebook_school_long_edge": "По длинному краю"
    }
    await state.update_data(Позиция_сшивания=stitch_map[callback.data])
    await state.set_state(OrderStates.notebook_school_binding_type)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип скрепления:",
        reply_markup=get_notebook_school_binding_type_keyboard()
    )

@router.callback_query(F.data.in_(["notebook_school_spring", "notebook_school_staple"]))
async def notebook_school_binding_selected(callback: CallbackQuery, state: FSMContext):
    binding_map = {
        "notebook_school_spring": "Пружина",
        "notebook_school_staple": "Скрепка"
    }
    await state.update_data(Тип_скрепления=binding_map[callback.data])
    await state.set_state(OrderStates.notebook_school_cover_type)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип обложки/подложки:",
        reply_markup=get_notebook_school_cover_type_keyboard()
    )

@router.callback_query(F.data.in_(["notebook_school_cover_offset_80", "notebook_school_cover_coated_115",
                                 "notebook_school_cover_coated_130", "notebook_school_cover_coated_150",
                                 "notebook_school_cover_coated_170", "notebook_school_cover_coated_250",
                                 "notebook_school_cover_coated_300"]))
async def notebook_school_cover_selected(callback: CallbackQuery, state: FSMContext):
    cover_map = {
        "notebook_school_cover_offset_80": "Офсетная 80 г/м²",
        "notebook_school_cover_coated_115": "Мелованная бумага 115 г/м²",
        "notebook_school_cover_coated_130": "Мелованная бумага 130 г/м²",
        "notebook_school_cover_coated_150": "Мелованная бумага 150 г/м²",
        "notebook_school_cover_coated_170": "Мелованная бумага 170 г/м²",
        "notebook_school_cover_coated_250": "Мелованная бумага 250 г/м²",
        "notebook_school_cover_coated_300": "Мелованная бумага 300 г/м²"
    }
    await state.update_data(Тип_обложки=cover_map[callback.data])
    await state.set_state(OrderStates.notebook_school_cover_print)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите обложка печать:",
        reply_markup=get_notebook_school_cover_print_keyboard()
    )

@router.callback_query(F.data.in_(["notebook_school_cover_bw_single", "notebook_school_cover_bw_double",
                                 "notebook_school_cover_color_single", "notebook_school_cover_color_double"]))
async def notebook_school_cover_print_selected(callback: CallbackQuery, state: FSMContext):
    print_map = {
        "notebook_school_cover_bw_single": "Печать ч/б односторонняя (1+0) только для ВХИ 80гр.",
        "notebook_school_cover_bw_double": "Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.",
        "notebook_school_cover_color_single": "Цветная односторонняя (4+0)",
        "notebook_school_cover_color_double": "Цветная двухсторонняя (4+4)"
    }
    await state.update_data(Обложка_печать=print_map[callback.data])
    await state.set_state(OrderStates.notebook_school_backing_print)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите подложка печать:",
        reply_markup=get_notebook_school_backing_print_keyboard()
    )

@router.callback_query(F.data.in_(["notebook_school_back_bw_single", "notebook_school_back_bw_double",
                                 "notebook_school_back_color_single", "notebook_school_back_color_double"]))
async def notebook_school_backing_print_selected(callback: CallbackQuery, state: FSMContext):
    print_map = {
        "notebook_school_back_bw_single": "Печать ч/б односторонняя (1+0) только для ВХИ 80гр.",
        "notebook_school_back_bw_double": "Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.",
        "notebook_school_back_color_single": "Цветная односторонняя (4+0)",
        "notebook_school_back_color_double": "Цветная двухсторонняя (4+4)"
    }
    await state.update_data(Подложка_печать=print_map[callback.data])
    await state.set_state(OrderStates.notebook_school_inner_block)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите внутренний блок:",
        reply_markup=get_notebook_school_inner_block_keyboard()
    )

@router.callback_query(F.data.in_(["notebook_school_inner_offset_80", "notebook_school_inner_coated_115",
                                 "notebook_school_inner_coated_130", "notebook_school_inner_coated_150",
                                 "notebook_school_inner_coated_170", "notebook_school_inner_coated_250"]))
async def notebook_school_inner_block_selected(callback: CallbackQuery, state: FSMContext):
    inner_map = {
        "notebook_school_inner_offset_80": "Офсетная 80 г/м²",
        "notebook_school_inner_coated_115": "Мелованная бумага 115 г/м²",
        "notebook_school_inner_coated_130": "Мелованная бумага 130 г/м²",
        "notebook_school_inner_coated_150": "Мелованная бумага 150 г/м²",
        "notebook_school_inner_coated_170": "Мелованная бумага 170 г/м²",
        "notebook_school_inner_coated_250": "Мелованная бумага 250 г/м²"
    }
    await state.update_data(Внутренний_блок=inner_map[callback.data])
    await state.set_state(OrderStates.notebook_school_inner_print)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите внутренний блок печать:",
        reply_markup=get_notebook_school_inner_print_keyboard()
    )

@router.callback_query(F.data.in_(["notebook_school_inner_bw_single", "notebook_school_inner_bw_double",
                                 "notebook_school_inner_color_single", "notebook_school_inner_color_double"]))
async def notebook_school_inner_print_selected(callback: CallbackQuery, state: FSMContext):
    print_map = {
        "notebook_school_inner_bw_single": "Печать ч/б односторонняя (1+0) только для ВХИ 80гр.",
        "notebook_school_inner_bw_double": "Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.",
        "notebook_school_inner_color_single": "Цветная односторонняя (4+0)",
        "notebook_school_inner_color_double": "Цветная двухсторонняя (4+4)"
    }
    await state.update_data(Внутренний_блок_печать=print_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# КАТАЛОГИ
@router.callback_query(F.data == "catalogs")
async def catalogs_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.catalog_format)
    await state.update_data(service_type="Каталоги", previous_menu='polygraphy')
    await callback.answer()
    await callback.message.edit_text(
        "📖 КАТАЛОГИ\n\nВыберите формат:",
        reply_markup=get_catalog_format_keyboard()
    )

@router.callback_query(F.data.in_(["catalog_a5", "catalog_a4", "catalog_a3"]))
async def catalog_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "catalog_a5": "A5",
        "catalog_a4": "A4",
        "catalog_a3": "А3"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.catalog_stitching_position)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите позицию сшивания:",
        reply_markup=get_catalog_stitching_position_keyboard()
    )

@router.callback_query(F.data.in_(["catalog_short_edge", "catalog_long_edge"]))
async def catalog_stitching_selected(callback: CallbackQuery, state: FSMContext):
    stitch_map = {
        "catalog_short_edge": "По короткому краю",
        "catalog_long_edge": "По длинному краю"
    }
    await state.update_data(Позиция_сшивания=stitch_map[callback.data])
    await state.set_state(OrderStates.catalog_binding_type)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип скрепления:",
        reply_markup=get_catalog_binding_type_keyboard()
    )

@router.callback_query(F.data.in_(["catalog_spring", "catalog_staple"]))
async def catalog_binding_selected(callback: CallbackQuery, state: FSMContext):
    binding_map = {
        "catalog_spring": "Пружина",
        "catalog_staple": "Скрепка"
    }
    await state.update_data(Тип_скрепления=binding_map[callback.data])
    await state.set_state(OrderStates.catalog_cover_type)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип обложки/подложки:",
        reply_markup=get_catalog_cover_type_keyboard()
    )

@router.callback_query(F.data.in_(["catalog_cover_offset_80", "catalog_cover_coated_115",
                                 "catalog_cover_coated_130", "catalog_cover_coated_150",
                                 "catalog_cover_coated_170", "catalog_cover_coated_250",
                                 "catalog_cover_coated_300"]))
async def catalog_cover_selected(callback: CallbackQuery, state: FSMContext):
    cover_map = {
        "catalog_cover_offset_80": "Офсетная 80 г/м²",
        "catalog_cover_coated_115": "Мелованная бумага 115 г/м²",
        "catalog_cover_coated_130": "Мелованная бумага 130 г/м²",
        "catalog_cover_coated_150": "Мелованная бумага 150 г/м²",
        "catalog_cover_coated_170": "Мелованная бумага 170 г/м²",
        "catalog_cover_coated_250": "Мелованная бумага 250 г/м²",
        "catalog_cover_coated_300": "Мелованная бумага 300 г/м²"
    }
    await state.update_data(Тип_обложки=cover_map[callback.data])
    await state.set_state(OrderStates.catalog_cover_print)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите обложка печать:",
        reply_markup=get_catalog_cover_print_keyboard()
    )

@router.callback_query(F.data.in_(["catalog_cover_bw_single", "catalog_cover_bw_double",
                                 "catalog_cover_color_single", "catalog_cover_color_double"]))
async def catalog_cover_print_selected(callback: CallbackQuery, state: FSMContext):
    print_map = {
        "catalog_cover_bw_single": "Печать ч/б односторонняя (1+0) только для ВХИ 80гр.",
        "catalog_cover_bw_double": "Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.",
        "catalog_cover_color_single": "Цветная односторонняя (4+0)",
        "catalog_cover_color_double": "Цветная двухсторонняя (4+4)"
    }
    await state.update_data(Обложка_печать=print_map[callback.data])
    await state.set_state(OrderStates.catalog_backing_print)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите подложка печать:",
        reply_markup=get_catalog_backing_print_keyboard()
    )

@router.callback_query(F.data.in_(["catalog_back_bw_single", "catalog_back_bw_double",
                                 "catalog_back_color_single", "catalog_back_color_double"]))
async def catalog_backing_print_selected(callback: CallbackQuery, state: FSMContext):
    print_map = {
        "catalog_back_bw_single": "Печать ч/б односторонняя (1+0) только для ВХИ 80гр.",
        "catalog_back_bw_double": "Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.",
        "catalog_back_color_single": "Цветная односторонняя (4+0)",
        "catalog_back_color_double": "Цветная двухсторонняя (4+4)"
    }
    await state.update_data(Подложка_печать=print_map[callback.data])
    await state.set_state(OrderStates.catalog_inner_block)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите внутренний блок:",
        reply_markup=get_catalog_inner_block_keyboard()
    )

@router.callback_query(F.data.in_(["catalog_inner_offset_80", "catalog_inner_coated_115",
                                 "catalog_inner_coated_130", "catalog_inner_coated_150",
                                 "catalog_inner_coated_170", "catalog_inner_coated_250"]))
async def catalog_inner_block_selected(callback: CallbackQuery, state: FSMContext):
    inner_map = {
        "catalog_inner_offset_80": "Офсетная 80 г/м²",
        "catalog_inner_coated_115": "Мелованная бумага 115 г/м²",
        "catalog_inner_coated_130": "Мелованная бумага 130 г/м²",
        "catalog_inner_coated_150": "Мелованная бумага 150 г/м²",
        "catalog_inner_coated_170": "Мелованная бумага 170 г/м²",
        "catalog_inner_coated_250": "Мелованная бумага 250 г/м²"
    }
    await state.update_data(Внутренний_блок=inner_map[callback.data])
    await state.set_state(OrderStates.catalog_inner_print)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите внутренний блок печать:",
        reply_markup=get_catalog_inner_print_keyboard()
    )

@router.callback_query(F.data.in_(["catalog_inner_bw_single", "catalog_inner_bw_double",
                                 "catalog_inner_color_single", "catalog_inner_color_double"]))
async def catalog_inner_print_selected(callback: CallbackQuery, state: FSMContext):
    print_map = {
        "catalog_inner_bw_single": "Печать ч/б односторонняя (1+0) только для ВХИ 80гр.",
        "catalog_inner_bw_double": "Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.",
        "catalog_inner_color_single": "Цветная односторонняя (4+0)",
        "catalog_inner_color_double": "Цветная двухсторонняя (4+4)"
    }
    await state.update_data(Внутренний_блок_печать=print_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )
