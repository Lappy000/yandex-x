"""
Telegram bot for Yandex Music track information extraction.
"""

import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)
from yandex_parser import YandexMusicParser


# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize parser
parser = YandexMusicParser()


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /start command.
    
    Args:
        update: Telegram update object
        context: Callback context
    """
    welcome_message = (
        "👋 Привет! Я бот для извлечения информации о треках из Яндекс.Музыки.\n\n"
        "📝 Просто отправьте мне ссылку на трек в формате:\n"
        "https://music.yandex.ru/album/XXXXX/track/XXXXX\n\n"
        "🎵 Я верну вам:\n"
        "• Название трека\n"
        "• Исполнителя\n"
        "• Длительность\n\n"
        "Попробуйте прямо сейчас!"
    )
    await update.message.reply_text(welcome_message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /help command.
    
    Args:
        update: Telegram update object
        context: Callback context
    """
    help_message = (
        "🔍 Как использовать бота:\n\n"
        "1. Найдите трек на Яндекс.Музыке\n"
        "2. Скопируйте ссылку на трек\n"
        "3. Отправьте её мне\n\n"
        "Пример ссылки:\n"
        "https://music.yandex.ru/album/12345/track/67890\n\n"
        "Команды:\n"
        "/start - Начать работу с ботом\n"
        "/help - Показать это сообщение"
    )
    await update.message.reply_text(help_message)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle text messages containing Yandex Music links.
    
    Args:
        update: Telegram update object
        context: Callback context
    """
    message_text = update.message.text.strip()
    
    # Check if the message contains a Yandex Music link
    if not parser.validate_url(message_text):
        error_message = (
            "❌ Неверный формат ссылки!\n\n"
            "Пожалуйста, отправьте ссылку в формате:\n"
            "https://music.yandex.ru/album/XXXXX/track/XXXXX\n\n"
            "Используйте /help для получения справки."
        )
        await update.message.reply_text(error_message)
        return
    
    # Send "processing" message
    processing_msg = await update.message.reply_text("🔄 Обрабатываю ссылку...")
    
    # Parse the track information
    track_info = parser.parse_track(message_text)
    
    if track_info is None:
        error_message = (
            "❌ Не удалось извлечь информацию о треке.\n\n"
            "Возможные причины:\n"
            "• Неверная ссылка\n"
            "• Трек недоступен\n"
            "• Проблемы с подключением\n\n"
            "Попробуйте другую ссылку или попробуйте позже."
        )
        await processing_msg.edit_text(error_message)
        return
    
    # Format and send the track information
    response = (
        "Информация о треке:\n\n"
        f"Название: {track_info['title']}\n"
        f"Исполнитель: {track_info['artist']}\n"
        f"Длительность: {track_info['duration']}\n\n"
        f"Ссылка: {track_info['url']}"
    )
    
    await processing_msg.edit_text(response)
    logger.info(f"Successfully processed track: {track_info['title']} by {track_info['artist']}")


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle errors in the bot.
    
    Args:
        update: Telegram update object
        context: Callback context
    """
    logger.error(f"Update {update} caused error {context.error}")
    
    if update and update.message:
        error_message = (
            "Произошла ошибка при обработке вашего запроса.\n"
            "Пожалуйста, попробуйте позже или отправьте другую ссылку."
        )
        await update.message.reply_text(error_message)


def main() -> None:
    """Start the bot."""
    # Get bot token from environment
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not bot_token:
        logger.error("TELEGRAM_BOT_TOKEN not found in environment variables!")
        return
    
    # Create application
    application = Application.builder().token(bot_token).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Add error handler
    application.add_error_handler(error_handler)
    
    # Start the bot
    logger.info("Bot started successfully!")
    print("Bot is running... Press Ctrl+C to stop.")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()