
# Thanks to @D3_krish
# Porting in MafiaBot by @H1M4N5HU0P

import asyncio
import random
from telethon import events, version
from userbot import mafiaversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from . import *
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ππΈπ½ππΈπΉππ"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

MAFIA_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/852a8de1eaa17e61867c2.jpg"
pm_caption = "  __**ππ¦π¨π₯π§π¨π₯ππ’π§ ππ¦ ππππ©ππ**__\n\n"

pm_caption += f"**ββββββββββββββββββββ**\n\n"
pm_caption += (
    f"                 ππΎππ½π΄ππ\n  **γπ[{DEFAULTUSER}](tg://user?id={mafia})πγ**\n\n"
)
pm_caption += f"ββββββββββββββββββββ\n"
pm_caption += f"β£β’β³β  `Telethon:` `{version.__version__}` \n"
pm_caption += f"β£β’β³β  `Version:` `{mafiaversion}`\n"
pm_caption += f"β£β’β³β  `Sudo:` `{sudou}`\n"
pm_caption += f"β£β’β³β  `Channel:` [α΄α΄ΙͺΙ΄](https://t.me/surturbot_Support)\n"
pm_caption += f"β£β’β³β  `Creator:` [RISHABH](https://t.me/Mafiarishabh)\n"
pm_caption += f"ββββββββββββββββββββ\n"
pm_caption += " [π₯REPOπ₯](https://github.com/Mafiarishabh/SURTUR-BOT) πΉ [δΈγ©ε©ε©γε°Ίγ](https://t.me/surturbot_Support)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, MAFIA_IMG,caption=pm_caption)

    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add()
