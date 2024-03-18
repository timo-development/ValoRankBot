from interactions import Extension

from interactions import listen
from interactions.api.events import Component

from valo_api import v1_account, Account, Error


class ConnectComponent(Extension):
    @listen(Component)
    async def on_component(self, event: Component):
        if not event.ctx.custom_id.startswith("connect_account"):
            return False

        account_name = event.ctx.values[0]
        name, tag = account_name.split("#")

        user = event.ctx.author
        # communicate with api
        account = v1_account(name, tag)
        if isinstance(account, Error):
            # when account can not be fetched
            await user.send(f"Error: {str(account)}")
            return

        # when account can be fetched
        await event.ctx.message.delete()
        await user.send(f"Connected with `{account.name}#{account.tag}`")
