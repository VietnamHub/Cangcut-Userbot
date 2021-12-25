# Thank For CatUserBot
# Ported By @VckyouuBitch
# FROM Geez - Projects <https://github.com/Vckyou/GeezProjects>

from telethon.tl.functions.contacts import BlockRequest, UnblockRequest

from telethon.tl.types import (
    MessageEntityMentionName,
)

from userbot import bot, BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import geezbot_cmd
from userbot import CUSTOM_CMD as geez


async def get_full_user(event):
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`ID người dùng là bắt buộc`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Có gì đó sai", str(err))
    return user_obj, extra


async def get_user_sender_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


@bot.on(geezbot_cmd(outgoing=True, pattern=r"gban(?: |$)(.*)"))
async def gspider(userbot):
    lol = userbot
    sender = await lol.get_sender()
    me = await lol.client.get_me()
    if not sender.id == me.id:
        friday = await lol.reply("Gbanning người dùng..")
    else:
        friday = await lol.edit("Chờ xử lý.....")
    me = await userbot.client.get_me()
    await friday.edit(f"**Đã cấm người dùng khỏi toàn bộ nhóm tôi làm admin..**")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await friday.edit(f"**Có một lỗi!!**")
    if user:
        if user.id == 1920635554:
            return await friday.edit(
                f"**Cha của bạn đã không dạy bạn? Rằng bạn không thể cấm người sáng tạo của bạn🖕**"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await friday.edit(f"**GBANNED // Tổng số cuộc trò chuyện bị ảnh hưởng **: `{a}`")
            except BaseException:
                b += 1
    else:
        await friday.edit(f"**Trả lời người dùng!!**")
    try:
        if gmute(user.id) is False:
            return await friday.edit(f"**Lỗi! Người dùng đã bị cấm.**")
    except BaseException:
        pass
    return await friday.edit(
        f"**Đã cấm [{user.first_name}](tg://user?id={user.id}) khỏi {a} nhóm**"
    )

    if BOTLOG:
        await userbot.client.send_message(
            BOTLOG_CHATID,
            "#GMUTE\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {userbot.chat.title}(`{userbot.chat_id}`)",
        )


@bot.on(geezbot_cmd(outgoing=True, pattern=r"ungban(?: |$)(.*)"))
async def gspider(userbot):
    lol = userbot
    sender = await lol.get_sender()
    me = await lol.client.get_me()
    if not sender.id == me.id:
        friday = await lol.reply("`Chờ để tôi xử lý`")
    else:
        friday = await lol.edit("Chỉ một giây thôi ")
    me = await userbot.client.get_me()
    await friday.edit(f"Đang cố gắng Bỏ cấm người dùng!")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await friday.edit("Có một lỗi !!")
    if user:
        if user.id == 1920635554:
            return await friday.edit("**Bạn không thể cấm anh ta ... kết quả là bạn không thể cấm anh ta ... Anh ta là Người tạo ra tôi!**")
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await friday.edit(f"**UNGBANNING // TRÒ CHUYỆN CÓ ẢNH HƯỞNG - {a} **")
            except BaseException:
                b += 1
    else:
        await friday.edit("**Trả lời người dùng !!**")
    try:
        if ungmute(user.id) is False:
            return await friday.edit("**Lỗi! Người dùng có thể đã được bỏ cấm.**")
    except BaseException:
        pass
    return await friday.edit(
        f"**UNGBANNED // USER - [{user.first_name}](tg://user?id={user.id}) CHATS : {a} **"
    )


CMD_HELP.update({
    "gban": f"\
`{geez}gban reason`\
\nUsage: Trên toàn cầu Cấm người dùng khỏi tất cả các bot Quản trị nhóm nơi bạn là SUDO.\
\n\n`{geez}ungban reason`\
\nUsage: Bỏ Cấm người dùng trên toàn cầu khỏi tất cả các bot Quản trị nhóm nơi bạn đang SUDO"
})
