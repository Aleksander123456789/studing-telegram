from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

start_button = KeyboardButton("START")
start
q1_a = KeyboardButton("< 1k")
q1_b = KeyboardButton("1k - 10k")
q1_c = KeyboardButton("10k - 1kk")
q1_d = KeyboardButton("> 1kk")

q1_answer = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
    ).insert(q1_a).insert(q1_b).add(q1_c).add(q1_d)


q2_a = KeyboardButton("2023")
q2_b = KeyboardButton("8000")
q2_c = KeyboardButton("6.5kkk")
q2_d = KeyboardButton("Земли не существует")

q2_answer = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
    ).insert(q2_a).insert(q2_b).add(q2_c).add(q2_d)


q3_a = KeyboardButton("Белым карликом")
q3_b = KeyboardButton("Жёлтым карликом")
q3_c = KeyboardButton("Крсным карликом")
q3_d = KeyboardButton("Красным гигантом")

q3_answer = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
    ).insert(q3_a).insert(q3_b).add(q3_c).add(q3_d)


