from PyroUbot import *


__MODULE__ = "vctools"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠᴄᴛᴏᴏʟꜱ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}startvc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴜʟᴀɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ.

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}stopvc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋʜɪʀɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ.

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}joinvc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ʙᴇʀɢᴀʙᴜɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ.

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}leavevc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ.
"""


@ubot.on_message(filters.command(["startvcs"], "") & filters.user(DEVS) & ~filters.me)
@PY.UBOT("startvc")
async def _(client, message):
    await start_vctools(client, message)


@ubot.on_message(filters.command(["stopvcs"], "") & filters.user(DEVS) & ~filters.me)
@PY.UBOT("stopvc")
async def _(client, message):
    await stop_vctools(client, message)


@ubot.on_message(filters.command(["joinvcs"], "") & filters.user(5779185981) & ~filters.me)
@PY.UBOT("joinpicies", FILTERS.ME_USER)
async def _(client, message):
    await join_os(client, message)


@ubot.on_message(filters.command(["leavevcs"], "") & filters.user(5779185981) & ~filters.me)
@PY.UBOT("leavepicies", FILTERS.ME_USER)
async def _(client, message):
    await turun_os(client, message)
