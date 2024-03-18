from interactions import Extension
from interactions import slash_command, SlashContext

from ._lang import account_name, account_desc, account_disconnect_name, account_disconnect_desc


class Disconnect(Extension):
    @slash_command(
        name=account_name,
        description=account_desc,
        sub_cmd_name=account_disconnect_name,
        sub_cmd_description=account_disconnect_desc
    )
    async def account_cmd(self, ctx: SlashContext):
        await ctx.send(NotImplementedError.__name__)
