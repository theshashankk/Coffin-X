from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, π'πΊ β¨ ππ‘π¦ππππ'π¦ π π¨π¦ππ π£πππ¬ππ₯ β’ β¨
I can play music in your group's voice call. Developed by [πNSHIKAπ₯°](https://t.me/Anshika_4).
Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π€π»ππΎππ πΌπ°πΊπ΄ππ€π»", url="https://t.me/Anshika_4")
                  ],[
                    InlineKeyboardButton(
                        "π°πΆππΎππΏπ°", url="https://t.me/Schoolmastii"
                    ),
                    InlineKeyboardButton(
                        "ποΈ π²πΎπΌπΌπ°π½π³π ποΈ", url="https://telegra.ph/MusicBot-Robot-MusicBot-Robo-03-14"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "π π°π³π³ ππΎ ππΎππ πΆππΎππΏ π", url="https://t.me/ANSHIKA_MUSIC_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**β¨ ππ‘π¦ππππ β¨ is on fire π₯ β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "πΏπ»π°ππΈπ½πΆ π±π ππΎππ π€π»", url="https://t.me/Anshika_4")
                ]
            ]
        )
   )

