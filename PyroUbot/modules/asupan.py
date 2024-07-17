from PyroUbot import *

__MODULE__ = "Asupan"
__HELP__ = f"""
 <b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀsᴜᴘᴀɴ 』</b>

<b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}asupan</code>
<b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>  ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ ᴀsᴜᴘᴀɴ ʀᴀɴᴅᴏᴍ.

<b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}bokep</code>
<b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ ʙᴏᴋᴇᴘ ʀᴀɴᴅᴏᴍ.

<b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}cewe</code>
<b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>  ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴄᴇᴡᴇᴋ ʀᴀɴᴅᴏᴍ.

<b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}cowo</code>
<b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴄᴏᴡᴏᴋ ʀᴀɴᴅᴏᴍ.

<b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}anime</code>
<b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>  ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴀɴɪᴍᴇ ʀᴀɴᴅᴏᴍ.
"""

@PY.UBOT("asupan")
async def _(client, message):
    await video_asupan(client, message)


@PY.UBOT("cewe")
async def _(client, message):
    await photo_cewek(client, message)


@PY.UBOT("cowo")
async def _(client, message):
    await photo_cowok(client, message)


@PY.UBOT("anime")
async def _(client, message):
    await photo_anime(client, message)


@PY.UBOT("bokep")
async def _(client, message):
    await video_bokep(client, message)
