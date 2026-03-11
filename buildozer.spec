[app]
# Имя приложения
title = Telegram Proxy

# Уникальный идентификатор
package.name = telegramproxy
package.domain = org.example

# Исходный файл
source.dir = .
source.include_exts = py,png,jpg,kv,atxt,txt

# Версия
version = 1.0

# Требования
requirements = python3,kivy

# Ориентация экрана
orientation = portrait

# Разрешения
android.permissions = INTERNET

# Настройки Android (исправлено)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

# Отладка
android.debug = True
android.logcat_filters = *:S python:D

# Графика
android.wakelock = True

[buildozer]
log_level = 2
warn_on_root = 1
