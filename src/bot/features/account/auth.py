from interactions import Extension
from interactions import listen
from interactions.api.events import MessageCreate

from discordoauth2 import Client as AuthClient, exceptions

from json import loads, JSONDecodeError

from utils import BotConfig, AuthEvent, UserData, Connection


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

        # add reaction 'eye'
        await event.message.add_reaction(":eye:")

        # remove the mention from the message
        content = event.message.content.replace(
            event.bot.user.mention,
            ""
        )

        # load the json data into an object
        try:
            auth_event = AuthEvent(**loads(content))
        except JSONDecodeError as e:
            return

        # get AuthClient instance
        auth_client: AuthClient = event.bot.auth

        try:
            # exchange code with discord api using the code
            access = auth_client.exchange_code(auth_event.code)

            # get user data
            user_data = UserData(**access.fetch_identify())

            # get users connections
            connections_data = access.fetch_connections()
            connections = [Connection(**data) for data in connections_data]

            riot_connections = [
                conn for conn in connections if conn.type == "riotgames"
            ]

            access.revoke()
        except exceptions.HTTPException:
            return

        # add reaction 'white_check_mark'
        await event.message.add_reaction(":white_check_mark:")

        # check if state is equal to user id
        if user_data.id != int(auth_event.state):
            return

        # use the data to authorize the user
        user = event.message.bot.get_user(user_data.id)
        temp_content = [
            "We found the following riotgames accounts on your discord account:"
        ]
        for riot_acc in riot_connections:
            temp_content.append(riot_acc.name)
        await user.send('\n'.join(temp_content))

        # add reaction 'speech_balloon'
        await event.message.add_reaction(":speech_balloon:")
