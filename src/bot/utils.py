from pydantic.dataclasses import dataclass
from dataclasses import asdict
from typing import Optional, List


@dataclass
class BotConfig:
    '''dataclass for storing bot config data'''
    auth_channel_id: int
    bot_token: str
    client_secret: str
    support_server_id: int


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
