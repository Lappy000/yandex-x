# Yandex Music Track Info Bot 🎵

Telegram bot for extracting track information from Yandex Music links.

## 🤖 Bot Link

**[Try the bot now: @YandexMusic_test3_bot](https://t.me/test_music1_bot)**

**Bot Username:** @YandexMusic_test3_bot
**Direct Link:** https://t.me/YandexMusic_test3_bot

## 📋 Description

This bot allows you to quickly extract information about tracks from Yandex Music. Simply send a track link and get:
- Track title (название трека)
- Artist name (имя исполнителя)
- Duration (длительность)

## ✨ Features

- ✅ Simple and intuitive interface
- ✅ Fast track information extraction
- ✅ URL validation
- ✅ Error handling with helpful messages
- ✅ Support for Russian and English Yandex Music links
- ✅ Web scraping approach (no API required)

## 🚀 Quick Start for Users

**No installation needed!** Just open the bot and start using it:

1. Click here: **https://t.me/YandexMusic_test3_bot**
2. Press **Start**
3. Send any Yandex Music track link
4. Get instant track information!

## 🚀 Setup Instructions (For Developers)

Want to run your own instance of the bot? Follow these steps:

### Prerequisites

- **Python 3.8 or higher** ([Download](https://www.python.org/downloads/))
- **pip** (Python package manager, included with Python)
- **Telegram Bot Token** (get it from [@BotFather](https://t.me/BotFather))

### Step-by-Step Installation

#### 1. Clone or Download the Project

```bash
# Navigate to the project directory
cd yandex-music-bot
```

#### 2. Install Required Dependencies

```bash
# Install all required Python packages
pip install -r requirements.txt
```

**Required packages:**
- `python-telegram-bot==20.7` - Telegram Bot API wrapper
- `requests==2.31.0` - HTTP library
- `beautifulsoup4==4.12.2` - HTML parsing
- `python-dotenv==1.0.0` - Environment variables
- `lxml==4.9.3` - XML/HTML parser

#### 3. Get Your Bot Token

1. Open Telegram and find [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the bot token (looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

#### 4. Configure Environment Variables

**Option A: Using the provided example file**
```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

**Option B: Create .env manually**
Create a new file named `.env` in the project root directory.

**Edit the `.env` file and add your bot token:**
```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

**Example:**
```env
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

⚠️ **Important:** Never share your bot token publicly!

#### 5. Run the Bot

**Method 1: Using Python directly**
```bash
python bot.py
```

**Method 2: Using the start script (Windows only)**
```bash
start.bat
```

**Success message:**
```
2026-02-04 13:30:00,000 - __main__ - INFO - Bot started successfully!
🤖 Bot is running... Press Ctrl+C to stop.
```

#### 6. Test Your Bot

1. Open Telegram and find your bot (use the username you created with BotFather)
2. Send `/start` command
3. Send a Yandex Music track link
4. Verify you receive track information

### Stopping the Bot

Press `Ctrl+C` in the terminal where the bot is running.

## 📖 Usage Examples

### Starting the Bot

1. Open the bot: **https://t.me/YandexMusic_test3_bot**
2. Click **"Start"** or send `/start` command
3. You'll receive a welcome message with instructions in Russian

### Extracting Track Information

**Step-by-step guide:**

1. Go to [Yandex Music](https://music.yandex.ru)
2. Find a track you want information about
3. Copy the track URL (format: `https://music.yandex.ru/album/XXXXX/track/XXXXX`)
4. Open [@YandexMusic_test3_bot](https://t.me/YandexMusic_test3_bot)
5. Paste and send the URL to the bot
6. Wait a moment while the bot processes your request
7. Receive formatted track information including:
   - Track title (название)
   - Artist name (исполнитель)
   - Duration (длительность)

### Example Workflow

**You send:**
```
https://music.yandex.ru/album/123456/track/789012
```

**Bot replies:**
```
🎵 Информация о треке:

Название: [Track Name]
Исполнитель: [Artist Name]
Длительность: 3:45

Ссылка: https://music.yandex.ru/album/123456/track/789012
```

### Supported Link Formats

✅ **Valid formats:**
```
https://music.yandex.ru/album/123456/track/789012
https://music.yandex.com/album/654321/track/987654
http://music.yandex.ru/album/111111/track/222222
```

❌ **Invalid formats:**
```
https://music.yandex.ru/album/123456           (missing track ID)
https://music.yandex.ru/track/789012           (missing album ID)
https://yandex.ru/music/album/123/track/456    (wrong domain)
```

## 🤖 Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot and see welcome message |
| `/help` | Get usage instructions |

## 📁 Project Structure

```
yandex-music-bot/
│
├── bot.py              # Main bot logic
├── yandex_parser.py    # Yandex Music parser
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not in git)
├── .env.example       # Example environment file
└── README.md          # This file
```

## 🔧 Technical Details

### Dependencies

- **python-telegram-bot** (v20.7) - Telegram Bot API wrapper
- **requests** (v2.31.0) - HTTP library for web scraping
- **beautifulsoup4** (v4.12.2) - HTML parsing
- **python-dotenv** (v1.0.0) - Environment variable management
- **lxml** (v4.9.3) - XML/HTML parser

### How It Works

1. User sends a Yandex Music track URL
2. Bot validates the URL format
3. Parser fetches the page using requests
4. BeautifulSoup extracts track information from HTML
5. Bot formats and returns the information to user

### Error Handling

The bot handles various error scenarios:
- Invalid URL format
- Network errors
- Parsing errors
- Missing track information
- Unexpected exceptions

## 🛠️ Development

### Running in Development Mode

```bash
python bot.py
```

### Testing the Parser

You can test the parser independently:

```python
from yandex_parser import YandexMusicParser

parser = YandexMusicParser()
url = "https://music.yandex.ru/album/123456/track/789012"

if parser.validate_url(url):
    info = parser.parse_track(url)
    print(info)
```

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. Bot doesn't respond to messages

**Possible causes:**
- Bot token is incorrect or expired
- Bot is not running
- Network connection issues
- Telegram API is temporarily unavailable

**Solutions:**
```bash
# Check if bot token is set correctly in .env file
cat .env  # Linux/Mac
type .env  # Windows

# Verify all dependencies are installed
pip install -r requirements.txt

# Restart the bot
python bot.py
```

#### 2. "Invalid URL format" error

**Problem:** Bot rejects your Yandex Music link

**Solution:** Make sure your link matches the format:
```
https://music.yandex.ru/album/[ALBUM_ID]/track/[TRACK_ID]
```

**Example of correct link:**
```
https://music.yandex.ru/album/123456/track/789012
```

#### 3. Parsing errors / "Failed to extract track info"

**Possible causes:**
- Track is region-restricted or unavailable
- Yandex Music updated their page structure
- Network timeout or connection issues
- Track link is broken

**Solutions:**
- Try opening the link in a web browser first
- Use a different track URL
- Check your internet connection
- Wait a few minutes and try again

#### 4. Module not found errors

**Error message:**
```
ModuleNotFoundError: No module named 'telegram'
```

**Solution:**
```bash
# Install all required dependencies
pip install -r requirements.txt

# Or install individually:
pip install python-telegram-bot==20.7
pip install requests beautifulsoup4 python-dotenv lxml
```

#### 5. Bot stops after some time

**Possible causes:**
- Network disconnection
- System sleep/hibernation
- Server/computer restart

**Solutions:**
- Keep the terminal window open
- Use a process manager (e.g., `screen`, `tmux` on Linux)
- Deploy to a cloud server for 24/7 availability

### Debug Mode

To see detailed logs, the bot already runs with `INFO` level logging. Check the console output for detailed error messages.


**🔗 Bot Link:** https://t.me/YandexMusic_test3_bot  
**👤 Username:** @YandexMusic_test3_bot

