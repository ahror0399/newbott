from typing import List

from aiogram import types
from aiogram.dispatcher.filters import Command, MediaGroupFilter
from aiogram.types import ContentType

from loader import dp, bot
from aiogram_media_group import media_group_handler

channel_id = -1001600489294
channel_link = "https://t.me/+cek_ScsoO6Q0NmRk"


# @dp.message_handler(MediaGroupFilter(is_media_group=True), content_types=ContentType.PHOTO)
# async def media_group(message: types.Message):
#     await bot.copy_message(chat_id=message.from_user.id, from_chat_id=message.from_user.id,
#                            message_id=message.message_id)


@dp.message_handler(MediaGroupFilter(is_media_group=True), content_types=ContentType.ANY)
async def media_group(message: types.Message):
    # txt = ""
    # caption = message.caption
    # caption_split = caption.split("\n")
    # for tx in caption_split:
    #     if tx.__contains__("@") or tx.__contains__("http"):
    #         break
    #     else:
    #         txt = txt + f"\n{tx}"
    # txt = f"<b>{txt} \n👉 {channel_link} </b> - энг тезкор ва махфий хабарлар каналига аъзо бўлинг!"

    media = types.MediaGroup()
    # state = True
    for photo in message:
        # if state:
        #     media.attach_photo(photo.file_id, caption=txt)
        #     state = False
        # else:
        media.attach({"media": message[message.content_type].file_id, "type": message.content_type})
    await bot.send_media_group(chat_id=message.from_user.id, media=media)

# await message.bot.send_media_group(message.from_user.id,message.media_group_id)
# media_group = types.MediaGroup()
# for obj in album:
#     if obj.photo:
#         file_id = obj.photo[-1].file_id
#     else:
#         file_id = obj[obj.content_type].file_id
#
#     try:
#         # We can also add a caption to each file by specifying `"caption": "text"`
#         media_group.attach({"media": file_id, "type": obj.content_type})
#     except ValueError:
#         return await message.answer("This type of album is not supported by aiogram.")
#
# await message.answer_media_group(media_group)

#
# @dp.message_handler(content_types=types.ContentType.TEXT)
# async def send_text(message: types.Message):
#     caption = message.text
#     txt = ""
#     caption_split = caption.split("\n")
#     for tx in caption_split:
#         if tx.__contains__("@") or tx.__contains__("http"):
#             break
#         else:
#             txt = txt + f"\n{tx}"
#     txt = f"<b>{txt}  </b>"
#     await bot.send_message(chat_id=channel_id, text=txt)
#


#
# @dp.message_handler(content_types=types.ContentType.ANY)
# async def send_any(message: types.Message):
#     txt = ""
#     caption = message.caption
#
#     if caption is not None:
#         caption_split = caption.split("\n")
#         for tx in caption_split:
#             if tx.__contains__("@") or tx.__contains__("http"):
#                 break
#             else:
#                 txt = txt + f"\n{tx}"
#
#     txt = f"<b>{txt} \n👉 {channel_link} </b> - энг тезкор ва махфий хабарлар каналига аъзо бўлинг!"
#
#     if message.content_type == "photo":
#         file_id = message.photo[-1].file_id
#         await bot.send_photo(chat_id=channel_id, photo=file_id, caption=txt)
#
#     elif message.content_type == "video":
#         file_id = message.video.file_id
#         await bot.send_video(chat_id=channel_id, video=file_id, caption=txt)
#
#     elif message.content_type == "document":
#         file_id = message.document.file_id
#         await bot.send_document(chat_id=channel_id, document=file_id, caption=txt)
#
#     elif message.content_type == "animation":
#         file_id = message.animation.file_id
#         await bot.send_animation(chat_id=channel_id, animation=file_id, caption=txt)
#
#     elif message.content_type == "audio":
#         file_id = message.audio.file_id
#         await bot.send_audio(chat_id=channel_id, audio=file_id, caption=txt)
#
#     elif message.content_type == "voice":
#         file_id = message.voice.file_id
#         await bot.send_voice(chat_id=channel_id, voice=file_id, caption=txt)
#
#     elif message.content_type == "video_note":
#         file_id = message.video_note.file_id
#         await bot.send_video_note(chat_id=channel_id, video_note=file_id, caption=txt)
