from pydantic.dataclasses import dataclass


@dataclass
class BotConfig:
    token: str
