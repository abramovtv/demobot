# Telegram AI Bot

Этот бот использует библиотеку **Telethon** для работы с Telegram и **OpenAI API** для генерации ответов. Он отвечает на вопросы об автомобилях, используя OpenAI GPT-4o-mini.

## 🚀 Как запустить бота

Инструкция для пользователей **Windows** и **MacOS** без установки Git.

---

## 1️⃣ Скачивание кода с GitHub

1. Перейдите в репозиторий на GitHub.
2. Нажмите на **Code** → **Download ZIP**.
3. Разархивируйте скачанный архив в удобное место на вашем компьютере.

---

## 2️⃣ Установка Python и библиотек

### **Windows**:
1. Скачайте Python с официального сайта: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/).
2. Установите Python, не забыв поставить галочку **Add Python to PATH**.
3. Откройте **Командную строку (cmd)** и проверьте установку:
   ```sh
   python --version
   ```
4. Установите необходимые библиотеки:
   ```sh
   pip install telethon openai asyncio
   ```

### **MacOS**:
1. Откройте **Терминал**.
2. Установите Python через **Homebrew** (если он не установлен):
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   brew install python
   ```
3. Проверьте установку:
   ```sh
   python3 --version
   ```
4. Установите библиотеки:
   ```sh
   pip3 install telethon openai asyncio
   ```

---

## 3️⃣ Получение API-ключей

### **Telegram API**:
1. Перейдите на [https://my.telegram.org/](https://my.telegram.org/) и войдите в аккаунт.
2. Нажмите **API development tools**.
3. Создайте приложение и получите **API ID** и **API HASH**.

### **Telegram Bot Token**:
1. Откройте Telegram и найдите бота **@BotFather**.
2. Напишите команду `/newbot` и следуйте инструкциям.
3. Скопируйте полученный **токен бота**.

### **OpenAI API Key**:
1. Перейдите на [https://platform.openai.com/signup/](https://platform.openai.com/signup/) и создайте аккаунт.
2. В разделе API получите **API Key**.

---

## 4️⃣ Настройка бота

1. Откройте файл **bot.py** в любом текстовом редакторе.
2. Замените заглушки своими данными:
   ```python
   tg_client = TelegramClient("bot", int("ВАШ_TG_API_ID"), "ВАШ_TG_API_HASH")
   openai_client = openai.AsyncOpenAI(api_key="ВАШ_OPENAI_API_KEY")
   ```
   ```python
   await tg_client.start(bot_token="ВАШ_TG_BOT_TOKEN")
   ```
3. Сохраните файл.

---

## 5️⃣ Запуск бота

### **Windows**:
1. Откройте папку с ботом.
2. В адресной строке проводника напишите `cmd` и нажмите **Enter**.
3. Запустите бота командой:
   ```sh
   python bot.py
   ```

### **MacOS**:
1. Откройте **Терминал**.
2. Перейдите в папку с ботом:
   ```sh
   cd /путь/к/папке
   ```
3. Запустите бота:
   ```sh
   python3 bot.py
   ```

---

## 6️⃣ Добавление бота в Telegram-группу
1. Найдите своего бота по его имени в Telegram.
2. Добавьте его в группу через настройки группы.
3. Дайте боту **права администратора**.

---

## 7️⃣ Проверка работы бота
Отправьте в группу вопрос про автомобили. Если бот отвечает – он работает корректно! 🚗✅

---

🎉 **Поздравляем! Теперь ваш Telegram-бот запущен и работает!**
