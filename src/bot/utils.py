from pydantic.dataclasses import dataclass
from dataclasses import asdict
from typing import Optional, List


@dataclass
class BotConfig:
    '''dataclass for storing bot config data'''

    auth_channel_id: int
    '''the channel.id where the bot will reveive AuthEvents'''

    bot_token: str
    '''Discord bot token'''

    client_id: int
    '''the id of the app / bot.user.id'''

    client_secret: str
    '''Discord client secret used for OAuth2'''

    support_server_id: int
    '''the guild.id of the bots support server'''

    valo_api_key: Optional[str]
    '''Optional: api key for https://github.com/Henrik-3/unofficial-valorant-api'''


@dataclass
class AuthEvent:
    '''dataclass for OAuth2 events'''
    code: str
    state: str
    time: int


@dataclass
class UserData:
    '''dataclass for OAuth2 response: user_data'''
    accent_color: Optional[int]
    avatar_decoration_data: Optional[dict]
    avatar: str
    banner_color: Optional[str]
    banner: Optional[str]
    discriminator: str
    flags: int
    global_name: str
    id: int
    locale: str
    mfa_enabled: bool
    premium_type: int
    public_flags: int
    username: str

    def to_dict(self):
        return asdict(self)


@dataclass
class Connection:
    '''dataclass for OAuth2 response: user_connection'''
    friend_sync: bool
    id: str
    metadata_visibility: int
    name: str
    show_activity: bool
    two_way_link: bool
    type: str
    verified: bool
    visibility: int

    def to_dict(self):
        return asdict(self)
