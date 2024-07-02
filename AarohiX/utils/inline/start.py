from typing import Union
from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="zzzback")
        ],
        [
            InlineKeyboardButton(text=_["S_B_10"], url=f"https://t.me/ST_B0"),
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=f"https://t.me/R_surce"),
            InlineKeyboardButton(text=_["S_B_2"], url=f"https://t.me/B_A_H_R5")
        ],
    ]
    return buttons