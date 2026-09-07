import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات با موفقیت روشن شد ✅")


TOKEN = os.getenv("8567898616:AAG0ipyl6Vq2Y3n6Imxb_wh9cUGipT0Iaxk")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
