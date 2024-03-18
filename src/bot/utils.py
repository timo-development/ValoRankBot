from pydantic.dataclasses import dataclass


@dataclass
class BotConfig:
    auth_channel_id: int
    bot_token: str
    client_secret: str
    support_server_id: int


@dataclass
class AuthData:
    code: str
    state: str
    time: int
