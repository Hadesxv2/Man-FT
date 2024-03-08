# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" ft module for other small commands. """
from ft import CMD_HANDLER as cmd
from ft import CMD_HELP
from ft.utils import edit_or_reply, man_cmd


@man_cmd(pattern="ihelp$")
async def usit(event):
    me = await event.client.get_me()
    await edit_or_reply(
        event,
        f"**Hai {me.first_name} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        f"✣ **Group :** [Ngobrol](https://t.me/HadesxGroup)\n"
        f"✣ **Channel VPN:** [H a d e s x VPN](https://t.me/HadesxVPN)\n"
        f"✣ **Owner Repo :** [𝐇 𝐚 𝐝 𝐞 𝐬 𝐱](https://t.me/iHadesx)\n"
        f"✣ **Repo :** [Man-FT](https://github.com/Hadesxv2/Man-FT)\n",
    )


@man_cmd(pattern="listvar$")
async def var(event):
    await edit_or_reply(
        event,
        "**Daftar Lengkap Vars Dari Man-FT:** [KLIK DISINI](https://t.me/HadesxGroup)",
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  •  **Syntax :** `{cmd}ihelp`\
        \n  •  **Function : **Bantuan Untuk Man-FT.\
        \n\n  •  **Syntax :** `{cmd}listvar`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Syntax :** `{cmd}repo`\
        \n  •  **Function : **Melihat Repository Man-FT.\
        \n\n  •  **Syntax :** `{cmd}string`\
        \n  •  **Function : **Link untuk mengambil String Man-FT.\
    "
    }
)
