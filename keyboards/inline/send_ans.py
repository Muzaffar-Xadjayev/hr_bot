from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

async def send_ans_btn(name):
    keyboard = InlineKeyboardMarkup(row_width=1)
    btn = InlineKeyboardButton(text=f"{name} ga javob qaytarish",callback_data="reklama:send_answer")
    keyboard.add(btn)

    return keyboard