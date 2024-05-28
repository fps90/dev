from pyrogram import filters
from YukkiMusic.utils.database import get_client
from YukkiMusic import app
from YukkiMusic.core.userbot import assistants

@app.on_message(filters.command(["اضفني","add","سجلني"]))
async def add_contact(client, message):
    try:
        for num in assistants:
            USER = await get_client(num)
            try:
                if message.from_user.username:
                    await USER.add_contact(message.from_user.username, message.from_user.first_name)
                else:
                    await USER.add_contact(message.from_user.id, message.from_user.first_name)
                await message.reply_text("You have been added to the contacts of the assistant's account in Netah ")
            except Exception as e:
                await message.reply_text(f"Error : {e}")
    except Exception as e:
            await message.reply_text(f"Error : {e}")
