from aiogram import Router
from aiogram.types import Message
from app.parser.digital_ocean import get_url
from settings import URL

from aiogram.filters import Command

from aiogram.fsm.context import FSMContext
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

router: Router = Router()


url_api = f"{URL}/api/static-content/v1/tags/"

@router.message(Command("tags"))
async def any_message(message: Message, state: FSMContext):
    print("echo")
    out: list = await get_url(url_api)
    print(list)
    all_slug = "_".join([item.get("slug") for item in out])
    # await message.reply(text=f"I'am echo!!! \n {all_slug}")
    # await message.reply(text=f"I'am echo!!! \n ")
    await state.clear()
    await message.answer(
        f"Nice to meet you, {message.text}!\nDid you like to write bots?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[

                    #                 KeyboardButton(text="Yes"),
                    # KeyboardButton(text="No"),
                [
                    KeyboardButton(text=item.get("name")) for item in out
                ]
            ],
            resize_keyboard=True,
        ),
    )