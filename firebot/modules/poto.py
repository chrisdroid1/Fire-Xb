import logging

from firebot import CMD_HELP
from firebot.utils import fire_on_cmd, sudo_cmd

logger = logging.getLogger(__name__)


if 1 == 1:

    name = "Profile Photos"

    client = borg

    @fire.on(fire_on_cmd(pattern="poto(.*)"))
    @fire.on(sudo_cmd(pattern="poto(.*)", allow_sudo=True))
    async def potocmd(event):

        """Gets the profile photos of replied users, channels or chats"""
        id = "".join(event.raw_text.split(maxsplit=2)[1:])

        user = await event.get_reply_message()

        chat = event.input_chat

        if user:

            photos = await event.client.get_profile_photos(user.sender)

        else:

            photos = await event.client.get_profile_photos(chat)

        if id.strip() == "":

            try:

                await event.client.send_file(event.chat_id, photos)

            except a:

                photo = await event.client.download_profile_photo(chat)

                await borg.send_file(event.chat_id, photo)

        else:

            try:

                id = int(id)

                if id <= 0:

                    await event.edit("`ID number you entered is invalid`")

                    return

            except:

                await event.edit("`Are you Comedy Me ?`")

                return

            if int(id) <= (len(photos)):

                send_photos = await event.client.download_media(photos[id - 1])

                await borg.send_file(event.chat_id, send_photos)

            else:

                await event.edit("`මූ ලග පොටෝ එකක් නෑ 😅 `")

                return


CMD_HELP.update(
    {
        "poto": "**Poto**\
\n\n**Syntax : **`.poto <reply to a user> <profile picture number>`\
\n**Usage :** Downloads profile picture of replyed user."
    }
)
