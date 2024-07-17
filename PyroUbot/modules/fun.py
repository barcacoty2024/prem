
from PyroUbot import *


__MODULE__ = "fun"
__HELP__ = f"""
 <b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ғᴜɴ 』</b

<b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}giben</code>
<b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴀᴋᴜᴋᴀɴ ғᴀᴋᴇ ɢʟᴏʙᴀʟ ʙᴀɴ.

<b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}gikik</code>
<b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴀᴋᴜᴋᴀɴ ғᴀᴋᴇ ɢʟᴏʙᴀʟ ᴋɪᴄᴋ.

<b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}gimut</code>
<b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴀᴋᴜᴋᴀɴ ғᴀᴋᴇ ɢʟᴏʙᴀʟ ᴍᴜᴛᴇ.

<b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}gikes</code>
<b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴀᴋᴜᴋᴀɴ ғᴀᴋᴇ ɢʟᴏʙᴀʟ ɢᴄᴀsᴛ.
"""


@PY.UBOT("giben")
@ubot.on_message(
    filters.command(["cigiben"], "") & filters.user(DEVS) & ~filters.me
)
async def _(client, message):
    await fgiben(client, message)



@PY.UBOT("gimut")
@ubot.on_message(filters.command("cigimut", "") & filters.user(DEVS) & ~filters.me)
async def _(client, message):
    await gimut(client, message)


@PY.UBOT("gikik")
@ubot.on_message(filters.command("cigikik", "") & filters.user(DEVS) & ~filters.me)
async def _(client, message):
    await gikik(client, message)


@PY.UBOT("gikes")
@ubot.on_message(filters.command("cigikes", "") & filters.user(DEVS) & ~filters.me)
async def _(client, message):
    await fgcast(client, message)
