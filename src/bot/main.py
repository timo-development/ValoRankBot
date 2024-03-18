from interactions import Client, Intents, Status, Activity
from json import load
from utils import BotConfig


# setup bot client
bot = Client(
    delete_unused_application_cmds=True,  # todo: not ok for prod
    disable_dm_commands=True,
    intents=Intents.DEFAULT,
    send_command_tracebacks=True,  # todo: not ok for prod
    send_not_ready_messages=True,
    status=Status.ONLINE,
    activity=Activity(
        name="",
        state="by @EchterTimo"
    )
)

# load the config file
with open("src/config.json", 'r', encoding="utf-8") as file:
    config_data: dict = load(file)

# save config data bot class
bot.config = BotConfig(**config_data)

# load extensions
extensions = []


def main():
    for ext in extensions:
        bot.load_extension(ext)
    print(f"loaded {len(extensions)} extensions")
    bot.start(bot.config.token)
