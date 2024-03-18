from interactions import LocalisedName, LocalisedDesc


# ----------
# localization for commands

# /account
account_name = LocalisedName(
    english_us="account",
    # german=""
)

account_desc = LocalisedDesc(
    english_us="Manage your Riot Games account",
    german="Verwalte deinen Riot Games Account"
)

# /account connect
account_connect_name = LocalisedName(
    english_us="connect",
    german="verbinden"
)

account_connect_desc = LocalisedDesc(
    english_us="Connect your Riot Games account",
    german="Verbinde deinen Riot Games Account"
)

# /account disconnect
account_disconnect_name = LocalisedName(
    english_us="disconnect",
    german="trennen"
)

account_disconnect_desc = LocalisedDesc(
    english_us="Disconnect your Riot Games account",
    german="Trenne deinen Riot Games Account"
)

# /account privacy
# todo

# /account privacy set-visibility
# todo

# /account privacy request-data
# todo

# ----------
# localization for other stuff

auth_received_connect_account = {
    "en-GB": account_connect_desc.english_us,
    "de": account_connect_desc.german,
}

auth_received_choose_account = {
    "en-GB": "Choose Account",
    "de": "Wähle Account aus"
}
