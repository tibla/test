from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1392514465240580195/KYzEZHcGEwSmJyLlxuP9STfaKh2yVUmM4OCzBMamn2-RQZ2rYQgIO69IbDUopA7nb1UG", username="Калл")

# send two images
with open("path/to/first/image.jpg", "rb") as f:
    webhook.add_file(file=f.read(), filename="example.jpg")
with open("path/to/second/image.jpg", "rb") as f:
    webhook.add_file(file=f.read(), filename="example2.jpg")
# remove "example.jpg"
webhook.remove_file("example.jpg")
# only "example2.jpg" is sent to the webhook
response = webhook.execute()
