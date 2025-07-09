from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1392514465240580195/KYzEZHcGEwSmJyLlxuP9STfaKh2yVUmM4OCzBMamn2-RQZ2rYQgIO69IbDUopA7nb1UG",
    username="Калл"
)

# Пример URL картинок
image_url1 = "https://example.com/image1.jpg"
image_url2 = "https://example.com/image2.jpg"

# Встраиваем изображения как embed
embed1 = DiscordEmbed(title="Картинка 1", color="03b2f8")
embed1.set_image(url=image_url1)

embed2 = DiscordEmbed(title="Картинка 2", color="03b2f8")
embed2.set_image(url=image_url2)

# Добавляем embeds в webhook
webhook.add_embed(embed1)
webhook.add_embed(embed2)

# Отправляем
response = webhook.execute()
