from pyrogram import Client
from pyrogram.handlers.callback_query_handler import CallbackQueryHandler
from pyrogram.handlers.message_handler import MessageHandler
import callback

bot = Client("my_session")

if bot.run:
    print("Bot operativo")
    
if __name__ == "__main__":
    bot.add_handler(CallbackQueryHandler(callback.translator_buttons), 0)
    bot.add_handler(CallbackQueryHandler(callback.default_buttons), 1)
    bot.add_handler(MessageHandler(callback.take_message), 2)
    bot.run()
    
    


