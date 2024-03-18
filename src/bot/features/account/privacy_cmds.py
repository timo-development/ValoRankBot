from interactions import Extension
from interactions import slash_command, SlashContext

from ._lang import account_name, account_desc


class PrivacyCmds(Extension):
    @slash_command(
        name=account_name,
        description=account_desc,
        group_name="privacy",
        group_description="Manage your privacy settings",
        sub_cmd_name="request-data",
        sub_cmd_description="Request your data",
    )
    async def request_data(self, ctx: SlashContext):
        await ctx.send(NotImplementedError.__name__)

    @slash_command(
        name=account_name,
        description=account_desc,
        group_name="privacy",
        group_description="Manage your privacy settings",
        sub_cmd_name="set-visibility",
        sub_cmd_description="Set the account visibility",
    )
    async def visibility(self, ctx: SlashContext):
        await ctx.send(NotImplementedError.__name__)
