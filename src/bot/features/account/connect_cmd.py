from interactions import Extension
from interactions import slash_command, SlashContext, Embed, ActionRow, Button, ButtonStyle

from ._lang import account_name, account_desc, account_connect_name, account_connect_desc

from discordoauth2 import Client as AuthClient


class ConnectCmd(Extension):
    @slash_command(
        name=account_name,
        description=account_desc,
        sub_cmd_name=account_connect_name,
        sub_cmd_description=account_connect_desc
    )
    async def account_connect(self, ctx: SlashContext):
        auth_client: AuthClient = ctx.bot.auth
        url = auth_client.generate_uri(
            scope=[
                "connections",
                "identify"
            ],
            state=f"{ctx.author.id}"
        )
        components = [
            ActionRow(
                Button(
                    style=ButtonStyle.URL,
                    label="Connect Riot Games account",
                    url=url,
                )
            )
        ]
        await ctx.send(
            components=components,
            ephemeral=True
        )
