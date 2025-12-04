from aiogram import Router, F
from aiogram.types import Message, FSInputFile, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from datetime import datetime
from config import RECIPIENT_ID


from states.order_states import OrderStates
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.copycenter import get_files_keyboard, get_comment_keyboard, get_order_confirmation_keyboard
from utils.order_message import create_order_message, send_order_to_manager, create_order_summary
from utils.user_store import get_user_info, set_user_info

# Импортируем все клавиатуры
# from keyboards.copycenter import *
# from keyboards.polygraphy import *
# from keyboards.packaging import *
# from keyboards.interior import *
# from keyboards.souvenirs import *
# from keyboards.stamps import *
# from keyboards.photoprint import *

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext, bot):
    await state.clear()
    user = get_user_info(message.from_user.id)
    

    # try:
    #     await message.answer_photo(photo=FSInputFile("start_pic.jpg"))
    # except Exception as e:
    #     print(f"Не удалось отправить фото: {e}")

    if user:
        # Убираем старую клавиатуру, затем показываем inline-меню
        # await message.answer("Клавиатура скрыта.", reply_markup=ReplyKeyboardRemove())
        await message.answer_photo(
                photo=FSInputFile("start_pic.jpg"),
                caption='Привет! Я твой личный помощник Лия!\n'
                        "Данные пользователя сохранены. Выберите раздел:",
                reply_markup=get_main_menu_keyboard()
        )
    else:
        # Начать регистрацию: попросить фамилию
        await state.set_state(OrderStates.registration_last_name)
        await message.answer(
            "Здравствуйте! Перед началом работы, пожалуйста, укажите вашу фамилию:"
        )
        

# Регистрация — фамилия
@router.message(OrderStates.registration_last_name)
async def registration_last_name(message: Message, state: FSMContext):
    await state.update_data(reg_last_name=message.text)
    await state.set_state(OrderStates.registration_first_name)
    await message.answer("Теперь введите ваше имя:")

# Регистрация — имя
@router.message(OrderStates.registration_first_name)
async def registration_first_name(message: Message, state: FSMContext):
    await state.update_data(reg_first_name=message.text)
    await state.set_state(OrderStates.registration_phone)
    # Предложим кнопку для отправки контакта или текстом ввести номер
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Отправить контакт", request_contact=True)],
                  [KeyboardButton(text="Отправить номер текстом")]],
        resize_keyboard=True
    )
    await message.answer("Отправьте номер телефона (можно как контакт или текстом):", reply_markup=kb)

# Регистрация — телефон (принимаем контакт или текст)
@router.message(OrderStates.registration_phone)
async def registration_phone(message: Message, state: FSMContext):
    phone = None
    if message.contact and message.contact.phone_number:
        phone = message.contact.phone_number
    else:
        # простая валидация: оставить введённый текст
        phone = message.text.strip()
    data = await state.get_data()
    last_name = data.get("reg_last_name", "")
    first_name = data.get("reg_first_name", "")
    # Сохраняем в локальное хранилище
    set_user_info(message.from_user.id, last_name, first_name, phone)
    await state.clear()
    await message.answer(
        f"Спасибо, {first_name} {last_name}! Ваш номер {phone} сохранён.\n"
        "Теперь вы можете делать заказы. Выберите раздел:",
        reply_markup=get_main_menu_keyboard()
    )

# Обработчик подтверждения сообщений от клиентов
@router.callback_query(F.data.in_(["confirm", "confirmed"]))
async def handle_message_confirmation(callback: CallbackQuery):
    from keyboards.order_message_buttons import get_confirmed_keyboard
    
    if callback.data == "confirm":
        # Меняем кнопку на "Подтверждено" только в сообщении менеджера
        await callback.message.edit_reply_markup(reply_markup=get_confirmed_keyboard())
        # Отвечаем только менеджеру, клиент не получает уведомление
        await callback.answer("Сообщение отмечено как обработанное ✅", show_alert=False)
    elif callback.data == "confirmed":
        # Если уже подтверждено, просто отвечаем менеджеру
        await callback.answer("Сообщение уже обработано", show_alert=False)
    
    # Важно: не отправляем никаких сообщений клиенту

# Обработчик кнопки "Написать менеджеру"
@router.message(F.text == "💬 Написать менеджеру")
async def write_to_manager(message: Message, state: FSMContext):
    # Сохраняем состояние, что пользователь хочет написать менеджеру
    await state.set_state(OrderStates.writing_to_manager)
    await message.answer(
        "📝 Напишите ваше сообщение для менеджера. После отправки сообщения вы вернетесь в главное меню.",
        reply_markup=ReplyKeyboardRemove()
    )

# Обработчик сообщения для менеджера
@router.message(OrderStates.writing_to_manager)
async def manager_message_received(message: Message, state: FSMContext):
    # Получаем информацию о пользователе
    user = get_user_info(message.from_user.id)
    
    # Формируем сообщение для менеджера
    user_info = f"📩 СООБЩЕНИЕ ОТ КЛИЕНТА\n\n"
    user_info += f"👤 Пользователь: {user['first_name']} {user['last_name']} (@{message.from_user.username or 'нет username'})\n"
    user_info += f"🆔 ID: {message.from_user.id}\n"
    user_info += f"📞 Телефон: {user['phone']}\n"
    user_info += f"🕒 Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    user_info += f"💬 Сообщение:\n{message.text}"
    
    # Импортируем клавиатуру для подтверждения
    from keyboards.order_message_buttons import get_confirm_keyboard
    
    # Отправляем сообщение менеджеру с кнопкой подтверждения
    try:
        await message.bot.send_message(
            chat_id=RECIPIENT_ID,
            text=user_info,
            reply_markup=get_confirm_keyboard()
        )
        success = True
    except Exception as e:
        print(f"Ошибка отправки сообщения менеджеру: {e}")
        success = False
    
    # Очищаем состояние
    await state.clear()
    
    # Возвращаем в главное меню
    if success:
        await message.answer(
            "✅ Ваше сообщение отправлено менеджеру. Он свяжется с вами в ближайшее время.\n\n"
            "Возвращаю вас в главное меню...",
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await message.answer(
            "❌ Произошла ошибка при отправке сообщения. Пожалуйста, попробуйте позже.\n\n"
            "Возвращаю вас в главное меню...",
            reply_markup=ReplyKeyboardRemove()
        )
    
    await message.answer(
        "Главное меню:",
        reply_markup=get_main_menu_keyboard()
    )

@router.callback_query(F.data == "main_menu")
async def main_menu_inline(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer()
    await callback.message.edit_text(
        "Главное меню:",
        reply_markup=get_main_menu_keyboard()
    )

@router.message(OrderStates.waiting_for_quantity, F.text.regexp(r'^\d+$'))
async def quantity_entered(message: Message, state: FSMContext):
    await state.update_data(Количество=message.text)
    await state.set_state(OrderStates.waiting_for_files)
    await message.answer(
        "Теперь прикрепите файлы:",
        reply_markup=get_files_keyboard()
    )

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

@router.message(OrderStates.waiting_for_comment, F.text == "📝 Добавить примечание")
async def request_comment(message: Message, state: FSMContext):
    await message.answer(
        "Введите примечание к заказу:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Пропустить")],
                     [KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

# ИСПРАВЛЕНИЕ: Добавить фильтр чтобы не срабатывал на кнопки
@router.message(OrderStates.waiting_for_comment, ~F.text.in_(["Пропустить", "🏠 Главное меню", "✅ Отправить заказ-подтверждение", "💬 Написать менеджеру"]))
async def comment_received(message: Message, state: FSMContext):
	await state.update_data(comment=message.text)
	
	data = await state.get_data()
	service_type = data.get('service_type', 'Неизвестная услуга')

	# Краткая сводка
	summary = create_order_summary(message.from_user.id, service_type, data, files_info=data.get('files_info', []), comment=data.get('comment'))
	
	await message.answer(
		f"Заказ готов к отправке!\n\n"
		f"Проверьте детали заказа и нажмите кнопку для отправки менеджеру:\n\n{summary}",
		reply_markup=get_order_confirmation_keyboard()
	)

# ИСПРАВЛЕНИЕ: Добавить обработчик для кнопки "Пропустить"
@router.message(OrderStates.waiting_for_comment, F.text == "Пропустить")
async def skip_comment(message: Message, state: FSMContext):
	data = await state.get_data()
	service_type = data.get('service_type', 'Неизвестная услуга')

	# Краткая сводка
	summary = create_order_summary(message.from_user.id, service_type, data, files_info=data.get('files_info', []), comment=data.get('comment'))

	await message.edit_text(
		f"Заказ готов к отправке!\n\n"
		f"Проверьте детали заказа и нажмите кнопку для отправки менеджеру:\n\n{summary}",
		reply_markup=get_order_confirmation_keyboard()
	)

# Исправленный обработчик confirm_order_inline
@router.callback_query(F.data == "send_order")
async def confirm_order_inline(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_info = get_user_info(callback.from_user.id) or {}
    
    order_message = create_order_message(
        username=callback.from_user.username,
        user_id=callback.from_user.id,
        # Исправлено: убраны лишние параметры
        service_type=data.get('service_type', 'Неизвестная услуга'),
        order_data=data,
        files_info=data.get('files_info', []),
        comment=data.get('comment')
    )
    
    # Отправляем менеджеру
    success = await send_order_to_manager(callback.bot, order_message, data.get('files_data', []))
    
    await callback.answer()
    # await callback.message.edit_text("Идёт загрузка...", reply_markup=ReplyKeyboardRemove())
    
    if success:
        await callback.message.edit_text(
            "✅ Ваш заказ успешно отправлен менеджеру!\n"
            "Ожидайте уведомления о принятии заказа в работу...\n",
            reply_markup=get_main_menu_keyboard()
        )
    else:
        await callback.message.edit_text(
            "❌ Произошла ошибка при отправке заказа. Пожалуйста, попробуйте позже.",
            reply_markup=get_main_menu_keyboard()
        )
    
    await state.clear()

# Добавляем обработчики для inline-кнопок главного меню
@router.callback_query(F.data == "copycenter")
async def handle_copycenter(callback: CallbackQuery, state: FSMContext):
	from keyboards.copycenter import get_copycenter_main_keyboard
	await state.set_state(OrderStates.waiting_for_files)
	await state.update_data(previous_menu='main')
	await callback.answer()
	await callback.message.edit_text(
		"Раздел КОПИЦЕНТР. Выберите тип печати:",
		reply_markup=get_copycenter_main_keyboard()
	)

@router.callback_query(F.data == "polygraphy")
async def handle_polygraphy(callback: CallbackQuery, state: FSMContext):
	from keyboards.polygraphy import get_polygraphy_main_keyboard
	await state.set_state(OrderStates.waiting_for_files)
	await state.update_data(previous_menu='main')
	await callback.answer()
	await callback.message.edit_text(
		"Раздел ПОЛИГРАФИЯ. Выберите продукт:",
		reply_markup=get_polygraphy_main_keyboard()
	)

@router.callback_query(F.data == "packaging")
async def handle_packaging(callback: CallbackQuery, state: FSMContext):
	from keyboards.packaging import get_packaging_main_keyboard
	await state.set_state(OrderStates.waiting_for_files)
	await state.update_data(previous_menu='main')
	await callback.answer()
	await callback.message.edit_text(
		"Раздел УПАКОВКА. Выберите продукт:",
		reply_markup=get_packaging_main_keyboard()
	)

@router.callback_query(F.data == "interior")
async def handle_interior(callback: CallbackQuery, state: FSMContext):
	from keyboards.interior import get_interior_main_keyboard
	await state.set_state(OrderStates.waiting_for_files)
	await state.update_data(previous_menu='main')
	await callback.answer()
	await callback.message.edit_text(
		"Раздел ИНТЕРЬЕРНАЯ ПЕЧАТЬ. Выберите продукт:",
		reply_markup=get_interior_main_keyboard()
	)

@router.callback_query(F.data == "souvenirs")
async def handle_souvenirs(callback: CallbackQuery, state: FSMContext):
	from keyboards.souvenirs import get_souvenirs_main_keyboard
	await state.set_state(OrderStates.waiting_for_files)
	await state.update_data(previous_menu='main')
	await callback.answer()
	await callback.message.edit_text(
		"Раздел СУВЕНИРЫ. Выберите продукт:",
		reply_markup=get_souvenirs_main_keyboard()
	)

@router.callback_query(F.data == "stamps")
async def handle_stamps(callback: CallbackQuery, state: FSMContext):
	from keyboards.stamps import get_stamps_main_keyboard
	await state.set_state(OrderStates.stamp_type)
	await state.update_data(service_type="Изготовление печатей и штампов", previous_menu='main')
	await callback.answer()
	await callback.message.edit_text(
		"🖋️ ИЗГОТОВЛЕНИЕ ПЕЧАТЕЙ И ШТАМПОВ\n\nВыберите тип печати:",
		reply_markup=get_stamps_main_keyboard()
	)

@router.callback_query(F.data == "photoprint")
async def handle_photoprint(callback: CallbackQuery, state: FSMContext):
	from keyboards.photoprint import get_photo_format_keyboard
	await state.set_state(OrderStates.photo_format)
	await state.update_data(service_type="Фотопечать", previous_menu='main')
	await callback.answer()
	await callback.message.edit_text(
		"📸 ФОТОПЕЧАТЬ\n\nℹ️ Печать производится только на глянцевой бумаге\n\nВыберите формат бумаги:",
		reply_markup=get_photo_format_keyboard()
	)