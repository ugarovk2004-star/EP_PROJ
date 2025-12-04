from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from states.order_states import OrderStates
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.interior import *
from keyboards.polygraphy import get_poster_format_keyboard, get_poster_paper_type_a3_keyboard, get_poster_paper_type_large_keyboard, get_poster_cutting_keyboard
from keyboards.copycenter import get_files_keyboard, get_comment_keyboard, get_order_confirmation_keyboard
from utils.order_message import create_order_message, send_order_to_manager

router = Router()

# Обработчик главного меню интерьерной печати через callback
@router.callback_query(F.data == "interior")
async def interior_main(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.waiting_for_files)
    await state.update_data(previous_menu='main')
    await callback.answer()
    await callback.message.edit_text(
        "Раздел ИНТЕРЬЕРНАЯ ПЕЧАТЬ. Выберите продукт:",
        reply_markup=get_interior_main_keyboard()
    )

# ПЛАКАТЫ (дублирует полиграфию)
@router.callback_query(F.data == "interior_posters")
async def interior_posters_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.interior_poster_format)
    await state.update_data(service_type="Интерьерные плакаты", previous_menu='interior')
    await callback.answer()
    await callback.message.edit_text(
        "📊 ИНТЕРЬЕРНЫЕ ПЛАКАТЫ\n\nВыберите формат:",
        reply_markup=get_poster_format_keyboard()
    )

# ТАБЛИЧКИ
@router.callback_query(F.data == "interior_signs")
async def signs_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.sign_type)
    await state.update_data(service_type="Таблички", previous_menu='interior')
    await callback.answer()
    await callback.message.edit_text(
        "🏢 ТАБЛИЧКИ\n\nВыберите тип таблички:",
        reply_markup=get_sign_type_keyboard()
    )

@router.callback_query(F.data.in_(["sign_office", "sign_outdoor"]))
async def sign_type_selected(callback: CallbackQuery, state: FSMContext):
    type_map = {
        "sign_office": "Офисные таблички",
        "sign_outdoor": "Уличные таблички"
    }
    await state.update_data(Тип_таблички=type_map[callback.data])
    await state.set_state(OrderStates.sign_size)
    await callback.answer()
    await callback.message.edit_text(
        "Введите размер таблички в формате Ш×В (мм):"
    )

@router.message(OrderStates.sign_size)
async def sign_size_entered(message: Message, state: FSMContext):
    await state.update_data(Размер=message.text)
    await state.set_state(OrderStates.sign_material)
    await message.edit_text(
        "Выберите материал:",
        reply_markup=get_sign_material_keyboard()
    )

@router.callback_query(F.data.in_(["sign_pvc_3mm", "sign_pvc_5mm", "sign_two_layer"]))
async def sign_material_selected(callback: CallbackQuery, state: FSMContext):
    material_map = {
        "sign_pvc_3mm": "Пластик ПВХ-3 мм",
        "sign_pvc_5mm": "Пластик ПВХ-5 мм",
        "sign_two_layer": "Двухслойный пластик"
    }
    await state.update_data(Материал=material_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# КАРТИНЫ НА ХОЛСТЕ
@router.callback_query(F.data == "interior_canvas")
async def canvas_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.canvas_size)
    await state.update_data(service_type="Картины на холсте", previous_menu='interior')
    await callback.answer()
    await callback.message.edit_text(
        "🎨 КАРТИНЫ НА ХОЛСТЕ\n\nВыберите размер холста:",
        reply_markup=get_canvas_size_keyboard()
    )

@router.callback_query(F.data.in_(["canvas_20x30", "canvas_30x40", "canvas_40x50", "canvas_40x60",
                                 "canvas_50x50", "canvas_50x70", "canvas_60x80", "canvas_70x100",
                                 "canvas_80x120"]))
async def canvas_size_selected(callback: CallbackQuery, state: FSMContext):
    size_map = {
        "canvas_20x30": "20×30 см",
        "canvas_30x40": "30×40 см",
        "canvas_40x50": "40×50 см",
        "canvas_40x60": "40×60 см",
        "canvas_50x50": "50×50 см",
        "canvas_50x70": "50×70 см",
        "canvas_60x80": "60×80 см",
        "canvas_70x100": "70×100 см",
        "canvas_80x120": "80×120 см"
    }
    await state.update_data(Размер=size_map[callback.data])
    await state.set_state(OrderStates.canvas_framing)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите оформление:",
        reply_markup=get_canvas_framing_keyboard()
    )

@router.callback_query(F.data.in_(["canvas_no_frame", "canvas_gallery_stretch"]))
async def canvas_framing_selected(callback: CallbackQuery, state: FSMContext):
    framing_map = {
        "canvas_no_frame": "Без подрамника",
        "canvas_gallery_stretch": "Галерейная натяжка"
    }
    await state.update_data(Оформление=framing_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# ПЕЧАТЬ НА БАННЕРЕ
@router.callback_query(F.data == "interior_banner")
async def banner_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.banner_print_type)
    await state.update_data(service_type="Печать на баннере", previous_menu='interior')
    await callback.answer()
    await callback.message.edit_text(
        "🪧 ПЕЧАТЬ НА БАННЕРЕ\n\nВыберите тип печати:",
        reply_markup=get_banner_print_type_keyboard()
    )

@router.callback_query(F.data.in_(["banner_wide_format", "banner_interior"]))
async def banner_print_type_selected(callback: CallbackQuery, state: FSMContext):
    type_map = {
        "banner_wide_format": "Широкоформатная",
        "banner_interior": "Интерьерная"
    }
    await state.update_data(Тип_печати=type_map[callback.data])
    await state.set_state(OrderStates.banner_size)
    await callback.answer()
    await callback.message.edit_text(
        "Введите размер баннера в формате Ш×В (мм):"
    )

@router.message(OrderStates.banner_size)
async def banner_size_entered(message: Message, state: FSMContext):
    await state.update_data(Размер=message.text)
    await state.set_state(OrderStates.banner_edge_processing)
    await message.edit_text(
        "Выберите обработку краев:",
        reply_markup=get_banner_edge_processing_keyboard()
    )

@router.callback_query(F.data.in_(["banner_no_edge", "banner_edge_reinforcement"]))
async def banner_edge_processing_selected(callback: CallbackQuery, state: FSMContext):
    edge_map = {
        "banner_no_edge": "Без обработки",
        "banner_edge_reinforcement": "Укрепление края"
    }
    await state.update_data(Края=edge_map[callback.data])
    
    if callback.data == "banner_edge_reinforcement":
        await state.set_state(OrderStates.banner_grommets)
        await callback.answer()
        await callback.message.edit_text(
            "Выберите крепление:",
            reply_markup=get_banner_grommets_keyboard()
        )
    else:
        await state.set_state(OrderStates.waiting_for_quantity)
        await callback.answer()
        await callback.message.edit_text(
            "Введите количество экземпляров (только цифры):"
        )

@router.callback_query(F.data.in_(["banner_no_grommets", "banner_grommets_30cm", "banner_grommets_50cm"]))
async def banner_grommets_selected(callback: CallbackQuery, state: FSMContext):
    grommets_map = {
        "banner_no_grommets": "Без люверсов",
        "banner_grommets_30cm": "Люверсы через 30 см",
        "banner_grommets_50cm": "Люверсы через 50 см"
    }
    await state.update_data(Крепление=grommets_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# ПЕЧАТЬ НА САМОКЛЕЮЩЕЙСЯ ПЛЁНКЕ
@router.callback_query(F.data == "interior_sticker_film")
async def interior_stickers_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.interior_sticker_film_type)
    await state.update_data(service_type="Печать на самоклеющейся плёнке", previous_menu='interior')
    await callback.answer()
    await callback.message.edit_text(
        "🏷️ ПЕЧАТЬ НА САМОКЛЕЮЩЕЙСЯ ПЛЁНКЕ\n\nВыберите тип плёнки:",
        reply_markup=get_interior_sticker_film_type_keyboard()
    )

@router.callback_query(F.data.in_(["interior_film_white_matte", "interior_film_white_glossy",
                                 "interior_film_clear_matte", "interior_film_clear_glossy"]))
async def interior_sticker_film_selected(callback: CallbackQuery, state: FSMContext):
    film_map = {
        "interior_film_white_matte": "Пленка белая мат.",
        "interior_film_white_glossy": "Пленка белая гл.",
        "interior_film_clear_matte": "Пленка прозрач. мат.",
        "interior_film_clear_glossy": "Пленка прозрач. гл."
    }
    await state.update_data(Тип_плёнки=film_map[callback.data])
    await state.set_state(OrderStates.interior_sticker_size)
    await callback.answer()
    await callback.message.edit_text(
        "Введите размер в формате Ш×В (мм):"
    )

@router.message(OrderStates.interior_sticker_size)
async def interior_sticker_size_entered(message: Message, state: FSMContext):
    await state.update_data(Размер=message.text)
    await state.set_state(OrderStates.interior_sticker_processing)
    await message.edit_text(
        "Выберите дополнительную обработку:",
        reply_markup=get_interior_sticker_processing_keyboard()
    )

@router.callback_query(F.data.in_(["interior_no_processing", "interior_lamination", 
                                 "interior_cutting", "interior_plotter_cut"]))
async def interior_sticker_processing_selected(callback: CallbackQuery, state: FSMContext):
    processing_map = {
        "interior_no_processing": "Без обработки",
        "interior_lamination": "Ламинация",
        "interior_cutting": "Подрезка напечатанного макета",
        "interior_plotter_cut": "Плоттерная резка"
    }
    await state.update_data(Доп_обработка=processing_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )