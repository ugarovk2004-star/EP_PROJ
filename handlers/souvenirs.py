from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from states.order_states import OrderStates
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.souvenirs import *
from keyboards.copycenter import get_files_keyboard, get_comment_keyboard, get_order_confirmation_keyboard
from utils.order_message import create_order_message, send_order_to_manager

router = Router()

# Обработчик главного меню сувениров через callback
@router.callback_query(F.data == "souvenirs")
async def souvenirs_main(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.waiting_for_files)
    await state.update_data(previous_menu='main')
    await callback.answer()
    await callback.message.edit_text(
        "Раздел СУВЕНИРЫ. Выберите продукт:",
        reply_markup=get_souvenirs_main_keyboard()
    )

# РУЧКИ С ЛОГОТИПОМ
@router.callback_query(F.data == "souvenirs_pens")
async def pens_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.pen_material)
    await state.update_data(service_type="Ручки с логотипом", previous_menu='souvenirs')
    await callback.answer()
    await callback.message.edit_text(
        "✏️ РУЧКИ С ЛОГОТИПОМ\n\nВыберите материал корпуса:",
        reply_markup=get_pen_material_keyboard()
    )

@router.callback_query(F.data.in_(["pen_plastic", "pen_craft"]))
async def pen_material_plastic_craft(callback: CallbackQuery, state: FSMContext):
    material_map = {
        "pen_plastic": "Пластик",
        "pen_craft": "Крафт (картон)"
    }
    await state.update_data(Материал=material_map[callback.data])
    await state.set_state(OrderStates.pen_color)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите цвет корпуса:",
        reply_markup=get_pen_color_keyboard()
    )

@router.callback_query(F.data == "pen_metal")
async def pen_material_metal(callback: CallbackQuery, state: FSMContext):
    await state.update_data(Материал="Металл")
    await state.set_state(OrderStates.pen_application)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите способ нанесения:",
        reply_markup=get_pen_application_keyboard()
    )

@router.callback_query(F.data.in_(["pen_laser_engraving", "pen_uv_print"]))
async def pen_application_selected(callback: CallbackQuery, state: FSMContext):
    application_map = {
        "pen_laser_engraving": "Лазерная гравировка",
        "pen_uv_print": "УФ-печать"
    }
    await state.update_data(Нанесение=application_map[callback.data])
    await state.set_state(OrderStates.pen_color)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите цвет корпуса:",
        reply_markup=get_pen_color_keyboard()
    )

@router.callback_query(F.data.in_(["pen_blue", "pen_red", "pen_black", "pen_white", "pen_silver", "pen_gold"]))
async def pen_color_selected(callback: CallbackQuery, state: FSMContext):
    color_map = {
        "pen_blue": "Синий",
        "pen_red": "Красный",
        "pen_black": "Черный",
        "pen_white": "Белый",
        "pen_silver": "Серебристый",
        "pen_gold": "Золотистый"
    }
    await state.update_data(Цвет=color_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# ФУТБОЛКИ
@router.callback_query(F.data == "souvenirs_tshirts")
async def tshirts_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.tshirt_size)
    await state.update_data(service_type="Футболки", previous_menu='souvenirs')
    await callback.answer()
    await callback.message.edit_text(
        "👕 ФУТБОЛКИ\n\nВыберите размер:",
        reply_markup=get_tshirt_size_keyboard()
    )

@router.callback_query(F.data.in_(["tshirt_xs", "tshirt_s", "tshirt_m", "tshirt_l", "tshirt_xl", "tshirt_xxl", "tshirt_xxxl"]))
async def tshirt_size_selected(callback: CallbackQuery, state: FSMContext):
    size_map = {
        "tshirt_xs": "XS",
        "tshirt_s": "S",
        "tshirt_m": "M",
        "tshirt_l": "L",
        "tshirt_xl": "XL",
        "tshirt_xxl": "XXL",
        "tshirt_xxxl": "XXXL"
    }
    await state.update_data(Размер=size_map[callback.data])
    await state.set_state(OrderStates.tshirt_material)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите материал и цвет:",
        reply_markup=get_tshirt_material_keyboard()
    )

@router.callback_query(F.data.in_(["tshirt_cotton_100_white", "tshirt_cotton_100_black", "tshirt_cotton_poly_white"]))
async def tshirt_material_selected(callback: CallbackQuery, state: FSMContext):
    material_map = {
        "tshirt_cotton_100_white": "Хлопок 100% (белый)",
        "tshirt_cotton_100_black": "Хлопок 100% (черный)",
        "tshirt_cotton_poly_white": "Хлопок 50% / Полиэстер 50% (белый)"
    }
    await state.update_data(Материал=material_map[callback.data])
    await state.set_state(OrderStates.tshirt_print_position)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите расположение принта:",
        reply_markup=get_tshirt_print_position_keyboard()
    )

@router.callback_query(F.data.in_(["tshirt_print_chest", "tshirt_print_back"]))
async def tshirt_print_position_selected(callback: CallbackQuery, state: FSMContext):
    position_map = {
        "tshirt_print_chest": "На груди",
        "tshirt_print_back": "На спине"
    }
    await state.update_data(Позиция=position_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# КРУЖКИ
@router.callback_query(F.data == "souvenirs_mugs")
async def mugs_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.mug_type)
    await state.update_data(service_type="Кружки", previous_menu='souvenirs')
    await callback.answer()
    await callback.message.edit_text(
        "☕ КРУЖКИ\n\nВыберите тип кружки:",
        reply_markup=get_mug_type_keyboard()
    )

@router.callback_query(F.data.in_(["mug_white", "mug_colored"]))
async def mug_type_selected(callback: CallbackQuery, state: FSMContext):
    type_map = {
        "mug_white": "Кружка белая",
        "mug_colored": "Кружка цветная внутри, цветная ручка"
    }
    await state.update_data(Тип_кружки=type_map[callback.data])
    await state.set_state(OrderStates.mug_print_position)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите расположение принта:",
        reply_markup=get_mug_print_position_keyboard()
    )

@router.callback_query(F.data.in_(["mug_print_one_side", "mug_print_around", "mug_print_two_sides"]))
async def mug_print_position_selected(callback: CallbackQuery, state: FSMContext):
    position_map = {
        "mug_print_one_side": "С одной стороны",
        "mug_print_around": "По кругу",
        "mug_print_two_sides": "С двух сторон"
    }
    await state.update_data(Позиция=position_map[callback.data])
    await state.set_state(OrderStates.mug_packaging)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите дополнительную упаковку:",
        reply_markup=get_mug_packaging_keyboard()
    )

@router.callback_query(F.data.in_(["mug_no_packaging", "mug_gift_box"]))
async def mug_packaging_selected(callback: CallbackQuery, state: FSMContext):
    packaging_map = {
        "mug_no_packaging": "Без упаковки",
        "mug_gift_box": "Подарочная коробка"
    }
    await state.update_data(Упаковка=packaging_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )