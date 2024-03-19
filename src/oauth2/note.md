# OAuth2

[OAuth2](https://discord.com/developers/docs/topics/oauth2) enables application developers to build applications that utilize authentication and data from the Discord API.

## General Solution

In order to receive a [Discord OAuth2 code](https://discord.com/developers/docs/topics/oauth2#authorization-code-grant), you would normally need your own web server.

You can make your own api using this [Tutorial](https://github.com/treeben77/discord-oauth2.py/blob/main/README.md#example-with-flask).

## My Solution

In order to receive a [Discord OAuth2 code](https://discord.com/developers/docs/topics/oauth2#authorization-code-grant), you would normally need your own web server like [Flask](https://github.com/pallets/flask) to receive the codes.

To make it easier, I'm using an Event Gateway Service called [Hookdeck.com](https://hookdeck.com/) to redirect OAuth2 codes to a private [Discord Webhook](https://discord.com/developers/docs/resources/webhook).

Using an [request handler](./request_handler.js) you can modify the transformation of the data in a discord friendly format.

The bot receives a [MessageCreate](https://interactions-py.github.io/interactions.py/API%20Reference/API%20Reference/events/discord/#interactions.api.events.discord.MessageCreate) event and utilizes the provided code to access the user's data.

After retrieving the necessary information, the OAuth2 code is revoked to ensure it cannot be used again.

### Read before replicating

If you want to replicate my solution you need to keep the following things in mind.

- Make sure that the channel of the Discord Webhook can only be accessed by yourself and the bot to maintain data privacy.

- Make sure that you handle the rate limit for the Discord Webhook (30 messages per minute) to prevent loosing code data or get punished by [Cloudflare](https://www.cloudflare.com/) for [Too Many Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429).

To make it easier, I'm using an Event Gateway Service called [Hookdeck.com](https://hookdeck.com/) to redirect OAuth2 codes to a private [Discord Webhook](https://discord.com/developers/docs/resources/webhook).

Using an [request handler](./request_handler.js) you can modify the transformation of the data in a discord friendly format.

The bot receives a [MessageCreate](https://interactions-py.github.io/interactions.py/API%20Reference/API%20Reference/events/discord/#interactions.api.events.discord.MessageCreate) event and utilizes the provided code to access the user's data.

After retrieving the necessary information, the OAuth2 code is revoked to ensure it cannot be used again.

## Read before replicating

If you want to replicate my solution you need to keep the following things in mind.

- Make sure that the channel of the Discord Webhook can only be accessed by yourself and the bot to maintain data privacy.

- Make sure that you handle the rate limit for the Discord Webhook (30 messages per minute) to prevent loosing code data or get punished by [Cloudflare](https://www.cloudflare.com/) for [Too Many Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429).
