import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/299c51cf401307e635b8d.jpg",
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 🎶 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜.
𝐂𝐫𝐞𝐚𝐭𝐨𝐫 :- [✨𝐌𝐑.𝐄𝐕𝐄𝐑𝐄𝐓𝐓🚬 💜](https://t.me/D_E_V_l_L)
𝐒𝐮𝐩𝐩𝐨𝐫𝐭 :- [✨ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ❤️🎸](https://t.me/ABOUT_DEVIL_DAD)
𝐃𝐢𝐬𝐜𝐮𝐬𝐬 :- [✨ 𝐌𝐑.𝐃𝐄𝐕𝐈𝐋 🎧](https://t.me/D_E_V_l_L)
𝐒𝐨𝐮𝐫𝐜𝐞  :- [✨  𝗖𝗹𝗶𝗰𝗸 ☑️ 𝗥𝗲𝗽𝗼 🌍](https://t.me/D_E_V_l_L)
𝐌𝐎𝐕𝐈𝐄𝐒:- [𝐅𝐎𝐑 𝐌𝐎𝐕𝐈𝐄🚩](https://t.me/backup_channel_000)
𝐅𝐞𝐞𝐋𝐢𝐧𝐠'𝐒 :- [✨ 𝗝𝗼𝗶𝗻 ❤️🥀](https://t.me/ABOUT_DEVIL_DAD)

𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [𝗠𝗿.𝐄𝐕𝐄𝐑𝐄𝐓𝐓🚬 ❤️](https://t.me/D_E_V_l_L)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 Jᴏɪɴ Hᴇʀᴇ & Sᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/ABOUT_DEVIL_DAD")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/299c51cf401307e635b8d.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Cʟɪᴄᴋ Mᴇ Tᴏ Gᴇᴛ Rᴇᴘᴏ 💞", url=f"https://github.com/kkverma25/SmokerMusicX")
                ]
            ]
        ),
    )
