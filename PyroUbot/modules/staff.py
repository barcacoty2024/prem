from ubot import *

__MODULE__ = "staff"
__HELP__ = f"""
 <b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛᴀғғ 』</b>

<b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}staff</code>
<b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴅᴀғᴛᴀʀ sᴇᴍᴜᴀ ᴀᴅᴍɪɴ ᴅɪᴅᴀʟᴀᴍ ɢʀᴜᴘ.
"""

@PY.UBOT("staff")
async def _(client, message):
    await staff_cmd(client, message)
