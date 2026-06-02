import os
import logging
import telebot

# Bot tokeni bu yerda ko'rinmaydi, server muhitidan yashirincha olinadi
BOT_TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        response_text = (
            "✅ <b>Kino topildi!</b>\n\n"
            "🎬 Yangi premyera kinosi havolasi:\n"
            "https://t.me\n\n"
            "🍿 Yoqimli tomosha tilaymiz!"
        )
        bot.send_message(message.chat.id, response_text, parse_mode="HTML")
    except Exception as e:
        logging.error(f"Xatolik: {e}")

if __name__ == "__main__":
    logging.info("Bot ishga tushdi...")
    try:
        bot.infinity_polling(skip_pending_updates=True)
    except Exception as main_error:
        logging.critical(f"Jiddiy xato: {main_error}")
      
