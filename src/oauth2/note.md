# My Solution for OAuth2

In order to fetch the `User` and `Connections` objects from [Discord OAuth2](https://discord.com/developers/docs/topics/oauth2), you would normally need your own web server.

To save money and make it easier, I'm using an [Event Gateway](https://hookdeck.com/blog/introducing-the-event-gateway#introducing-the-event-gateway) Service called [hookdeck.com](https://hookdeck.com) to redirect auth codes to a private Discord webhook.

The service transforms `GET` requests using an [request_handler.js](./request_handler.js) to discord friendly `POST` requests.

The bot receives a [MessageCreate](https://interactions-py.github.io/interactions.py/API%20Reference/API%20Reference/events/discord/#interactions.api.events.discord.MessageCreate) event and utilizes the provided code to access the user's data. After retrieving the necessary information, the code is revoked to ensure it cannot be used again.

## Read before replicating

If you want to replicate my solution you need to keep the following things in mind.

- Make sure that the Discord Webhook can only be used by yourself and the bot to maintain data privacy.

- Make sure that you handle the rate limit for the webhooks (30 messages per minute) to prevent loosing data or get punished by [Cloudflare](https://www.cloudflare.com/) for [Too Many Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429).
