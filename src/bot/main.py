from interactions import Client, Intents, Status, Activity
from discordoauth2 import Client as AuthClient

from json import load
from utils import BotConfig


# setup bot client
bot = Client(
    delete_unused_application_cmds=True,  # todo: not ok for prod
    disable_dm_commands=True,
    intents=Intents.DEFAULT | Intents.GUILD_MEMBERS,
    send_command_tracebacks=True,  # todo: not ok for prod
    send_not_ready_messages=True,
    status=Status.ONLINE,
    activity=Activity(
        name="v0.0.0",
        state="by @EchterTimo"
    )
)

# load the config file
with open("src/bot/config.json", 'r', encoding="utf-8") as file:
    config_data: dict = load(file)

# save BotConfig instance in bot class
bot.config = BotConfig(**config_data)

# save AuthClient instance in bot class
bot.auth = AuthClient(
    id=bot.config.client_id,
    secret=bot.config.client_secret,
    redirect=None,
    bot_token=None
)

# define extensions to load
extensions = [
    'features.account.auth_received',
    'features.account.connect_cmd',
    'features.account.connect_component'
]


def main():
    for ext in extensions:
        bot.load_extension(ext)
    print(f"loaded {len(extensions)} extensions")
    bot.start(bot.config.bot_token)


if __name__ == '__main__':
    main()
