# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Port to userbot by @MoveAngel

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import geezbot_cmd
from userbot import CUSTOM_CMD as geez

from asyncio.exceptions import TimeoutError


# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Port to userbot by @MoveAngel


@bot.on(geezbot_cmd(outgoing=True, pattern=r"sg(?: |$)(.*)"))
async def lastname(steal):
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await steal.edit("```Trả lời bất kỳ tin nhắn nào của người dùng.```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await steal.edit("```Trả lời tin nhắn của người dùng thực tế.```")
        return
    await steal.edit("```Hãy ngồi yên trong khi tôi lấy cắp một số dữ liệu từ NASA```")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply(
                    "```Vui lòng bỏ chặn @sangmatainfo_bot và thử lại```"
                )
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await steal.edit(f"{r.message}")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                )
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await steal.edit("```Không tìm thấy hồ sơ nào cho người dùng này```")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await steal.edit(f"{response.message}")
            await steal.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await steal.edit("`Lỗi: `@ SangMataInfo_bot` không phản hồi!.`")


CMD_HELP.update({
    "sangmata":
        f"`{geez}sg`\
          \nUsage: Đánh cắp tên bạn hoặc bạn."
})
