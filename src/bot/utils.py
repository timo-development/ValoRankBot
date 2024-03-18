from pydantic.dataclasses import dataclass


@dataclass
class BotConfig:
    token: str
    auth_channel_id: int
