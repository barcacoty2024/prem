from PyroUbot import *

__MODULE__ = "prefix"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴇғɪx 』</b>

<b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}prefix [trigger]
<b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> : Untuk mengatur handler userbot anda.
"""


@PY.UBOT("prefix")
async def _(client, message):
    await kok_anjeng(client, message)
