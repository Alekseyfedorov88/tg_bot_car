from aiogram import F, Router, Bot
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import logging

import app.keyboards as kb

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = Router()

# Define states for the form
class Form(StatesGroup):
    name = State()
    phone = State()
    car_model = State()
    budget = State()
    comment = State()
    confirmation = State()

@router.message(F.text == 'Заявка на просчет авто 🟢')
async def start_form(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("Пожалуйста, введите ваше имя:", reply_markup=ReplyKeyboardRemove())

@router.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.phone)
    await message.answer("Теперь введите ваш номер телефона:")

@router.message(Form.phone)
async def process_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(Form.car_model)
    await message.answer("Какую модель автомобиля вы ищете?")

@router.message(Form.car_model)
async def process_car_model(message: Message, state: FSMContext):
    await state.update_data(car_model=message.text)
    await state.set_state(Form.budget)
    await message.answer("Какой у вас бюджет на покупку?")

@router.message(Form.budget)
async def process_budget(message: Message, state: FSMContext):
    await state.update_data(budget=message.text)
    await state.set_state(Form.comment)
    await message.answer("Укажите, если имеется, комм. по выбору:/n"
                         "цвет, год, пробег, топливо, привод, объем дв.. ?")

@router.message(Form.comment)
async def process_comment(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    data = await state.get_data()
    await state.set_state(Form.confirmation)
    confirmation_text = (
        f"Проверьте ваши данные:\n"
        f"Имя: {data['name']}\n"
        f"Телефон: {data['phone']}\n"
        f"Модель автомобиля: {data['car_model']}\n"
        f"Бюджет: {data['budget']}\n"
        f"Комментарий: {data['comment']}\n"
        f"Все верно?"
    )
    await message.answer(confirmation_text, reply_markup=kb.confirmation_menu)

@router.callback_query(F.data == "confirm", Form.confirmation)
async def process_confirmation(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()
    manager_chat_ids = [1101051783, 347709146]  
    logger.info(f"Attempting to send message to manager_chat_ids: {manager_chat_ids}")
    manager_message = (
        f"Новая заявка:\n"
        f"Имя: {data['name']}\n"
        f"Телефон: {data['phone']}\n"
        f"Модель автомобиля: {data['car_model']}\n"
        f"Бюджет: {data['budget']}\n"
        f"Комментарий: {data['comment']}"
    )
    for manager_chat_id in manager_chat_ids:
        try:
            await bot.send_message(chat_id=manager_chat_id, text=manager_message)
            logger.info(f"Message sent successfully to manager_chat_id: {manager_chat_id}")
        except Exception as e:
            logger.error(f"Error sending message to manager {manager_chat_id}: {e}")
    await callback.message.answer("Спасибо! Ваша заявка отправлена менеджеру.", reply_markup=kb.main_menu)
    await state.clear()
    await callback.answer()

@router.callback_query(F.data == "cancel", Form.confirmation)
async def process_cancel(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Заявка отменена.", reply_markup=kb.main_menu)
    await state.clear()
    await callback.answer()
