from aiogram import BaseMiddleware
from aiogram.types import Message, Update, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from typing import Dict, Any, Callable, Awaitable
import re

# Словарь-маппинг: состояние → разрешенные текстовые команды
# Словарь-маппинг: состояние → разрешенные текстовые команды
STATE_ALLOWED_INPUTS = {
    # ============ КОПИЦЕНТР ============
    # Ч/Б печать
    'OrderStates:bw_format': ['A4', 'A3'],
    'OrderStates:bw_print_type': ['Односторонняя', 'Двусторонняя', 'Печать брошюры'],
    'OrderStates:bw_additional_services': [
        'Брошюровка на металлическую пружину', 
        'Пластиковые обложки', 
        'Скрепление брошюры', 
        'Пропустить'
    ],
    
    # Цветная печать
    'OrderStates:color_format': [
        'A7 (74×105 мм)', 'A6 (105×148 мм)', 'Евроформат (210×99 мм)', 
        'A5 (148×210 мм)', 'A4 (210×297 мм)', 'A3 (297×420 мм)'
    ],
    'OrderStates:color_paper_type': [
        'Офсетная 80 г/м²', 'Мелованная 115 г/м²', 'Мелованная 130 г/м²',
        'Мелованная 170 г/м²', 'Мелованная 250 г/м²', 'Мелованная 300 г/м²',
        'Пленка белая мат.', 'Пленка белая гл.', 'Пленка прозрач. мат.', 'Пленка прозрач. гл.'
    ],
    'OrderStates:color_print_type': ['Односторонняя', 'Двусторонняя', 'Печать брошюры'],
    'OrderStates:color_additional_services': [
        'Брошюровка на металлическую пружину', 
        'Пластиковые обложки', 
        'Скрепление брошюры', 
        'Подрезка', 
        'Пропустить'
    ],
    
    # Ризограф
    'OrderStates:risograph_format': ['A4', 'А3'],
    'OrderStates:risograph_quantity': ['500', '1000', '1500', '2000', '3000', '5000', '10000'],
    'OrderStates:risograph_color': ['Черный', 'Красный', 'Черный/Красный'],
    'OrderStates:risograph_print_type': ['Односторонняя', 'Двухсторонний'],
    
    # ============ ПОЛИГРАФИЯ ============
    # Визитки
    'OrderStates:business_card_print_type': ['Офсетная', 'Цифровая'],
    'OrderStates:business_card_offset_color': ['4+0 (односторонние)', '4+4 (двусторонние)'],
    'OrderStates:business_card_offset_quantity': ['1000 шт.', '2500 шт.', '5000 шт.', '10000 шт.'],
    'OrderStates:business_card_digital_paper': [
        'Картон 310 г/м²', 'Лен', 'Маджестик', 'Фактурная', 'Плайк'
    ],
    'OrderStates:business_card_digital_lamination': ['Без ламинации', 'Глянцевая', 'Матовая'],
    'OrderStates:business_card_digital_quantity': ['50 шт.', '100 шт.', '200 шт.', '300 шт.', '1000 шт.'],
    
    # Блокноты
    'OrderStates:notebook_format': ['A6', 'A5', 'A4'],
    'OrderStates:notebook_inner_block': [
        'Офсетная 80 г/м² без печати', 
        'Офсетная 80 г/м² с цветной печатью', 
        'Офсетная 80 г/м² с Ч/Б печатью'
    ],
    'OrderStates:notebook_cover_type': [
        'Мелованная бумага 250 г/м² с печатью', 
        'Мелованная бумага 300 г/м² с печатью'
    ],
    'OrderStates:notebook_backing': ['С печатью', 'Без печати'],
    'OrderStates:notebook_stitching': ['По короткому краю', 'По длинному краю'],
    'OrderStates:notebook_pages': ['20 стр.', '40 стр.', '60 стр.', '80 стр.'],
    
    # Буклеты
    'OrderStates:booklet_format': [
        'A4 (в сложенном виде)', 
        'A5 (в сложенном виде)', 
        'A6 (в сложенном виде)', 
        'Евроформат (в сложенном виде)'
    ],
    'OrderStates:booklet_paper_type': [
        'Мелованная 115 г/м²', 
        'Мелованная 130 г/м²', 
        'Мелованная 150 г/м²', 
        'Мелованная 250 г/м²'
    ],
    'OrderStates:booklet_color': ['4+0 (односторонняя)', '4+4 (двухсторонняя)'],
    'OrderStates:booklet_fold_type': ['Один сгиб', 'Два сгиба', 'Гармошка'],
    
    # Календари
    'OrderStates:calendar_type': [
        'Квартальный', 'Домик', 'Карманный (кратно 8 шт.)', 
        'Перекидной А4', 'Перекидной А3'
    ],
    
    # Конверты
    'OrderStates:envelope_type': ['Евроконверт', 'Формат C5', 'Формат C6', 'Конверт для CD'],
    
    # Листовки
    'OrderStates:leaflet_format': [
        'A4 (210×297 мм)', 'A5 (148×210 мм)', 'A6 (105×148 мм)', 
        'A7 (74×105 мм)', 'Евроформат (210×99 мм)'
    ],
    'OrderStates:leaflet_paper_type': [
        'Мелованная 115 г/м²', 'Мелованная 130 г/м²', 
        'Мелованная 150 г/м²', 'Офсетная 80 г/м²'
    ],
    
    # Печать на самоклейке
    'OrderStates:sticker_material_type': [
        'Пленка белая мат.', 'Пленка белая гл.', 
        'Пленка прозрач. мат.', 'Пленка прозрач. гл.'
    ],
    'OrderStates:sticker_print_format': ['A4 (210×297 мм)', 'A3 (297×420 мм)', 'SRA3 (320×450 мм)'],
    'OrderStates:sticker_cutting': ['Да', 'Нет'],
    
    # Плакаты A3
    'OrderStates:poster_format': [
        'A3 (297×420 мм) - цифровая печать',
        'A2 (420×594 мм) - интерьерная печать',
        'A1 (594×841 мм) - интерьерная печать',
        'A0 (841×1189 мм) - интерьерная печать'
    ],
    'OrderStates:poster_paper_type_a3': [
        'Офсетная 80 г/м²', 'Мелованная 115 г/м²', 'Мелованная 130 г/м²',
        'Мелованная 150 г/м²', 'Мелованная 170 г/м²', 'Мелованная 250 г/м²'
    ],
    'OrderStates:poster_cutting': ['Подрезка нужна', 'Подрезка не нужна'],
    'OrderStates:poster_paper_type_large': ['Постерная бумага 150 г/м²', 'Постерная бумага 200 г/м²'],
    
    # Сертификаты
    'OrderStates:certificate_format': [
        'A4 (210×297 мм)', 'A5 (148×210 мм)', 
        'A6 (105×148 мм)', 'Евроформат (210×99 мм)'
    ],
    'OrderStates:certificate_paper_type': [
        'Мелованная 150 г/м²', 'Мелованная 170 г/м²', 'Мелованная 250 г/м²'
    ],
    'OrderStates:certificate_lamination': ['Без ламинации', 'Глянцевая', 'Матовая'],
    
    # Стикеры с плоттерной резкой
    'OrderStates:sticker_pack_material': [
        'Пленка белая мат.', 'Пленка белая гл.', 
        'Пленка прозрач. мат.', 'Пленка прозрач. гл.'
    ],
    'OrderStates:sticker_pack_format': [
        'A4 (210×297 мм)', 'A3 (297×420 мм)', 
        'A5 стикерпак (148×210 мм)', 'A6 стикерпак (105×148 мм)'
    ],
    'OrderStates:sticker_pack_color': ['4+0 (односторонняя)'],
    'OrderStates:sticker_pack_cut': ['Да (включена в стоимость)', 'Нет (только печать)'],
    
    # Тетради
    'OrderStates:notebook_school_format': ['A6', 'A5', 'A4', 'А3'],
    'OrderStates:notebook_school_stitching_position': ['По короткому краю', 'По длинному краю'],
    'OrderStates:notebook_school_binding_type': ['Пружина', 'Скрепка'],
    'OrderStates:notebook_school_cover_type': [
        'Офсетная 80 г/м²',
        'Мелованная бумага 115 г/м²', 'Мелованная бумага 130 г/м²',
        'Мелованная бумага 150 г/м²', 'Мелованная бумага 170 г/м²',
        'Мелованная бумага 250 г/м²', 'Мелованная бумага 300 г/м²'
    ],
    'OrderStates:notebook_school_cover_print': [
        'Печать ч/б односторонняя (1+0) только для ВХИ 80гр.',
        'Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.',
        'Цветная односторонняя (4+0)', 'Цветная двухсторонняя (4+4)'
    ],
    'OrderStates:notebook_school_backing_print': [
        'Печать ч/б односторонняя (1+0) только для ВХИ 80гр.',
        'Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.',
        'Цветная односторонняя (4+0)', 'Цветная двухсторонняя (4+4)'
    ],
    'OrderStates:notebook_school_inner_block': [
        'Офсетная 80 г/м²',
        'Мелованная бумага 115 г/м²', 'Мелованная бумага 130 г/м²',
        'Мелованная бумага 150 г/м²', 'Мелованная бумага 170 г/м²',
        'Мелованная бумага 250 г/м²'
    ],
    'OrderStates:notebook_school_inner_print': [
        'Печать ч/б односторонняя (1+0) только для ВХИ 80гр.',
        'Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.',
        'Цветная односторонняя (4+0)', 'Цветная двухсторонняя (4+4)'
    ],
    
    # Каталоги
    'OrderStates:catalog_format': ['A5', 'A4', 'А3'],
    'OrderStates:catalog_stitching_position': ['По короткому краю', 'По длинному краю'],
    'OrderStates:catalog_binding_type': ['Пружина', 'Скрепка'],
    'OrderStates:catalog_cover_type': [
        'Офсетная 80 г/м²',
        'Мелованная бумага 115 г/м²', 'Мелованная бумага 130 г/м²',
        'Мелованная бумага 150 г/м²', 'Мелованная бумага 170 г/м²',
        'Мелованная бумага 250 г/м²', 'Мелованная бумага 300 г/м²'
    ],
    'OrderStates:catalog_cover_print': [
        'Печать ч/б односторонняя (1+0) только для ВХИ 80гр.',
        'Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.',
        'Цветная односторонняя (4+0)', 'Цветная двухсторонняя (4+4)'
    ],
    'OrderStates:catalog_backing_print': [
        'Печать ч/б односторонняя (1+0) только для ВХИ 80гр.',
        'Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.',
        'Цветная односторонняя (4+0)', 'Цветная двухсторонняя (4+4)'
    ],
    'OrderStates:catalog_inner_block': [
        'Офсетная 80 г/м²',
        'Мелованная бумага 115 г/м²', 'Мелованная бумага 130 г/м²',
        'Мелованная бумага 150 г/м²', 'Мелованная бумага 170 г/м²',
        'Мелованная бумага 250 г/м²'
    ],
    'OrderStates:catalog_inner_print': [
        'Печать ч/б односторонняя (1+0) только для ВХИ 80гр.',
        'Печать ч/б двухсторонняя (1+1) только для ВХИ 80гр.',
        'Цветная односторонняя (4+0)', 'Цветная двухсторонняя (4+4)'
    ],
    
    # ============ УПАКОВКА ============
    # Пакеты
    'OrderStates:bag_type': ['Бумажные пакеты', 'ПВД пакеты'],
    'OrderStates:bag_paper_print': [
        'Печать с одной стороны пакета',
        'Печать с 2 сторон с одного макета',
        'Печать с 2 сторон разные макеты'
    ],
    'OrderStates:bag_paper_format': [
        '220×330×70 мм', '195×320×90 мм', '100×330×100 мм',
        '170×220×70 мм', '70×330×70 мм', '130×220×70 мм',
        '120×140×70 мм', '210×210×100 мм', '210×210×80 мм',
        '330×220×70 мм'
    ],
    'OrderStates:bag_paper_lamination': ['Матовое', 'Глянцевое'],
    'OrderStates:bag_paper_grommets': ['Золото', 'Серебро'],
    'OrderStates:bag_paper_handle': [
        'Белые', 'Чёрные', 'Красные', 'Синие', 'Зелёные', 'Жёлтые'
    ],
    'OrderStates:bag_pvd_print': ['1+0', '1+1', '2+0', '2+2'],
    'OrderStates:bag_pvd_format': ['20×30 см', '30×40 см', '40×50 см', '50×60 см'],
    
    # Коробки
    'OrderStates:box_material': ['Коробки из мелованного картона', 'Коробки из микро-гофры'],
    'OrderStates:box_cardboard_print': ['Без печати', 'Полноцветная печать'],
    'OrderStates:box_corrugated_format': [
        '95×55×90 мм', '115×95×65 мм', '180×55×55 мм',
        '360×150×50 мм', '415×160×60 мм', '200×200×10 мм',
        'Индивидуальный размер'
    ],
    'OrderStates:box_corrugated_color': ['Белый', 'Коричневый'],
    'OrderStates:box_corrugated_logo': ['Без нанесения', 'С нанесением'],
    
    # ============ ИНТЕРЬЕРНАЯ ПЕЧАТЬ ============
    # Таблички
    'OrderStates:sign_type': ['Офисные таблички', 'Уличные таблички'],
    'OrderStates:sign_material': ['Пластик ПВХ-3 мм', 'Пластик ПВХ-5 мм', 'Двухслойный пластик'],
    
    # Картины на холсте
    'OrderStates:canvas_size': [
        '20×30 см', '30×40 см', '40×50 см', '40×60 см',
        '50×50 см', '50×70 см', '60×80 см', '70×100 см', '80×120 см'
    ],
    'OrderStates:canvas_framing': ['Без подрамника', 'Галерейная натяжка'],
    
    # Печать на баннере
    'OrderStates:banner_print_type': ['Широкоформатная', 'Интерьерная'],
    'OrderStates:banner_edge_processing': ['Без обработки', 'Укрепление края'],
    'OrderStates:banner_grommets': [
        'Без люверсов', 'Люверсы через 30 см', 'Люверсы через 50 см'
    ],
    
    # Печать на самоклейке
    'OrderStates:interior_sticker_film_type': [
        'Пленка белая мат.', 'Пленка белая гл.', 
        'Пленка прозрач. мат.', 'Пленка прозрач. гл.'
    ],
    'OrderStates:interior_sticker_processing': [
        'Без обработки', 'Ламинация', 
        'Подрезка напечатанного макета', 'Плоттерная резка'
    ],
    
    # ============ СУВЕНИРЫ ============
    # Ручки
    'OrderStates:pen_material': ['Пластик', 'Металл', 'Крафт (картон)'],
    'OrderStates:pen_color': [
        'Синий', 'Красный', 'Черный', 'Белый', 'Серебристый', 'Золотистый'
    ],
    'OrderStates:pen_application': ['Лазерная гравировка', 'УФ-печать'],
    
    # Футболки
    'OrderStates:tshirt_size': ['XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL'],
    'OrderStates:tshirt_material': [
        'Хлопок 100% (белый)', 'Хлопок 100% (черный)',
        'Хлопок 50% / Полиэстер 50% (белый)'
    ],
    'OrderStates:tshirt_print_position': ['На груди', 'На спине'],
    
    # Кружки
    'OrderStates:mug_type': [
        'Кружка белая', 'Кружка цветная внутри, цветная ручка'
    ],
    'OrderStates:mug_print_position': ['С одной стороны', 'По кругу', 'С двух сторон'],
    'OrderStates:mug_packaging': ['Без упаковки', 'Подарочная коробка'],
    
    # ============ ПЕЧАТИ И ШТАМПЫ ============
    'OrderStates:stamp_type': [
        'АВТОМАТИЧЕСКАЯ ПЕЧАТЬ', 'КАРМАННАЯ ПЕЧАТЬ',
        'ФАКСИМИЛЕ', 'КЛИШЕ БЕЗ ОСНАСТКИ'
    ],
    'OrderStates:stamp_format': ['Круглая 30 мм', 'Круглая 40 мм', 'Прямоугольный штамп'],
    'OrderStates:stamp_ink_color': ['Черный', 'Фиолетовый', 'Красный', 'Зелёный'],
    
    # ============ ФОТОПЕЧАТЬ ============
    'OrderStates:photo_format': ['10×15', '15×21', '21×30'],
    'OrderStates:photo_print_type': [
        'С полями (изображение полностью, возможны белые поля)',
        'Без полей (изображение займёт всю площадь, возможна обрезка краёв)'
    ],

    # ============ ГЛАВНОЕ МЕНЮ ============
    'OrderStates:main_menu': ['📄 КОПИЦЕНТР', '🖨️ ПОЛИГРАФИЯ', '📦 УПАКОВКА', '🖼️ ИНТЕРЬЕРНАЯ ПЕЧАТЬ', 
                              '🎁 СУВЕНИРЫ', '🏢 ИЗГОТОВЛЕНИЕ ПЕЧАТЕЙ И ШТАМПОВ', '📸 ФОТОПЕЧАТЬ'],
    
    # ============ ОБЩИЕ СОСТОЯНИЯ ============
    # Числовые вводы
    'OrderStates:waiting_for_quantity': r'^\d+$',
    'OrderStates:box_cardboard_size': r'^.+$',  # Любой текст для размеров
    'OrderStates:sign_size': r'^.+$',
    'OrderStates:banner_size': r'^.+$',
    'OrderStates:interior_sticker_size': r'^.+$',
    
    # Текстовые вводы
    'OrderStates:waiting_for_comment': r'^.+$',
    'OrderStates:waiting_for_files': r'^.+$',
}

# Специальные команды, разрешённые в любом состоянии
GLOBAL_ALLOWED_COMMANDS = [
    '🏠 Главное меню', '⬅️ Назад', 'Пропустить',
    '✅ Отправить заказ-подтверждение', '📎 Прикрепить файлы',
    '📝 Добавить примечание', '💬 Написать менеджеру',
    'Ч/Б ПЕЧАТЬ', 'ЦВЕТНАЯ ПЕЧАТЬ', 'РИЗОГРАФ',  # Копицентр
    'ВИЗИТКИ', 'БЛОКНОТЫ', 'БУКЛЕТЫ', 'КАЛЕНДАРИ', 'КОНВЕРТЫ',  # Полиграфия
    'ЛИСТОВКИ', 'ПЕЧАТЬ НА САМОКЛЕЙКЕ', 'ПЛАКАТЫ', 'СЕРТИФИКАТЫ',
    'СТИКЕРЫ С ПЛОТТЕРНОЙ РЕЗКОЙ', 'ТЕТРАДИ', 'КАТАЛОГИ',
    'ПАКЕТЫ', 'КОРОБКИ',  # Упаковка
    'ПЛАКАТЫ', 'ТАБЛИЧКИ', 'КАРТИНЫ НА ХОЛСТЕ', 'ПЕЧАТЬ НА БАННЕРЕ',  # Интерьер
    'ПЕЧАТЬ НА САМОКЛЕЮЩЕЙСЯ ПЛЁНКЕ',
    'РУЧКИ С ЛОГОТИПОМ', 'ФУТБОЛКИ', 'КРУЖКИ',  # Сувениры
    'АВТОМАТИЧЕСКАЯ ПЕЧАТЬ', 'КАРМАННАЯ ПЕЧАТЬ', 'ФАКСИМИЛЕ', 'КЛИШЕ БЕЗ ОСНАСТКИ',  # Штампы
    'Офсетная', 'Цифровая',  # Визитки подразделы
    'Бумажные пакеты', 'ПВД пакеты',  # Упаковка подразделы
    'Коробки из мелованного картона', 'Коробки из микро-гофры',  # Коробки подразделы
    'Пластик', 'Металл', 'Крафт (картон)',  # Ручки материалы
    'Хлопок 100% (белый)', 'Хлопок 100% (черный)', 'Хлопок 50% / Полиэстер 50% (белый)',  # Футболки
    'Кружка белая', 'Кружка цветная внутри, цветная ручка',  # Кружки
    'Лазерная гравировка', 'УФ-печать',  # Нанесение
    'По короткому краю', 'По длинному краю',  # Сшивание
    'Пружина', 'Скрепка',  # Переплет
    'Без ламинации', 'Глянцевая', 'Матовая',  # Ламинация
    'Да', 'Нет',  # Общие ответы
    'Подрезка нужна', 'Подрезка не нужна',  # Плакаты
    'Да (включена в стоимость)', 'Нет (только печать)',  # Плоттерная резка
    'С печатью', 'Без печати',  # Блокноты
    'Без нанесения', 'С нанесением',  # Логотипы
    'Без подрамника', 'Галерейная натяжка',  # Холсты
    'Без обработки', 'Укрепление края',  # Баннеры
    'Без люверсов', 'Люверсы через 30 см', 'Люверсы через 50 см',  # Люверсы
    'Матовое', 'Глянцевое',  # Ламинация пакетов
    'Золото', 'Серебро',  # Люверсы цвета
    'Белые', 'Чёрные', 'Красные', 'Синие', 'Зелёные', 'Жёлтые',  # Ручки пакетов
    '1+0', '1+1', '2+0', '2+2',  # ПВД печать
    'Черный', 'Красный', 'Черный/Красный',  # Ризограф
    'Синий', 'Красный', 'Черный', 'Белый', 'Серебристый', 'Золотистый',  # Цвета ручек
    'На груди', 'На спине',  # Футболки принт
    'С одной стороны', 'По кругу', 'С двух сторон',  # Кружки принт
    'Без упаковки', 'Подарочная коробка',  # Упаковка кружек
    'С полями (изображение полностью, возможны белые поля)',
    'Без полей (изображение займёт всю площадь, возможна обрезка краёв)',  # Фото
    'Печать с одной стороны пакета', 'Печать с 2 сторон с одного макета', 'Печать с 2 сторон разные макеты',  # Печать пакетов
    'Круглая 30 мм', 'Круглая 40 мм', 'Прямоугольный штамп',  # Форматы штампов
    'Черный', 'Фиолетовый', 'Красный', 'Зелёный'  # Цвета чернил
]

class InputValidationMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any]
    ) -> Any:
        # Пропускаем колбэки (inline кнопки) без проверки
        if event.callback_query:
            return await handler(event, data)
        
        # Проверяем только текстовые сообщения
        if not event.message or not event.message.text:
            return await handler(event, data)
        
        # Получаем текущее состояние
        state: FSMContext = data.get("state")
        
        # Если состояние не установлено, пропускаем проверку
        if not state:
            return await handler(event, data)
        
        current_state = await state.get_state()
        
        # Если нет состояния
        if not current_state:
            return await handler(event, data)
        
        message_text = event.message.text
        
        # Проверяем глобально разрешённые команды
        if message_text in GLOBAL_ALLOWED_COMMANDS:
            return await handler(event, data)
        
        # Проверяем разрешённые вводы для текущего состояния
        allowed_inputs = STATE_ALLOWED_INPUTS.get(current_state)
        
        if allowed_inputs is None:
            # Если состояние не в списке, пропускаем проверку
            return await handler(event, data)
        
        # Проверка по регулярному выражению
        if isinstance(allowed_inputs, str) and re.match(allowed_inputs, message_text):
            return await handler(event, data)
        
        # Проверка по списку разрешённых значений
        if isinstance(allowed_inputs, list) and message_text in allowed_inputs:
            return await handler(event, data)
        
        # Если ввод не валиден - отправляем сообщение об ошибке
        await self.send_validation_error(event.message, state, current_state)
        return  # Прерываем дальнейшую обработку
    
    async def send_validation_error(self, message: Message, state: FSMContext, current_state: str):
        """Отправляет сообщение об ошибке и возвращает соответствующую клавиатуру"""
        from keyboards.main_menu import get_main_menu_keyboard
        
        # Получаем данные состояния
        state_data = await state.get_data()
        previous_menu = state_data.get('previous_menu', 'main')
        service_type = state_data.get('Услуга', 'Неизвестная услуга')
        
        # Формируем сообщение об ошибке
        error_message = (
            f"⚠️ **Некорректный ввод!**\n\n"
            f"Раздел: {service_type}\n"
            f"Ожидаемый ввод не соответствует текущему этапу.\n\n"
            f"Пожалуйста, используйте предложенные варианты."
        )
        
        # Отправляем сообщение
        await message.answer(error_message)
        
        # В зависимости от состояния, показываем соответствующую клавиатуру
        await self.show_correct_keyboard(message, current_state, previous_menu, service_type)
    
    async def show_correct_keyboard(self, message: Message, current_state: str, previous_menu: str, service_type: str):
        """Показывает правильную клавиатуру для текущего состояния"""
        try:
            # === КОПИЦЕНТР ===
            if 'bw_format' in current_state:
                from keyboards.copycenter import get_bw_format_keyboard
                await message.answer("Выберите формат:", reply_markup=get_bw_format_keyboard())
            
            elif 'bw_print_type' in current_state:
                from keyboards.copycenter import get_bw_print_type_keyboard
                await message.answer("Выберите тип печати:", reply_markup=get_bw_print_type_keyboard())
            
            elif 'bw_additional_services' in current_state:
                from keyboards.copycenter import get_bw_additional_services_keyboard
                await message.answer("Выберите дополнительные услуги:", reply_markup=get_bw_additional_services_keyboard())
            
            elif 'color_format' in current_state:
                from keyboards.copycenter import get_color_format_keyboard
                await message.answer("Выберите формат:", reply_markup=get_color_format_keyboard())
            
            elif 'color_paper_type' in current_state:
                from keyboards.copycenter import get_color_paper_type_keyboard
                await message.answer("Выберите тип бумаги:", reply_markup=get_color_paper_type_keyboard())
            
            elif 'color_print_type' in current_state:
                from keyboards.copycenter import get_bw_print_type_keyboard
                await message.answer("Выберите тип печати:", reply_markup=get_bw_print_type_keyboard())
            
            elif 'color_additional_services' in current_state:
                from keyboards.copycenter import get_color_additional_services_keyboard
                await message.answer("Выберите дополнительные услуги:", reply_markup=get_color_additional_services_keyboard())
            
            elif 'risograph_format' in current_state:
                from keyboards.copycenter import get_risograph_format_keyboard
                await message.answer("Выберите формат:", reply_markup=get_risograph_format_keyboard())
            
            elif 'risograph_quantity' in current_state:
                from keyboards.copycenter import get_risograph_quantity_keyboard
                await message.answer("Выберите количество экземпляров:", reply_markup=get_risograph_quantity_keyboard())
            
            elif 'risograph_color' in current_state:
                from keyboards.copycenter import get_risograph_color_keyboard
                await message.answer("Выберите цвет печати:", reply_markup=get_risograph_color_keyboard())
            
            elif 'risograph_print_type' in current_state:
                from keyboards.copycenter import get_risograph_print_type_keyboard
                await message.answer("Выберите тип печати:", reply_markup=get_risograph_print_type_keyboard())
            
            # === ПОЛИГРАФИЯ ===
            elif 'business_card_print_type' in current_state:
                from keyboards.polygraphy import get_business_card_print_type_keyboard
                await message.answer("Выберите тип печати:", reply_markup=get_business_card_print_type_keyboard())
            
            elif 'business_card_offset_color' in current_state:
                from keyboards.polygraphy import get_business_card_offset_color_keyboard
                await message.answer("Выберите цветность:", reply_markup=get_business_card_offset_color_keyboard())
            
            elif 'business_card_offset_quantity' in current_state:
                from keyboards.polygraphy import get_business_card_offset_quantity_keyboard
                await message.answer("Выберите количество:", reply_markup=get_business_card_offset_quantity_keyboard())
            
            elif 'business_card_digital_paper' in current_state:
                from keyboards.polygraphy import get_business_card_digital_paper_keyboard
                await message.answer("Выберите тип бумаги:", reply_markup=get_business_card_digital_paper_keyboard())
            
            elif 'business_card_digital_color' in current_state:
                from keyboards.polygraphy import get_business_card_offset_color_keyboard
                await message.answer("Выберите цветность:", reply_markup=get_business_card_offset_color_keyboard())
            
            elif 'business_card_digital_lamination' in current_state:
                from keyboards.polygraphy import get_business_card_digital_lamination_keyboard
                await message.answer("Выберите ламинацию:", reply_markup=get_business_card_digital_lamination_keyboard())
            
            elif 'business_card_digital_quantity' in current_state:
                from keyboards.polygraphy import get_business_card_digital_quantity_keyboard
                await message.answer("Выберите количество:", reply_markup=get_business_card_digital_quantity_keyboard())
            
            elif 'notebook_format' in current_state:
                from keyboards.polygraphy import get_notebook_format_keyboard
                await message.answer("Выберите формат:", reply_markup=get_notebook_format_keyboard())
            
            elif 'notebook_inner_block' in current_state:
                from keyboards.polygraphy import get_notebook_inner_block_keyboard
                await message.answer("Выберите внутренний блок:", reply_markup=get_notebook_inner_block_keyboard())
            
            elif 'notebook_cover_type' in current_state:
                from keyboards.polygraphy import get_notebook_cover_type_keyboard
                await message.answer("Выберите тип обложки:", reply_markup=get_notebook_cover_type_keyboard())
            
            elif 'notebook_backing' in current_state:
                from keyboards.polygraphy import get_notebook_backing_keyboard
                await message.answer("Выберите подложку:", reply_markup=get_notebook_backing_keyboard())
            
            elif 'notebook_stitching' in current_state:
                from keyboards.polygraphy import get_notebook_stitching_keyboard
                await message.answer("Выберите позицию сшивания:", reply_markup=get_notebook_stitching_keyboard())
            
            elif 'notebook_pages' in current_state:
                from keyboards.polygraphy import get_notebook_pages_keyboard
                await message.answer("Выберите количество страниц:", reply_markup=get_notebook_pages_keyboard())
            
            elif 'booklet_format' in current_state:
                from keyboards.polygraphy import get_booklet_format_keyboard
                await message.answer("Выберите формат готового изделия:", reply_markup=get_booklet_format_keyboard())
            
            elif 'booklet_paper_type' in current_state:
                from keyboards.polygraphy import get_booklet_paper_type_keyboard
                await message.answer("Выберите тип бумаги:", reply_markup=get_booklet_paper_type_keyboard())
            
            elif 'booklet_color' in current_state:
                from keyboards.polygraphy import get_booklet_color_keyboard
                await message.answer("Выберите цветность:", reply_markup=get_booklet_color_keyboard())
            
            elif 'booklet_fold_type' in current_state:
                from keyboards.polygraphy import get_booklet_fold_type_keyboard
                await message.answer("Выберите тип сгиба:", reply_markup=get_booklet_fold_type_keyboard())
            
            elif 'calendar_type' in current_state:
                from keyboards.polygraphy import get_calendar_type_keyboard
                await message.answer("Выберите вид календаря:", reply_markup=get_calendar_type_keyboard())
            
            elif 'envelope_type' in current_state:
                from keyboards.polygraphy import get_envelope_type_keyboard
                await message.answer("Выберите тип конверта:", reply_markup=get_envelope_type_keyboard())
            
            elif 'leaflet_format' in current_state:
                from keyboards.polygraphy import get_leaflet_format_keyboard
                await message.answer("Выберите формат:", reply_markup=get_leaflet_format_keyboard())
            
            elif 'leaflet_paper_type' in current_state:
                from keyboards.polygraphy import get_leaflet_paper_type_keyboard
                await message.answer("Выберите формат печати:", reply_markup=get_leaflet_paper_type_keyboard())
            
            elif 'leaflet_color' in current_state:
                from keyboards.polygraphy import get_business_card_offset_color_keyboard
                await message.answer("Выберите цветность:", reply_markup=get_business_card_offset_color_keyboard())
            
            elif 'sticker_material_type' in current_state:
                from keyboards.polygraphy import get_sticker_material_type_keyboard
                await message.answer("Выберите тип материала:", reply_markup=get_sticker_material_type_keyboard())
            
            elif 'sticker_print_format' in current_state:
                from keyboards.polygraphy import get_sticker_print_format_keyboard
                await message.answer("Выберите формат печати:", reply_markup=get_sticker_print_format_keyboard())
            
            elif 'sticker_cutting' in current_state:
                from keyboards.polygraphy import get_sticker_cutting_keyboard
                await message.answer("Вам нужна подрезка?:", reply_markup=get_sticker_cutting_keyboard())
            
            elif 'poster_paper_type_a3' in current_state:
                from keyboards.polygraphy import get_poster_paper_type_a3_keyboard
                await message.answer("Выберите тип бумаги:", reply_markup=get_poster_paper_type_a3_keyboard())
            
            elif 'poster_cutting_a3' in current_state:
                from keyboards.polygraphy import get_poster_cutting_keyboard
                await message.answer("Вам нужна подрезка?:", reply_markup=get_poster_cutting_keyboard())
            
            elif 'poster_paper_type_large' in current_state:
                from keyboards.polygraphy import get_poster_paper_type_large_keyboard
                await message.answer("Выберите тип бумаги:", reply_markup=get_poster_paper_type_large_keyboard())
            
            elif 'poster_cutting_large' in current_state:
                from keyboards.polygraphy import get_poster_cutting_keyboard
                await message.answer("Вам нужна подрезка?:", reply_markup=get_poster_cutting_keyboard())
            
            elif 'certificate_format' in current_state:
                from keyboards.polygraphy import get_certificate_format_keyboard
                await message.answer("Выберите формат:", reply_markup=get_certificate_format_keyboard())
            
            elif 'certificate_paper_type' in current_state:
                from keyboards.polygraphy import get_certificate_paper_type_keyboard
                await message.answer("Выберите тип бумаги:", reply_markup=get_certificate_paper_type_keyboard())
            
            elif 'certificate_color' in current_state:
                from keyboards.polygraphy import get_booklet_color_keyboard
                await message.answer("Выберите цветность бумаги:", reply_markup=get_booklet_color_keyboard())
            
            elif 'certificate_lamination' in current_state:
                from keyboards.polygraphy import get_certificate_lamination_keyboard
                await message.answer("Выберите ламинацию:", reply_markup=get_certificate_lamination_keyboard())
            
            elif 'sticker_pack_material' in current_state:
                from keyboards.polygraphy import get_sticker_pack_material_keyboard
                await message.answer("Выберите тип материала:", reply_markup=get_sticker_pack_material_keyboard())
            
            elif 'sticker_pack_format' in current_state:
                from keyboards.polygraphy import get_sticker_pack_format_keyboard
                await message.answer("Выберите формат материала:", reply_markup=get_sticker_pack_format_keyboard())
            
            elif 'sticker_pack_color' in current_state:
                from keyboards.polygraphy import get_sticker_pack_color_keyboard
                await message.answer("Выберите цветность печати:", reply_markup=get_sticker_pack_color_keyboard())
            
            elif 'sticker_pack_cutting' in current_state:
                from keyboards.polygraphy import get_sticker_pack_cut_keyboard
                await message.answer("Вам нужна нарезка на плоттере?:", reply_markup=get_sticker_pack_cut_keyboard())
            
            elif 'notebook_school_format' in current_state:
                from keyboards.polygraphy import get_notebook_school_format_keyboard
                await message.answer("Выберите формат:", reply_markup=get_notebook_school_format_keyboard())
            
            elif 'notebook_school_stitching_position' in current_state:
                from keyboards.polygraphy import get_notebook_school_stitching_position_keyboard
                await message.answer("Выберите позицию сшивания:", reply_markup=get_notebook_school_stitching_position_keyboard())
            
            elif 'notebook_school_binding_type' in current_state:
                from keyboards.polygraphy import get_notebook_school_binding_type_keyboard
                await message.answer("Выберите тип скрепления:", reply_markup=get_notebook_school_binding_type_keyboard())
            
            elif 'notebook_school_cover_type' in current_state:
                from keyboards.polygraphy import get_notebook_school_cover_type_keyboard
                await message.answer("Выберите тип обложки/подложки:", reply_markup=get_notebook_school_cover_type_keyboard())
            
            elif 'notebook_school_cover_print' in current_state:
                from keyboards.polygraphy import get_notebook_school_cover_print_keyboard
                await message.answer("Выберите обложка печать:", reply_markup=get_notebook_school_cover_print_keyboard())
            
            elif 'notebook_school_backing_print' in current_state:
                from keyboards.polygraphy import get_notebook_school_backing_print_keyboard
                await message.answer("Выберите подложка печать:", reply_markup=get_notebook_school_backing_print_keyboard())
            
            elif 'notebook_school_inner_block' in current_state:
                from keyboards.polygraphy import get_notebook_school_inner_block_keyboard
                await message.answer("Выберите внутренний блок:", reply_markup=get_notebook_school_inner_block_keyboard())
            
            elif 'notebook_school_inner_print' in current_state:
                from keyboards.polygraphy import get_notebook_school_inner_print_keyboard
                await message.answer("Выберите внутренний блок печать:", reply_markup=get_notebook_school_inner_print_keyboard())
            
            elif 'catalog_format' in current_state:
                from keyboards.polygraphy import get_catalog_format_keyboard
                await message.answer("Выберите формат:", reply_markup=get_catalog_format_keyboard())
            
            elif 'catalog_stitching_position' in current_state:
                from keyboards.polygraphy import get_catalog_stitching_position_keyboard
                await message.answer("Выберите позицию сшивания:", reply_markup=get_catalog_stitching_position_keyboard())
            
            elif 'catalog_binding_type' in current_state:
                from keyboards.polygraphy import get_catalog_binding_type_keyboard
                await message.answer("Выберите тип скрепления:", reply_markup=get_catalog_binding_type_keyboard())
            
            elif 'catalog_cover_type' in current_state:
                from keyboards.polygraphy import get_catalog_cover_type_keyboard
                await message.answer("Выберите тип обложки/подложки:", reply_markup=get_catalog_cover_type_keyboard())
            
            elif 'catalog_cover_print' in current_state:
                from keyboards.polygraphy import get_catalog_cover_print_keyboard
                await message.answer("Выберите обложка печать:", reply_markup=get_catalog_cover_print_keyboard())
            
            elif 'catalog_backing_print' in current_state:
                from keyboards.polygraphy import get_catalog_backing_print_keyboard
                await message.answer("Выберите подложка печать:", reply_markup=get_catalog_backing_print_keyboard())
            
            elif 'catalog_inner_block' in current_state:
                from keyboards.polygraphy import get_catalog_inner_block_keyboard
                await message.answer("Выберите внутренний блок:", reply_markup=get_catalog_inner_block_keyboard())
            
            elif 'catalog_inner_print' in current_state:
                from keyboards.polygraphy import get_catalog_inner_print_keyboard
                await message.answer("Выберите внутренний блок печать:", reply_markup=get_catalog_inner_print_keyboard())
            
            # === УПАКОВКА ===
            elif 'bag_type' in current_state:
                from keyboards.packaging import get_bag_type_keyboard
                await message.answer("Выберите тип пакета:", reply_markup=get_bag_type_keyboard())
            
            elif 'bag_paper_print' in current_state:
                from keyboards.packaging import get_bag_paper_print_keyboard
                await message.answer("Выберите тип печати:", reply_markup=get_bag_paper_print_keyboard())
            
            elif 'bag_paper_format' in current_state:
                from keyboards.packaging import get_bag_paper_format_keyboard
                await message.answer("Выберите формат пакета:", reply_markup=get_bag_paper_format_keyboard())
            
            elif 'bag_paper_lamination' in current_state:
                from keyboards.packaging import get_bag_paper_lamination_keyboard
                await message.answer("Выберите ламинированное покрытие:", reply_markup=get_bag_paper_lamination_keyboard())
            
            elif 'bag_paper_grommets' in current_state:
                from keyboards.packaging import get_bag_paper_grommets_keyboard
                await message.answer("Выберите люверсы:", reply_markup=get_bag_paper_grommets_keyboard())
            
            elif 'bag_paper_handle' in current_state:
                from keyboards.packaging import get_bag_paper_handle_keyboard
                await message.answer("Выберите ручку-шнурок:", reply_markup=get_bag_paper_handle_keyboard())
            
            elif 'bag_pvd_print' in current_state:
                from keyboards.packaging import get_bag_pvd_print_keyboard
                await message.answer("Выберите печать:", reply_markup=get_bag_pvd_print_keyboard())
            
            elif 'bag_pvd_format' in current_state:
                from keyboards.packaging import get_bag_pvd_format_keyboard
                await message.answer("Выберите формат:", reply_markup=get_bag_pvd_format_keyboard())
            
            elif 'box_material' in current_state:
                from keyboards.packaging import get_box_material_keyboard
                await message.answer("Выберите материал коробки:", reply_markup=get_box_material_keyboard())
            
            elif 'box_cardboard_print' in current_state:
                from keyboards.packaging import get_box_cardboard_print_keyboard
                await message.answer("Выберите печать на коробке:", reply_markup=get_box_cardboard_print_keyboard())
            
            elif 'box_cardboard_lamination' in current_state:
                from keyboards.packaging import get_bag_paper_lamination_keyboard
                await message.answer("Выберите ламинированное покрытие:", reply_markup=get_bag_paper_lamination_keyboard())
            
            elif 'box_corrugated_format' in current_state:
                from keyboards.packaging import get_box_corrugated_format_keyboard
                await message.answer("Выберите формат коробки:", reply_markup=get_box_corrugated_format_keyboard())
            
            elif 'box_corrugated_color' in current_state:
                from keyboards.packaging import get_box_corrugated_color_keyboard
                await message.answer("Выберите цвет микрогофры:", reply_markup=get_box_corrugated_color_keyboard())
            
            elif 'box_corrugated_logo' in current_state:
                from keyboards.packaging import get_box_corrugated_logo_keyboard
                await message.answer("Выберите нанесение логотипа:", reply_markup=get_box_corrugated_logo_keyboard())
            
            # === ИНТЕРЬЕРНАЯ ПЕЧАТЬ ===
            elif 'sign_type' in current_state:
                from keyboards.interior import get_sign_type_keyboard
                await message.answer("Выберите тип таблички:", reply_markup=get_sign_type_keyboard())
            
            elif 'sign_material' in current_state:
                from keyboards.interior import get_sign_material_keyboard
                await message.answer("Выберите материал:", reply_markup=get_sign_material_keyboard())
            
            elif 'canvas_size' in current_state:
                from keyboards.interior import get_canvas_size_keyboard
                await message.answer("Выберите размер холста:", reply_markup=get_canvas_size_keyboard())
            
            elif 'canvas_framing' in current_state:
                from keyboards.interior import get_canvas_framing_keyboard
                await message.answer("Выберите оформление:", reply_markup=get_canvas_framing_keyboard())
            
            elif 'banner_print_type' in current_state:
                from keyboards.interior import get_banner_print_type_keyboard
                await message.answer("Выберите тип печати:", reply_markup=get_banner_print_type_keyboard())
            
            elif 'banner_edge_processing' in current_state:
                from keyboards.interior import get_banner_edge_processing_keyboard
                await message.answer("Выберите обработку краев:", reply_markup=get_banner_edge_processing_keyboard())
            
            elif 'banner_grommets' in current_state:
                from keyboards.interior import get_banner_grommets_keyboard
                await message.answer("Выберите крепление:", reply_markup=get_banner_grommets_keyboard())
            
            elif 'interior_sticker_film_type' in current_state:
                from keyboards.interior import get_interior_sticker_film_type_keyboard
                await message.answer("Выберите тип плёнки:", reply_markup=get_interior_sticker_film_type_keyboard())
            
            elif 'interior_sticker_processing' in current_state:
                from keyboards.interior import get_interior_sticker_processing_keyboard
                await message.answer("Выберите дополнительную обработку:", reply_markup=get_interior_sticker_processing_keyboard())
            
            # === СУВЕНИРЫ ===
            elif 'pen_material' in current_state:
                from keyboards.souvenirs import get_pen_material_keyboard
                await message.answer("Выберите материал корпуса:", reply_markup=get_pen_material_keyboard())
            
            elif 'pen_application' in current_state:
                from keyboards.souvenirs import get_pen_application_keyboard
                await message.answer("Выберите способ нанесения:", reply_markup=get_pen_application_keyboard())
            
            elif 'pen_color' in current_state:
                from keyboards.souvenirs import get_pen_color_keyboard
                await message.answer("Выберите цвет корпуса:", reply_markup=get_pen_color_keyboard())
            
            elif 'tshirt_size' in current_state:
                from keyboards.souvenirs import get_tshirt_size_keyboard
                await message.answer("Выберите размер:", reply_markup=get_tshirt_size_keyboard())
            
            elif 'tshirt_material' in current_state:
                from keyboards.souvenirs import get_tshirt_material_keyboard
                await message.answer("Выберите материал и цвет:", reply_markup=get_tshirt_material_keyboard())
            
            elif 'tshirt_print_position' in current_state:
                from keyboards.souvenirs import get_tshirt_print_position_keyboard
                await message.answer("Выберите расположение принта:", reply_markup=get_tshirt_print_position_keyboard())
            
            elif 'mug_type' in current_state:
                from keyboards.souvenirs import get_mug_type_keyboard
                await message.answer("Выберите тип кружки:", reply_markup=get_mug_type_keyboard())
            
            elif 'mug_print_position' in current_state:
                from keyboards.souvenirs import get_mug_print_position_keyboard
                await message.answer("Выберите расположение принта:", reply_markup=get_mug_print_position_keyboard())
            
            elif 'mug_packaging' in current_state:
                from keyboards.souvenirs import get_mug_packaging_keyboard
                await message.answer("Выберите дополнительную упаковку:", reply_markup=get_mug_packaging_keyboard())
            
            # === ПЕЧАТИ И ШТАМПЫ ===
            elif 'stamp_type' in current_state:
                from keyboards.stamps import get_stamps_main_keyboard
                await message.answer("Выберите тип печати:", reply_markup=get_stamps_main_keyboard())
            
            elif 'stamp_format' in current_state:
                from keyboards.stamps import get_stamp_format_keyboard
                await message.answer("Выберите формат печати:", reply_markup=get_stamp_format_keyboard())
            
            elif 'stamp_ink_color' in current_state:
                from keyboards.stamps import get_stamp_ink_color_keyboard
                await message.answer("Выберите цвет штемпельной подушки:", reply_markup=get_stamp_ink_color_keyboard())
            
            # === ФОТОПЕЧАТЬ ===
            elif 'photo_format' in current_state:
                from keyboards.photoprint import get_photo_format_keyboard
                await message.answer("Выберите формат бумаги:", reply_markup=get_photo_format_keyboard())
            
            elif 'photo_print_type' in current_state:
                from keyboards.photoprint import get_photo_print_type_keyboard
                await message.answer("Выберите тип печати фото:", reply_markup=get_photo_print_type_keyboard())
            
            elif 'main_menu' in current_state:
                from keyboards.photoprint import get_main_menu_keyboard
                await message.answer("Главное меню", reply_markup=get_main_menu_keyboard())

            # === ОБЩИЕ СОСТОЯНИЯ ===
            elif 'waiting_for_quantity' in current_state:
                await message.answer(
                    "Введите количество цифрами:",
                    reply_markup=ReplyKeyboardMarkup(
                        keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
                        resize_keyboard=True
                    )
                )
            
            elif 'waiting_for_comment' in current_state:
                from keyboards.copycenter import get_comment_keyboard
                await message.answer("Хотите добавить примечание?", reply_markup=get_comment_keyboard())
            
            elif 'waiting_for_files' in current_state:
                from keyboards.copycenter import get_files_keyboard
                await message.answer("Прикрепите файлы для печати:", reply_markup=get_files_keyboard())
            
            # Общий fallback для размеров
            elif any(x in current_state for x in ['_size', 'box_cardboard_size', 'sign_size', 
                                                  'banner_size', 'interior_sticker_size']):
                await message.answer(
                    f"Введите размеры для {service_type} в нужном формате (например: 100×200 мм):",
                    reply_markup=ReplyKeyboardMarkup(
                        keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
                        resize_keyboard=True
                    )
                )
            
            else:
                # Общий fallback
                from keyboards.main_menu import get_main_menu_keyboard
                await message.answer(
                    "Пожалуйста, используйте предложенные варианты или вернитесь в главное меню:",
                    reply_markup=get_main_menu_keyboard()
                )
                
        except ImportError as e:
            # Если не удалось импортировать клавиатуру
            print(f"Import error in validation middleware: {e}")
            await message.answer(
                f"Пожалуйста, используйте предложенные варианты для раздела '{service_type}'.",
                reply_markup=ReplyKeyboardMarkup(
                    keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
                    resize_keyboard=True
                )
            )
        except Exception as e:
            # Общая обработка ошибок
            print(f"Error in validation middleware: {e}")
            from keyboards.main_menu import get_main_menu_keyboard
            await message.answer(
                "Произошла ошибка. Пожалуйста, вернитесь в главное меню и попробуйте снова.",
                reply_markup=get_main_menu_keyboard()
            )