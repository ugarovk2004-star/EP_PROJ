from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from states.order_states import OrderStates
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.packaging import *
from keyboards.copycenter import get_files_keyboard, get_comment_keyboard, get_order_confirmation_keyboard
from utils.order_message import create_order_message, send_order_to_manager

router = Router()

# Обработчик главного меню упаковки через callback
@router.callback_query(F.data == "packaging")
async def packaging_main(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.waiting_for_files)
    await state.update_data(previous_menu='main')
    await callback.answer()
    await callback.message.edit_text(
        "Раздел УПАКОВКА. Выберите продукт:",
        reply_markup=get_packaging_main_keyboard()
    )

# ПАКЕТЫ БУМАЖНЫЕ
@router.callback_query(F.data == "packaging_bags")
async def bags_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.bag_type)
    await state.update_data(service_type="Пакеты", previous_menu='packaging')
    await callback.answer()
    await callback.message.edit_text(
        "🛍️ ПАКЕТЫ\n\nВыберите тип пакета:",
        reply_markup=get_bag_type_keyboard()
    )

# Обработчики бумажных пакетов
@router.callback_query(F.data == "bag_paper")
async def paper_bags_selected(callback: CallbackQuery, state: FSMContext):
    await state.update_data(Тип_пакета="Бумажные пакеты")
    await state.set_state(OrderStates.bag_paper_print)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите тип печати:",
        reply_markup=get_bag_paper_print_keyboard()
    )

@router.callback_query(F.data.in_(["bag_paper_print_one_side", "bag_paper_print_two_sides_same", "bag_paper_print_two_sides_different"]))
async def paper_bags_print_selected(callback: CallbackQuery, state: FSMContext):
    print_map = {
        "bag_paper_print_one_side": "Печать с одной стороны пакета",
        "bag_paper_print_two_sides_same": "Печать с 2 сторон с одного макета",
        "bag_paper_print_two_sides_different": "Печать с 2 сторон разные макеты"
    }
    await state.update_data(Тип_печати=print_map[callback.data])
    await state.set_state(OrderStates.bag_paper_format)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите формат пакета:",
        reply_markup=get_bag_paper_format_keyboard()
    )

@router.callback_query(F.data.in_(["bag_paper_220x330x70", "bag_paper_195x320x90", "bag_paper_100x330x100",
                                 "bag_paper_170x220x70", "bag_paper_70x330x70", "bag_paper_130x220x70",
                                 "bag_paper_120x140x70", "bag_paper_210x210x100", "bag_paper_210x210x80",
                                 "bag_paper_330x220x70"]))
async def paper_bags_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "bag_paper_220x330x70": "220×330×70 мм",
        "bag_paper_195x320x90": "195×320×90 мм",
        "bag_paper_100x330x100": "100×330×100 мм",
        "bag_paper_170x220x70": "170×220×70 мм",
        "bag_paper_70x330x70": "70×330×70 мм",
        "bag_paper_130x220x70": "130×220×70 мм",
        "bag_paper_120x140x70": "120×140×70 мм",
        "bag_paper_210x210x100": "210×210×100 мм",
        "bag_paper_210x210x80": "210×210×80 мм",
        "bag_paper_330x220x70": "330×220×70 мм"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.bag_paper_lamination)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите ламинированное покрытие:",
        reply_markup=get_bag_paper_lamination_keyboard()
    )

@router.callback_query(F.data.in_(["bag_paper_matte", "bag_paper_glossy"]))
async def paper_bags_lamination_selected(callback: CallbackQuery, state: FSMContext):
    lamination_map = {
        "bag_paper_matte": "Матовое",
        "bag_paper_glossy": "Глянцевое"
    }
    await state.update_data(Ламинация=lamination_map[callback.data])
    await state.set_state(OrderStates.bag_paper_grommets)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите люверсы:",
        reply_markup=get_bag_paper_grommets_keyboard()
    )

@router.callback_query(F.data.in_(["bag_paper_grommets_gold", "bag_paper_grommets_silver"]))
async def paper_bags_grommets_selected(callback: CallbackQuery, state: FSMContext):
    grommets_map = {
        "bag_paper_grommets_gold": "Золото",
        "bag_paper_grommets_silver": "Серебро"
    }
    await state.update_data(Люверсы=grommets_map[callback.data])
    await state.set_state(OrderStates.bag_paper_handle)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите ручку-шнурок:",
        reply_markup=get_bag_paper_handle_keyboard()
    )

@router.callback_query(F.data.in_(["bag_paper_handle_white", "bag_paper_handle_black", "bag_paper_handle_red",
                                 "bag_paper_handle_blue", "bag_paper_handle_green", "bag_paper_handle_yellow"]))
async def paper_bags_handle_selected(callback: CallbackQuery, state: FSMContext):
    handle_map = {
        "bag_paper_handle_white": "Белые",
        "bag_paper_handle_black": "Чёрные",
        "bag_paper_handle_red": "Красные",
        "bag_paper_handle_blue": "Синие",
        "bag_paper_handle_green": "Зелёные",
        "bag_paper_handle_yellow": "Жёлтые"
    }
    await state.update_data(Ручка=handle_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# Обработчики ПВД пакетов
@router.callback_query(F.data == "bag_pvd")
async def pvd_bags_selected(callback: CallbackQuery, state: FSMContext):
    await state.update_data(Тип_пакета="ПВД пакеты")
    await state.set_state(OrderStates.bag_pvd_print)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите печать:",
        reply_markup=get_bag_pvd_print_keyboard()
    )

@router.callback_query(F.data.in_(["bag_pvd_print_1_0", "bag_pvd_print_1_1", "bag_pvd_print_2_0", "bag_pvd_print_2_2"]))
async def pvd_bags_print_selected(callback: CallbackQuery, state: FSMContext):
    print_map = {
        "bag_pvd_print_1_0": "1+0",
        "bag_pvd_print_1_1": "1+1",
        "bag_pvd_print_2_0": "2+0",
        "bag_pvd_print_2_2": "2+2"
    }
    await state.update_data(Тип_печати=print_map[callback.data])
    await state.set_state(OrderStates.bag_pvd_format)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите формат:",
        reply_markup=get_bag_pvd_format_keyboard()
    )

@router.callback_query(F.data.in_(["bag_pvd_20x30", "bag_pvd_30x40", "bag_pvd_40x50", "bag_pvd_50x60"]))
async def pvd_bags_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "bag_pvd_20x30": "20×30 см",
        "bag_pvd_30x40": "30×40 см",
        "bag_pvd_40x50": "40×50 см",
        "bag_pvd_50x60": "50×60 см"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# КОРОБКИ
@router.callback_query(F.data == "packaging_boxes")
async def boxes_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(OrderStates.box_material)
    await state.update_data(service_type="Коробки", previous_menu='packaging')
    await callback.answer()
    await callback.message.edit_text(
        "📦 КОРОБКИ\n\nВыберите материал коробки:",
        reply_markup=get_box_material_keyboard()
    )

# Обработчики коробок из мелованного картона
@router.callback_query(F.data == "box_cardboard")
async def cardboard_boxes_selected(callback: CallbackQuery, state: FSMContext):
    await state.update_data(Материал="Коробки из мелованного картона")
    await state.set_state(OrderStates.box_cardboard_size)
    await callback.answer()
    await callback.message.edit_text(
        "Введите размеры коробки в формате Д×Ш×В (мм):"
    )

@router.message(OrderStates.box_cardboard_size)
async def cardboard_boxes_size_entered(message: Message, state: FSMContext):
    await state.update_data(Размер=message.text)
    await state.set_state(OrderStates.box_cardboard_print)
    await message.answer(
        "Выберите печать на коробке:",
        reply_markup=get_box_cardboard_print_keyboard()
    )

@router.callback_query(F.data.in_(["box_cardboard_no_print", "box_cardboard_full_color"]))
async def cardboard_boxes_print_selected(callback: CallbackQuery, state: FSMContext):
    print_map = {
        "box_cardboard_no_print": "Без печати",
        "box_cardboard_full_color": "Полноцветная печать"
    }
    await state.update_data(Печать=print_map[callback.data])
    await state.set_state(OrderStates.box_cardboard_lamination)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите ламинированное покрытие:",
        reply_markup=get_bag_paper_lamination_keyboard()  # Та же клавиатура
    )

@router.callback_query(F.data.in_(["bag_paper_matte", "bag_paper_glossy"]))
async def cardboard_boxes_lamination_selected(callback: CallbackQuery, state: FSMContext):
    lamination_map = {
        "bag_paper_matte": "Матовое",
        "bag_paper_glossy": "Глянцевое"
    }
    await state.update_data(Ламинирование=lamination_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )

# Обработчики коробок из микро-гофры
@router.callback_query(F.data == "box_corrugated")
async def corrugated_boxes_selected(callback: CallbackQuery, state: FSMContext):
    await state.update_data(Материал="Коробки из микро-гофры")
    await state.set_state(OrderStates.box_corrugated_format)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите формат коробки:",
        reply_markup=get_box_corrugated_format_keyboard()
    )

@router.callback_query(F.data.in_(["box_corrugated_95x55x90", "box_corrugated_115x95x65", "box_corrugated_180x55x55",
                                 "box_corrugated_360x150x50", "box_corrugated_415x160x60", "box_corrugated_200x200x10",
                                 "box_corrugated_custom"]))
async def corrugated_boxes_format_selected(callback: CallbackQuery, state: FSMContext):
    format_map = {
        "box_corrugated_95x55x90": "95×55×90 мм",
        "box_corrugated_115x95x65": "115×95×65 мм",
        "box_corrugated_180x55x55": "180×55×55 мм",
        "box_corrugated_360x150x50": "360×150×50 мм",
        "box_corrugated_415x160x60": "415×160×60 мм",
        "box_corrugated_200x200x10": "200×200×10 мм",
        "box_corrugated_custom": "Индивидуальный размер"
    }
    await state.update_data(Формат=format_map[callback.data])
    await state.set_state(OrderStates.box_corrugated_color)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите цвет микрогофры:",
        reply_markup=get_box_corrugated_color_keyboard()
    )

@router.callback_query(F.data.in_(["box_corrugated_white", "box_corrugated_brown"]))
async def corrugated_boxes_color_selected(callback: CallbackQuery, state: FSMContext):
    color_map = {
        "box_corrugated_white": "Белый",
        "box_corrugated_brown": "Коричневый"
    }
    await state.update_data(Цвет=color_map[callback.data])
    await state.set_state(OrderStates.box_corrugated_logo)
    await callback.answer()
    await callback.message.edit_text(
        "Выберите нанесение логотипа:",
        reply_markup=get_box_corrugated_logo_keyboard()
    )

@router.callback_query(F.data.in_(["box_corrugated_no_logo", "box_corrugated_with_logo"]))
async def corrugated_boxes_logo_selected(callback: CallbackQuery, state: FSMContext):
    logo_map = {
        "box_corrugated_no_logo": "Без нанесения",
        "box_corrugated_with_logo": "С нанесением"
    }
    await state.update_data(Логотип=logo_map[callback.data])
    await state.set_state(OrderStates.waiting_for_quantity)
    await callback.answer()
    await callback.message.edit_text(
        "Введите количество экземпляров (только цифры):"
    )