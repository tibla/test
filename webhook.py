from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1392435872833601627/z0ErCKfbI4ncH8HfOq-QJi6yYeLqcq8cj6RQlKgrP1rZoJmIuQahLwsVUUOCOwa-aDzn", content="Молодой попался)))")
response = webhook.execute()