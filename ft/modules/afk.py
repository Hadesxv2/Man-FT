# Copyright (C) 2020 TeamUltroid
# Ported by X_ImFine
# Recode by @mrismanaziz

import asyncio
from datetime import datetime

from telethon.tl import functions, types

from ft import CMD_HANDLER as cmd
from ft import CMD_HELP
from ft.utils import bash, man_cmd, man_handler

USER_AFK = {}
afk_time = None
last_afk_message = {}
last_afk_msg = {}
afk_start = {}


@man_handler(outgoing=True)
async def set_not_afk(event):
    global USER_AFK
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    user = await event.client.get_me()
    owner = user.first_name
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message = event.message.message
    if "afk" not in current_message and "yes" in USER_AFK:
        try:
            if pic.endswith((".tgs", ".webp")):
                shite = await event.client.send_message(event.chat_id, file=pic)
                shites = await event.client.send_message(
                    event.chat_id,
                    f"❏ **{owner} Kembali Online Untuk Parming**\n└ **Offline Selama** `{total_afk_time}` **Yang Lalu**",
                )
            else:
                shite = await event.client.send_message(
                    event.chat_id,
                    f"❏ **{owner} Pengangguran sok Sibuk Balik Lagi!**\n└ **Offline Selama** `{total_afk_time}` **Yang Lalu**",
                    file=pic,
                )
        except BaseException:
            shite = await event.client.send_message(
                event.chat_id,
                f"❏ **{owner} 𝙺𝚎𝚖𝚋𝚊𝚕𝚒 𝙾𝚗𝚕𝚒𝚗𝚎❤‍🔥**\n└ **𝙾𝚏𝚏𝚕𝚒𝚗𝚎 𝚂𝚎𝚕𝚊𝚖𝚊** `{total_afk_time}` **𝚈𝚊𝚗𝚐 𝙻𝚊𝚕𝚞**",
            )

        await asyncio.sleep(6)
        await shite.delete()
        try:
            await shites.delete()
        except BaseException:
            pass
        USER_AFK = {}
        afk_time = None

        await bash("rm -rf *.webp")
        await bash("rm -rf *.tgs")


@man_handler(incoming=True, func=lambda e: bool(e.mentioned or e.is_private))
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    user = await event.client.get_me()
    owner = user.first_name
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        return False
    if USER_AFK and not (await event.get_sender()).bot:
        msg = None
        if reason:
            message_to_reply = f"❏ **{owner}**  `𝚂𝚎𝚍𝚊𝚗𝚐 𝙾𝚏𝚏𝚕𝚒𝚗𝚎❌`\n├ **𝙳𝚊𝚛𝚒** `{total_afk_time}` **𝚈𝚊𝚗𝚐 𝙻𝚊𝚕𝚞**\n└ **𝙺𝚊𝚛𝚎𝚗𝚊:** `{reason}`"
        else:
            message_to_reply = (
                f"❏ **{owner}**  `𝚂𝚎𝚍𝚊𝚗𝚐 𝙾𝚏𝚏𝚕𝚒𝚗𝚎❌`\n└ **𝙳𝚊𝚛𝚒** `{total_afk_time}` **𝚈𝚊𝚗𝚐 𝙻𝚊𝚕𝚞**"
            )
        try:
            if pic.endswith((".tgs", ".webp")):
                msg = await event.reply(file=pic)
                msgs = await event.reply(message_to_reply)
            else:
                msg = await event.reply(message_to_reply, file=pic)
        except BaseException:
            msg = await event.reply(message_to_reply)
        await asyncio.sleep(2.5)
        if event.chat_id in last_afk_message:
            await last_afk_message[event.chat_id].delete()
        try:
            if event.chat_id in last_afk_msg:
                await last_afk_msg[event.chat_id].delete()
        except BaseException:
            pass
        last_afk_message[event.chat_id] = msg
        try:
            if msgs:
                last_afk_msg[event.chat_id] = msgs
        except BaseException:
            pass


@man_cmd(pattern="afk(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    global USER_AFK
    global afk_time
    global last_afk_message
    global last_afk_msg
    global afk_start
    global afk_end
    global reason
    global pic
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    last_afk_msg = {}
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    user = await event.client.get_me()
    owner = user.first_name
    pic = await event.client.download_media(reply) if reply else None
    if not USER_AFK:
        last_seen_status = await event.client(
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()
        USER_AFK = f"yes: {reason} {pic}"
        if reason:
            try:
                if pic.endswith((".tgs", ".webp")):
                    await event.client.send_message(event.chat_id, file=pic)
                    await event.client.send_message(
                        event.chat_id,
                        f"\n❏ **{owner}   Telah Offline❌**\n└ **Karena:** `{reason}`",
                    )
                else:
                    await event.client.send_message(
                        event.chat_id,
                        f"\n❏ **{owner}   Telah Offline❌**\n└ **Karena:** `{reason}`",
                        file=pic,
                    )
            except BaseException:
                await event.client.send_message(
                    event.chat_id,
                    f"\n❏ **{owner}  Telah Offline❌**\n└ **Karena:** `{reason}`",
                )
        else:
            try:
                if pic.endswith((".tgs", ".webp")):
                    await event.client.send_message(event.chat_id, file=pic)
                    await event.client.send_message(
                        event.chat_id, f"**❌ {owner} Telah Offline ❌**"
                    )
                else:
                    await event.client.send_message(
                        event.chat_id,
                        f"**❌ {owner} Telah Offline ❌**",
                        file=pic,
                    )
            except BaseException:
                await event.client.send_message(
                    event.chat_id, f"**❌ {owner} Telah Offline ❌**"
                )
        await event.delete()


CMD_HELP.update(
    {
        "afk": f"**Plugin : **`afk`\
        \n\n  •  **Syntax :** `{cmd}afk` <alasan> bisa <sambil reply sticker/foto/gif/media>\
        \n  •  **Function : **Memberi tahu kalau Master sedang afk bisa dengan menampilkan media keren ketika seseorang menandai atau membalas salah satu pesan atau dm Anda.\
        \n\n  •  **Syntax :** `{cmd}off`\
        \n  •  **Function : **Memberi tahu kalau Master sedang OFFLINE, dan menguubah nama belakang menjadi 【 OFF 】 \
    "
    }
)
