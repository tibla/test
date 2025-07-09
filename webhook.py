from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1392514465240580195/KYzEZHcGEwSmJyLlxuP9STfaKh2yVUmM4OCzBMamn2-RQZ2rYQgIO69IbDUopA7nb1UG", content="Тестовое Сообщение.")
response = webhook.execute()
