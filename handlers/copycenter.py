from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from states.order_states import OrderStates
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.copycenter import (
    get_copycenter_main_keyboard,
    get_bw_format_keyboard,
    get_bw_print_type_keyboard,
    get_bw_additional_services_keyboard,
    get_color_format_keyboard,
    get_color_paper_type_keyboard,
    get_color_additional_services_keyboard,
    get_files_keyboard,
    get_comment_keyboard,
    get_order_confirmation_keyboard,
    get_risograph_format_keyboard,
    get_risograph_quantity_keyboard,
    get_risograph_color_keyboard,
    get_risograph_print_type_keyboard
)
from utils.order_message import create_order_message, send_order_to_manager, create_order_summary
from utils.user_store import get_user_info

router = Router()

# Обработчики главного меню копицентра (через callback)
@router.callback_query(F.data == "copycenter")
async def copycenter_main(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.waiting_for_files)
    await state.update_data(previous_menu='main')
    await callback.answer()
    await callback.message.edit_text(
        "Раздел КОПИЦЕНТР. Выберите тип печати:",
        reply_markup=get_copycenter_main_keyboard()
    )

# Обработчики Ч/Б печати
@router.callback_query(F.data == "bw_print")
async def bw_print_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.bw_format)
    await state.update_data(service_type="Ч/Б печать", previous_menu='copycenter')
    await callback.answer()
    await callback.message.edit_text(
        "🖨️ Ч/Б ПЕЧАТЬ\n\n"
        "Выберите формат:",
        reply_markup=get_bw_format_keyboard()
    )

@router.callback_query(F.data.in_(["bw_a4", "bw_a3"]))
async def bw_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "bw_a4": "A4",
        "bw_a3": "A3"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.bw_print_type)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип печати:",
        reply_markup=get_bw_print_type_keyboard()
    )

@router.callback_query(F.data.in_(["bw_single", "bw_double", "bw_booklet"]))
async def bw_print_type_selected(callback: CallbackQuery, state: FSMContext):
    type_map = {
        "bw_single": "Односторонняя",
        "bw_double": "Двусторонняя",
        "bw_booklet": "Печать брошюры"
    }
    await state.update_data(Тип_печати=type_map[callback.data])
    await state.set_state(OrderStates.bw_additional_services)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите дополнительные услуги:",
        reply_markup=get_bw_additional_services_keyboard()
    )

@router.callback_query(F.data.in_(["bw_spring", "bw_plastic_covers", "bw_stapling", "bw_skip_services"]))
async def bw_additional_services_selected(callback: CallbackQuery, state: FSMContext):
    services_map = {
        "bw_spring": "Брошюровка на металлическую пружину",
        "bw_plastic_covers": "Пластиковые обложки",
        "bw_stapling": "Скрепление брошюры",
        "bw_skip_services": "Пропустить"
    }
    
    if callback.data != "bw_skip_services":
        await state.update_data(additional_services=services_map[callback.data])
    
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# Обработчики цветной печати
@router.callback_query(F.data == "color_print")
async def color_print_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.color_format)
    await state.update_data(service_type="Цветная печать", previous_menu='copycenter')
    await callback.answer()
    await callback.message.edit_text(
        "🎨 ЦВЕТНАЯ ПЕЧАТЬ\n\n"
        "Выберите формат:",
        reply_markup=get_color_format_keyboard()
    )

@router.callback_query(F.data.in_(["color_a7", "color_a6", "color_euro", "color_a5", "color_a4", "color_a3"]))
async def color_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "color_a7": "A7 (74×105 мм)",
        "color_a6": "A6 (105×148 мм)",
        "color_euro": "Евроформат (210×99 мм)",
        "color_a5": "A5 (148×210 мм)",
        "color_a4": "A4 (210×297 мм)",
        "color_a3": "A3 (297×420 мм)"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.color_paper_type)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип бумаги:",
        reply_markup=get_color_paper_type_keyboard()
    )

@router.callback_query(F.data.startswith("color_"))
async def color_paper_type_selected(callback: CallbackQuery, state: FSMContext):
    paper_map = {
        "color_offset_80": "Офсетная 80 г/м²",
        "color_coated_115": "Мелованная 115 г/м²",
        "color_coated_130": "Мелованная 130 г/м²",
        "color_coated_170": "Мелованная 170 г/м²",
        "color_coated_250": "Мелованная 250 г/м²",
        "color_coated_300": "Мелованная 300 г/м²",
        "color_film_white_matte": "Пленка белая мат.",
        "color_film_white_glossy": "Пленка белая гл.",
        "color_film_clear_matte": "Пленка прозрач. мат.",
        "color_film_clear_glossy": "Пленка прозрач. гл."
    }
    
    if callback.data in paper_map:
        await state.update_data(Тип_бумаги=paper_map[callback.data])
        await state.set_state(OrderStates.color_print_type)
        await callback.answer()
        await callback.message.edit_text(
            "Выберите тип печати:",
            reply_markup=get_bw_print_type_keyboard()  # Та же клавиатура, что и для Ч/Б
        )
    elif callback.data in ["color_spring", "color_plastic_covers", "color_stapling", "color_cutting", "color_skip_services"]:
        # Обработка дополнительных услуг для цветной печати
        services_map = {
            "color_spring": "Брошюровка на металлическую пружину",
            "color_plastic_covers": "Пластиковые обложки",
            "color_stapling": "Скрепление брошюры",
            "color_cutting": "Подрезка",
            "color_skip_services": "Пропустить"
        }
        
        if callback.data != "color_skip_services":
            await state.update_data(Доп_услуги=services_map[callback.data])
        
        await state.set_state(OrderStates.waiting_for_quantity)
        await callback.answer()
        await callback.message.edit_text(
            "Введите количество экземпляров (только цифры):"
        )

# Обработчик количества (общий для всех услуг)
@router.message(OrderStates.waiting_for_quantity, F.text.regexp(r'^\d+$'))
async def quantity_entered(message: Message, state: FSMContext):
    await state.update_data(Количество=message.text)
    await state.set_state(OrderStates.waiting_for_files)
    await message.answer(
        "Теперь прикрепите файлы для печати:",
        reply_markup=get_files_keyboard()
    )

# Обработчик файлов
@router.message(OrderStates.waiting_for_files, F.document | F.photo)
async def files_received(message: Message, state: FSMContext):
    files_info = []
    files_data = []
    
    if message.document:
        file_info = f"📄 {message.document.file_name}"
        files_info.append(file_info)
        files_data.append({
            'type': 'document',
            'file_id': message.document.file_id,
            'caption': f"Документ: {message.document.file_name}"
        })
    elif message.photo:
        photo = message.photo[-1]
        file_info = f"🖼️ Фото"
        files_info.append(file_info)
        files_data.append({
            'type': 'photo', 
            'file_id': photo.file_id,
            'caption': "Фото от клиента"
        })
    
    current_data = await state.get_data()
    existing_files_info = current_data.get('files_info', [])
    existing_files_data = current_data.get('files_data', [])
    
    existing_files_info.extend(files_info)
    existing_files_data.extend(files_data)
    
    await state.update_data(
        files_info=existing_files_info,
        files_data=existing_files_data
    )
    
    await state.set_state(OrderStates.waiting_for_comment)
    await message.answer(
        f"✅ Файл получен! Всего файлов: {len(existing_files_info)}\n"
        "Хотите добавить примечание к заказу?",
        reply_markup=get_comment_keyboard()
    )

# Исправленный обработчик comment_action
@router.callback_query(F.data.in_(["add_note", "skip_note"]))
async def comment_action(callback: CallbackQuery, state: FSMContext):
    if callback.data == "add_note":
        await state.set_state(OrderStates.waiting_for_comment_text)
        await callback.answer()
        await callback.message.edit_text(
            "Введите примечание к заказу:"
        )
    else:  # skip_note
        data = await state.get_data()
        service_type = data.get('service_type', 'Неизвестная услуга')
        
        # Исправленный вызов create_order_summary
        summary = create_order_summary(
            user_id=callback.from_user.id,
            service_type=service_type,
            order_data=data,
            files_info=data.get('files_info', []),
            comment=data.get('comment')
        )
        
        await callback.answer()
        await callback.message.edit_text(
            f"Заказ {service_type} готов к отправке!\n\n"
            f"Проверьте детали заказа и нажмите кнопку для отправки менеджеру:\n\n{summary}",
            reply_markup=get_order_confirmation_keyboard()
        )

# Исправленный обработчик comment_text_received
@router.message(OrderStates.waiting_for_comment_text)
async def comment_text_received(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    data = await state.get_data()
    service_type = data.get('service_type', 'Неизвестная услуга')
    
    # Исправленный вызов create_order_summary
    summary = create_order_summary(
        user_id=message.from_user.id,
        service_type=service_type,
        order_data=data,
        files_info=data.get('files_info', []),
        comment=data.get('comment')
    )
    
    await message.answer(
        f"Заказ {service_type} готов к отправке!\n\n"
        f"Проверьте детали заказа и нажмите кнопку для отправки менеджеру:\n\n{summary}",
        reply_markup=get_order_confirmation_keyboard()
    )

# # Исправленный обработчик confirm_order_inline
# @router.callback_query(F.data == "send_order")
# async def confirm_order_inline(callback: CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     user_info = get_user_info(callback.from_user.id) or {}
    
#     order_message = create_order_message(
#         username=callback.from_user.username,
#         user_id=callback.from_user.id,
#         # Исправлено: убраны лишние параметры
#         service_type=data.get('service_type', 'Неизвестная услуга'),
#         order_data=data,
#         files_info=data.get('files_info', []),
#         comment=data.get('comment')
#     )
    
#     # Отправляем менеджеру
#     success = await send_order_to_manager(callback.bot, order_message, data.get('files_data', []))
    
#     await callback.answer()
#     await callback.message.edit_text("Идёт загрузка...", reply_markup=ReplyKeyboardRemove())
    
#     if success:
#         await callback.message.edit_text(
#             "✅ Ваш заказ успешно отправлен менеджеру!\n"
#             "Ожидайте уведомления о принятии заказа в работу...\n",
#             reply_markup=get_main_menu_keyboard()
#         )
#     else:
#         await callback.message.edit_text(
#             "❌ Произошла ошибка при отправке заказа. Пожалуйста, попробуйте позже.",
#             reply_markup=get_main_menu_keyboard()
#         )
    
#     await state.clear()

# РИЗОГРАФ
@router.callback_query(F.data == "risograph")
async def risograph_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.risograph_format)
    await state.update_data(service_type="Ризограф", previous_menu='copycenter')
    await callback.answer()
    await callback.message.edit_text(
        "🖨️ РИЗОГРАФ\n\nВыберите формат:",
        reply_markup=get_risograph_format_keyboard()
    )

@router.callback_query(F.data.in_(["riso_a4", "riso_a3"]))
async def risograph_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "riso_a4": "A4",
        "riso_a3": "А3"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.risograph_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите количество экземпляров:",
        reply_markup=get_risograph_quantity_keyboard()
    )

@router.callback_query(F.data.in_(["riso_500", "riso_1000", "riso_1500", "riso_2000", "riso_3000", "riso_5000", "riso_10000"]))
async def risograph_quantity_selected(callback: CallbackQuery, state: FSMContext):
    quantity_map = {
        "riso_500": "500",
        "riso_1000": "1000",
        "riso_1500": "1500",
        "riso_2000": "2000",
        "riso_3000": "3000",
        "riso_5000": "5000",
        "riso_10000": "10000"
    }
    await state.update_data(Количество=quantity_map[callback.data])
    await state.set_state(OrderStates.risograph_color)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите цвет печати:",
        reply_markup=get_risograph_color_keyboard()
    )

@router.callback_query(F.data.in_(["riso_black", "riso_red", "riso_black_red"]))
async def risograph_color_selected(callback: CallbackQuery, state: FSMContext):
    color_map = {
        "riso_black": "Черный",
        "riso_red": "Красный",
        "riso_black_red": "Черный/Красный"
    }
    await state.update_data(Цвет=color_map[callback.data])
    await state.set_state(OrderStates.risograph_print_type)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип печати:",
        reply_markup=get_risograph_print_type_keyboard()
    )

@router.callback_query(F.data.in_(["riso_single", "riso_double"]))
async def risograph_print_type_selected(callback: CallbackQuery, state: FSMContext):
    type_map = {
        "riso_single": "Односторонняя",
        "riso_double": "Двухсторонний"
    }
    await state.update_data(Тип_печати=type_map[callback.data])
    await state.set_state(OrderStates.waiting_for_files)
    await callback.answer()
    await callback.message.edit_text(
        "Теперь прикрепите файлы для печати:",
        reply_markup=get_files_keyboard()
    )

# Общие обработчики для кнопок "Написать менеджеру" и "Главное меню" в inline-клавиатурах
@router.callback_query(F.data == "write_manager")
async def write_to_manager_inline(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.writing_to_manager)
    await callback.answer()
    await callback.message.edit_text(
        "📝 Напишите ваше сообщение для менеджера. После отправки сообщения вы вернетесь в главное меню."
    )

# @router.callback_query(F.data == "main_menu")
# async def main_menu_inline(callback: CallbackQuery, state: FSMContext):
#     await state.clear()
#     await callback.answer()
#     await callback.message.edit_text(
#         "Главное меню:",
#         reply_markup=get_main_menu_keyboard()
#     )
