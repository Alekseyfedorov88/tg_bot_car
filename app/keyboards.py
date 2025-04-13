from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

main_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Заявка на просчет авто 🟢')],
    [KeyboardButton(text='Открыть сайт', web_app=WebAppInfo(url='https://jdm-for.ru'))],
    [KeyboardButton(text='Соц.сети'),
    KeyboardButton(text='Контакты')],
    [KeyboardButton(text='О нас'),
    KeyboardButton(text='FAQ ❓')],
], 
resize_keyboard=True,
input_field_placeholder='Выберите действие..'
)


# social groups for cartrading
social_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Канал про JDM', url='https://t.me/+45nJUgjYLeo3ZjQy')],
    [InlineKeyboardButton(text='Канал о доставки авто', url='https://t.me/+HSJPhANQjAk4MmFi')],
    [InlineKeyboardButton(text='ВК сообщество', url='https://vk.com/jdmforrus')],
    [InlineKeyboardButton(text='Перейти на сайт', url='https://jdm-for.ru')]
])

# Contacts
Contacts = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ростислав - менеджер', url='https://t.me/rosvlas')],
    [InlineKeyboardButton(text='Алексей - маркетолог', url='https://t.me/fedorovaleksey88')],
    [InlineKeyboardButton(text='Тех.поддержка (если нашли ошибку)', url='https://t.me/fedorovaleksey88')]
])

# Add the confirmation_menu here
confirmation_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Подтвердить🟢", callback_data="confirm"),
        InlineKeyboardButton(text="Отменить", callback_data="cancel")
    ]
])