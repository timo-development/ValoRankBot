from interactions import Extension
from interactions import listen
from interactions.api.events import MessageCreate
from interactions import ActionRow, StringSelectMenu, StringSelectOption
from discordoauth2 import Client as AuthClient, exceptions

from json import loads, JSONDecodeError

from utils import BotConfig, AuthEvent, UserData, Connection


class AuthReceived(Extension):
    @listen(MessageCreate)
    async def on_message_create(self, event: MessageCreate):
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

        # check if state is equal to user id
        if user_data.id != int(auth_event.state):
            return

        # use the data to authorize the user
        if len(riot_connections) == 0:
            # no riot account found
            return
        elif len(riot_connections) > 25:
            # remove accounts when more then 25
            riot_connections = riot_connections[:25]

        options = []
        for riot_acc in riot_connections:
            options.append(
                StringSelectOption(
                    label=riot_acc.name,
                    value=riot_acc.name,
                    description=None,
                    emoji="<:valorant:1219326778645020753>"
                )
            )

        components = [
            ActionRow(
                StringSelectMenu(
                    options,
                    placeholder="Choose Account",
                    custom_id="connect_account"
                )
            )
        ]
        user = event.message.bot.get_user(user_data.id)
        await user.send(components=components)

        # add reaction 'white_check_mark'
        await event.message.add_reaction(":white_check_mark:")
