# This is a troll indeed ffs *facepalm*
# Ported from xtra-telegram by @heyworld
import asyncio
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
#from userbot.utils import admin_cmd
from userbot.events import geezbot_cmd
from userbot import CUSTOM_CMD as geez
from userbot import ALIVE_NAME, CMD_HELP, bot

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@bot.on(geezbot_cmd(outgoing=True, pattern="fgban(?: |$)(.*)"))
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = f"`Cảnh báo!! Người dùng 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 bởi` {DEFAULTUSER}\n"
    no_reason = "Không có lý do "
    await event.edit("**Triệu hồi chiếc búa gban dũng mãnh ☠️**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 1411273575:
            await reply_message.reply("`Chờ đã, đây là chủ nhân của tôi!!`😏")
        else:
            jnl = ("`Cảnh báo!!`"
                   "[{}](tg://user?id={})"
                   f"` 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By` {DEFAULTUSER}\n\n"
                   "**Tên: ** __{}__\n"
                   "**ID : ** `{}`\n"
                   ).format(firstname, idd, firstname, idd)
            if usname is None:
                jnl += "**Username: ** `Không sở hữu tên người dùng!`\n"
            elif usname != "None":
                jnl += "**Username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Lý do: **" + gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = (
            f"Warning!! Người dùng bị 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 bởi {DEFAULTUSER} \nLý do: Không có lý do. ")
        await event.reply(mention)
    await event.delete()

CMD_HELP.update({
    "fakegban": f"`{geez}fgban`\
    \nUsage: Nhập .fgban hoặc Trả lời lý do .fgban và tự xem điều đó. "
})
