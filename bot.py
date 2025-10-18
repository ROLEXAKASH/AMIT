from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace this token with your actual bot token
TOKEN = "8461214559:AAHIP-n0wmnZOatJ-rggb7fU5cfv2uvl8Lc"

# Define the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello 🤗👋👋")

# Run the bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()