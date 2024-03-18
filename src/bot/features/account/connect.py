from interactions import Extension
from interactions import slash_command, SlashContext

from ._lang import account_name, account_desc, account_connect_name, account_connect_desc


class Connect(Extension):
    @slash_command(
        name=account_name,
        description=account_desc,
        sub_cmd_name=account_connect_name,
        sub_cmd_description=account_connect_desc
    )
    async def account_cmd(self, ctx: SlashContext):
        await ctx.send(NotImplementedError.__name__)
