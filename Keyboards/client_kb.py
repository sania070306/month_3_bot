from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('YES'), KeyboardButton('NO'))


direction_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

frontend = KeyboardButton('Frontend-developer(HTML, CSS, JavaScript)')
backend = KeyboardButton('Backend-developer(Python, Django')
fullstack = KeyboardButton('Fullstack-developer(Frontend + Backend)')
android_iOS = KeyboardButton('Android (Java, Kotlin)/iOS(SWIFT)')
ux_ui = KeyboardButton('UX/UI designer')
basics_of_prog = KeyboardButton('basics of programming')

direction_markup.add(frontend, backend, fullstack, android_iOS, basics_of_prog, ux_ui).add(KeyboardButton('CANCEL'))


cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('CANCEL'))