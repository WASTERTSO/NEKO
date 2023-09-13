import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from NekoRobot import tbot as bot
from NekoRobot import tbot as tgbot
from NekoRobot.events import register

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/36440524ecd0a6b65138f.jpg"
file2 = "https://telegra.ph/file/b0868af85d1d17554a6d4.jpg"
file3 = "https://telegra.ph/file/60c612b4736560f9b98b9.jpg"
file4 = "https://telegra.ph/file/a502e6322a201f5949058.jpg"
file5 = "https://telegra.ph/file/737a7b4d519887c35ed21.jpg"
""" =======================CONSTANTS====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    betsy = event.sender.first_name
    button = [[custom.Button.inline("𝐶𝑙𝑖𝑐𝑘 𝐻𝑒𝑟𝑒", data="information")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"ʜᴇʏ {betsy}, \nɪ'ᴍ ᴄʀᴇᴀᴛᴇᴅ ʙʏ [ʏᴏᴜʀ sʜɪᴠ](tg://user?id=5686536025)\nᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ɪɴғᴏ",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        NEKO = "ʏᴏᴜʀ ᴅᴇᴛᴀɪʟs \n\n"
        NEKO += f"ғɪʀsᴛ ɴᴀᴍᴇ  : {PRO.first_name} \n"
        NEKO += f"ʟᴀsᴛ ɴᴀᴍᴇ : {PRO.last_name}\n"
        NEKO += f"ʏᴏᴜ ʙᴏᴛ : {PRO.bot} \n"
        NEKO += f"ʀᴇsᴛʀɪᴄᴛᴇᴅ : {PRO.restricted} \n"
        NEKO += f"ᴜsᴇʀ ɪᴅ : {boy}\n"
        NEKO += f"ᴜsᴇʀɴᴀᴍᴇ : {PRO.username}\n"
        await event.answer(NEKO, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__help__ = """
/myinfo: shows your info in inline button
"""

__mod_name__ = "ᴍʏ-ɪɴғᴏ"
__command_list__ = ["myinfo"]
