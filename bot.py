from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
from threading import Thread

TOKEN = "8461214559:AAHIP-n0wmnZOatJ-rggb7fU5cfv2uvl8Lc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello 🤗👋👋")

# Telegram bot
app_bot = ApplicationBuilder().token(TOKEN).build()
app_bot.add_handler(CommandHandler("start", start))

# Tiny Flask server to satisfy Render port
flask_app = Flask("")

@flask_app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    flask_app.run(host="0.0.0.0", port=10000)  # Render will detect this port

Thread(target=run_flask).start()
app_bot.run_polling()