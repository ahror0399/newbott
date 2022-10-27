from aiogram import types
from aiogram.dispatcher.filters import Command, MediaGroupFilter

from loader import dp, bot

channel_id = -1001768934286
channel_link = "@avto_elon_avtobozor"


@dp.message_handler(content_types=types.ContentType.TEXT)
async def send_text(message: types.Message):
    caption = message.text
    txt = ""
    caption_split = caption.split("\n")
    for tx in caption_split:
        if tx.__contains__("@") or tx.__contains__("http"):
            break
        else:
            txt = txt + f"\n{tx}"
    txt = f"<b>{txt}  </b>"
    await bot.send_message(chat_id=channel_id, text=txt)


@dp.message_handler(MediaGroupFilter(is_media_group=False), content_types=types.ContentType.ANY)
async def send_any(message: types.Message):
    txt = ""
    caption = message.caption

    if caption is not None:
        caption_split = caption.split("\n")
        for tx in caption_split:
            if tx.__contains__("@") or tx.__contains__("http"):
                break
            else:
                txt = txt + f"\n{tx}"

    txt = f"<b>{txt} 👉 {channel_link} </b> "

    if message.content_type == "photo":
        file_id = message.photo[-1].file_id
        await bot.send_photo(chat_id=channel_id, photo=file_id, caption=txt)

    elif message.content_type == "video":
        file_id = message.video.file_id
        await bot.send_video(chat_id=channel_id, video=file_id, caption=txt)

    elif message.content_type == "document":
        file_id = message.document.file_id
        await bot.send_document(chat_id=channel_id, document=file_id, caption=txt)

    elif message.content_type == "animation":
        file_id = message.animation.file_id
        await bot.send_animation(chat_id=channel_id, animation=file_id, caption=txt)

    elif message.content_type == "audio":
        file_id = message.audio.file_id
        await bot.send_audio(chat_id=channel_id, audio=file_id, caption=txt)

    elif message.content_type == "voice":
        file_id = message.voice.file_id
        await bot.send_voice(chat_id=channel_id, voice=file_id, caption=txt)

    elif message.content_type == "video_note":
        file_id = message.video_note.file_id
        await bot.send_video_note(chat_id=channel_id, video_note=file_id, caption=txt)
