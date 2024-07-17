from PyroUbot import *

__MODULE__ = "button"
__HELP__ = f"""
 <b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙᴜᴛᴛᴏɴ 』</b>

<b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}button</code> Teks ~ Button Teks|Button Link.
<b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇᴋs ᴍᴇɴᴊᴀᴅɪ ʙᴜᴛᴛᴏɴ.

• Contoh : Google ~ Klik Disini|google.com
"""


@PY.UBOT("button")
async def _(client, message):
    await cmd_button(client, message)


@PY.INLINE("^get_button")
@INLINE.QUERY
async def _(client, inline_query):
    await inline_button(client, inline_query)
