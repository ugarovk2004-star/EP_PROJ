from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from states.order_states import OrderStates
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.stamps import *
from keyboards.copycenter import get_files_keyboard, get_comment_keyboard, get_order_confirmation_keyboard
from utils.order_message import create_order_message, send_order_to_manager

router = Router()

# Обработчик главного меню печатей и штампов через callback
@router.callback_query(F.data == "stamps")
async def stamps_main(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.stamp_type)
    await state.update_data(service_type="Изготовление печатей и штампов", previous_menu='main')
    
    info_text = (
        "🖋️ ИЗГОТОВЛЕНИЕ ПЕЧАТЕЙ И ШТАМПОВ\n\n"
        "ℹ️ При заказе печати ООО необходимо предоставить:\n"
        "• Учредительные документы ООО\n"
        "• Доверенность на получение печати\n\n"
        "ℹ️ Индивидуальный предприниматель получает печать с паспортом\n\n"
        "ℹ️ При заказе печати врача необходимо предоставить диплом врача\n\n"
        "Выберите тип печати:"
    )
    
    await callback.answer()
    await callback.message.edit_text(info_text, reply_markup=get_stamps_main_keyboard())

@router.callback_query(F.data.in_(["stamp_auto", "stamp_pocket", "stamp_facsimile", "stamp_cliche"]))
async def stamp_type_selected(callback: CallbackQuery, state: FSMContext):
    type_map = {
        "stamp_auto": "АВТОМАТИЧЕСКАЯ ПЕЧАТЬ",
        "stamp_pocket": "КАРМАННАЯ ПЕЧАТЬ",
        "stamp_facsimile": "ФАКСИМИЛЕ",
        "stamp_cliche": "КЛИШЕ БЕЗ ОСНАСТКИ"
    }
    await state.update_data(Тип=type_map[callback.data])
    await state.set_state(OrderStates.stamp_format)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите формат печати:",
        reply_markup=get_stamp_format_keyboard()
    )

@router.callback_query(F.data.in_(["stamp_round_30", "stamp_round_40", "stamp_rectangular"]))
async def stamp_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "stamp_round_30": "Круглая 30 мм",
        "stamp_round_40": "Круглая 40 мм",
        "stamp_rectangular": "Прямоугольный штамп"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.stamp_ink_color)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите цвет штемпельной подушки:",
        reply_markup=get_stamp_ink_color_keyboard()
    )

@router.callback_query(F.data.in_(["stamp_ink_black", "stamp_ink_purple", "stamp_ink_red", "stamp_ink_green"]))
async def stamp_ink_color_selected(callback: CallbackQuery, state: FSMContext):
    color_map = {
        "stamp_ink_black": "Черный",
        "stamp_ink_purple": "Фиолетовый",
        "stamp_ink_red": "Красный",
        "stamp_ink_green": "Зелёный"
    }
    await state.update_data(Цвет=color_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.answer(
        "Введите количество экземпляров (только цифры):"
    )