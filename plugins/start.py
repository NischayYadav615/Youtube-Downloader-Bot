from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/botbynischay")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/Nischayyadav")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help Welcome, The Most Advanced utube Video and Audio Downloader in Telegram!"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
