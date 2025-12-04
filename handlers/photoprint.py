from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from states.order_states import OrderStates
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.photoprint import get_photo_format_keyboard, get_photo_print_type_keyboard
from keyboards.copycenter import get_files_keyboard, get_comment_keyboard, get_order_confirmation_keyboard
from utils.order_message import create_order_message, send_order_to_manager

router = Router()

# Обработчик фотопечати через callback
@router.callback_query(F.data == "photoprint")
async def photoprint_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.photo_format)
    await state.update_data(service_type="Фотопечать", previous_menu='main')
    
    info_text = (
        "📸 ФОТОПЕЧАТЬ\n\n"
        "ℹ️ Печать производится только на глянцевой бумаге\n\n"
        "Выберите формат бумаги:"
    )
    
    await callback.answer()
    await callback.message.edit_text(info_text, reply_markup=get_photo_format_keyboard())

@router.callback_query(F.data.in_(["photo_10x15", "photo_15x21", "photo_21x30"]))
async def photo_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "photo_10x15": "10×15",
        "photo_15x21": "15×21",
        "photo_21x30": "21×30"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.photo_print_type)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип печати фото:",
        reply_markup=get_photo_print_type_keyboard()
    )

@router.callback_query(F.data.in_(["photo_with_margins", "photo_without_margins"]))
async def photo_print_type_selected(callback: CallbackQuery, state: FSMContext):
    type_map = {
        "photo_with_margins": "С полями (изображение полностью, возможны белые поля)",
        "photo_without_margins": "Без полей (изображение займёт всю площадь, возможна обрезка краёв)"
    }
    await state.update_data(Тип_печати=type_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )