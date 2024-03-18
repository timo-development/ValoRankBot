from interactions import Extension
from interactions import listen
from interactions.api.events import MessageCreate

from discordoauth2 import Client, exceptions

from json import loads, JSONDecodeError

from utils import BotConfig, AuthEvent


class Auth(Extension):
    @listen(MessageCreate)
    async def an_event_handler(self, event: MessageCreate):
        config: BotConfig = event.bot.config

        # return when not auth channel
        if event.message.channel.id != config.auth_channel_id:
            return

        # return when content will be none
        if not event.bot.user.id in event.message._mention_ids:
            return

        # remove the mention from the message
        content = event.message.content.replace(
            event.bot.user.mention,
            ""
        )

        # load the json data into an object
        try:
            auth_data = AuthEvent(**loads(content))
        except JSONDecodeError as e:
            return

        # create auth_client instance
        auth_client = Client(
            id=event.bot.id,
            secret=config.client_secret,
            redirect=None,
            bot_token=None
        )

        #
