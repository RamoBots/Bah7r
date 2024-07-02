import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from random import  choice, randint

@app.on_message(
    filters.command(["سورس مين","سورس","السورس","سورسي", "𝗠𝗥  𝐑𝙄𝙆𝙊"], ""))
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/cf2f6bafc7b1ed489a95a.mp4",
        caption=f"""᭙ᥱᥣᥴ᥆ꪔᥱ ƚ᥆ ᥉᥆ᥙᖇᥴᥱ 𝑅𝑖𝑘𝑜 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                text="𝗦𝗼𝘂𝗿𝗰𝗲  𝐑𝙄𝙆𝙊", url=f"https://t.me/R_surce"
                        ),
           InlineKeyboardButton(
                text="𝗚𝗿𝗼𝘂𝗽", url=f"https://t.me/B_A_H_R5"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝗠𝗥  𝐑𝙄𝙆𝙊", url=f"https://t.me/ST_B0"
            ),
  
                ],

            ]

        ),

    )


@app.on_message(filters.command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
