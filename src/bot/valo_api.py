from enum import Enum
from pydantic.dataclasses import dataclass
from dataclasses import asdict

from datetime import datetime

import requests


class Affinity(Enum):
    AP = "ap"
    BR = "br"
    EU = "eu"
    KR = "kr"
    LATAM = "latam"
    NA = "na"

    def __str__(self):
        return self.name


@dataclass
class Error:
    message: str
    code: int
    details: str

    def to_dict(self):
        return asdict(self)


@dataclass
class Account_Card:
    small: str
    large: str
    wide: str
    id: str


@dataclass
class Account:
    puuid: str
    region: str
    account_level: int
    name: str
    tag: str
    card: Account_Card
    last_update: str
    last_update_raw: int

    @classmethod
    def from_dict(
        cls,
        puuid: str,
        region: str,
        account_level: int,
        name: str,
        tag: str,
        card: dict,
        last_update: str,
        last_update_raw: int,
    ):
        return Account(
            puuid=puuid,
            region=region,
            account_level=account_level,
            name=name,
            tag=tag,
            card=Account_Card(
                small=card.get("small"),
                large=card.get("large"),
                wide=card.get("wide"),
                id=card.get("id")
            ),
            last_update=last_update,
            last_update_raw=last_update_raw
        )

    def v1_by_puuid_mmr(self):
        return v1_by_puuid_mmr(self.region, self.puuid)


@dataclass
class AccountMMR_Images:
    small: str
    large: str
    triangle_down: str
    triangle_up: str


@dataclass
class AccountMMR:
    currenttier: int
    currenttierpatched: str
    images: AccountMMR_Images
    ranking_in_tier: int
    mmr_change_to_last_game: int
    elo: int
    name: str
    tag: str
    old: bool

    @classmethod
    def from_dict(
        cls,
        currenttier: int,
        currenttierpatched: str,
        images: dict,
        ranking_in_tier: int,
        mmr_change_to_last_game: int,
        elo: int,
        name: str,
        tag: str,
        old: bool,
    ):
        return AccountMMR(
            currenttier=currenttier,
            currenttierpatched=currenttierpatched,
            images=AccountMMR_Images(
                small=images.get("small"),
                large=images.get("large"),
                triangle_down=images.get("triangle_down"),
                triangle_up=images.get("triangle_up")
            ),
            ranking_in_tier=ranking_in_tier,
            mmr_change_to_last_game=mmr_change_to_last_game,
            elo=elo,
            name=name,
            tag=tag,
            old=old
        )


@dataclass
class Tier:
    id: int
    name: str


@dataclass
class Map:
    id: str
    name: str


@dataclass
class Season:
    id: str
    short: str


@dataclass
class Match:
    match_id: str
    tier: Tier
    map: Map
    season: Season
    ranking_in_tier: int
    last_mmr_change: int
    elo: int
    date: datetime

    @classmethod
    def from_dict(
        cls,
        match_id: str,
        tier: dict,
        map: dict,
        season: dict,
        ranking_in_tier: int,
        last_mmr_change: int,
        elo: int,
        date: str,
    ):
        return Match(
            match_id=match_id,
            tier=Tier(
                id=tier.get("id"),
                name=tier.get("name")
            ),
            map=Map(
                id=map.get("id"),
                name=map.get("name")
            ),
            season=Season(
                season.get("id"),
                season.get("short"),
            ),
            ranking_in_tier=ranking_in_tier,
            last_mmr_change=last_mmr_change,
            elo=elo,
            date=datetime.fromisoformat(date[:-1])
        )


BASE_URL = 'https://api.henrikdev.xyz'


def v1_account(
    name: str,
    tag: str,
    force: bool = False
) -> (Account | Error):
    ENDPOINT = '/valorant/v1/account/{name}/{tag}'
    url = BASE_URL + ENDPOINT.format(
        name=name,
        tag=tag
    )
    params = {
        "force": force
    }
    try:
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            account_data = dict(response.json()).get("data")
            return Account.from_dict(**account_data)
        else:
            error_data = dict(response.json()).get("errors")[0]
            return Error(**error_data)
    except requests.RequestException as e:
        print(e)


def v1_by_puuid_mmr(
    affinity: Affinity | str,
    puuid: str
) -> (AccountMMR | Error):
    ENDPOINT = '/valorant/v1/by-puuid/mmr/{affinity}/{puuid}'
    url = BASE_URL + ENDPOINT.format(
        affinity=str(affinity),
        puuid=puuid
    )
    try:
        response = requests.get(url=url)
        if response.status_code == 200:
            mmr_data = dict(response.json()).get("data")
            return AccountMMR(**mmr_data)
        else:
            error_data = dict(response.json()).get("errors")[0]
            return Error(**error_data)
    except requests.RequestException as e:
        print(e)


def v1_lifetime_mmr_history(
    affinity: Affinity | str,
    name: str,
    tag: str,
    page: int = 1,
    size: int = 15
) -> (list[Match] | Error):
    ENDPOINT = '/valorant/v1/lifetime/mmr-history/{affinity}/{name}/{tag}'
    url = BASE_URL + ENDPOINT.format(
        affinity=str(affinity),
        name=name,
        tag=tag
    )
    params = {
        "page": page,
        "size": size
    }
    try:
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            matches_data = dict(response.json()).get("data")
            matches: list[Match] = []
            for match_data in matches_data:
                match = Match.from_dict(**match_data)
                matches.append(match)
            return matches
        else:
            error_data = dict(response.json()).get("errors")[0]
            return Error(**error_data)
    except requests.RequestException as e:
        print(e)
