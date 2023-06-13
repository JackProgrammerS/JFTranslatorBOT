import utils
import deepl
import mysql.connector
from database import *
import time

# data center
translator= deepl.Translator("73b6378e-53d0-2cd2-bac6-3b932df5842f:fx")
callback_query_id = {}
text_message = {}


# translator buttons language
async def translator_buttons(client, CallbackQuery):
    if CallbackQuery.data == "ita":
        callback_query_id["lang"] = "IT"
    elif CallbackQuery.data == "eng":
        callback_query_id["lang"] = "EN"
    elif CallbackQuery.data == "de":
        callback_query_id["lang"] = "DE"
    elif CallbackQuery.data == "esp":
        callback_query_id["lang"] = "ES"
    elif CallbackQuery.data == "jap":
        callback_query_id["lang"] = "JA"
    elif CallbackQuery.data == "chi":
        callback_query_id["lang"] = "ZH"
        
    if not "def_" in CallbackQuery.data:
        await client.edit_message_text(chat_id=CallbackQuery.from_user.id,
                                       message_id=CallbackQuery.message.id,
                                       text="**Insert a message.**")
    else:
        await client.edit_message_text(chat_id=CallbackQuery.from_user.id,
                                       message_id=CallbackQuery.message.id,
                                       text="**Chosen language.**")

# default buttons language
async def default_buttons(client, CallbackQuery):
    try:
    
        if CallbackQuery.data == "def_ita":
            cursor.execute(insertDefLangDb,(CallbackQuery.from_user.id, "IT"))
            cnx.commit()
        elif CallbackQuery.data == "def_eng":
            cursor.execute(insertDefLangDb,(CallbackQuery.from_user.id, "EN"))
            cnx.commit()
        elif CallbackQuery.data == "def_de":
            cursor.execute(insertDefLangDb,(CallbackQuery.from_user.id, "DE"))
            cnx.commit()
        elif CallbackQuery.data == "def_esp":
            cursor.execute(insertDefLangDb,(CallbackQuery.from_user.id, "ES"))
            cnx.commit()
        elif CallbackQuery.data == "def_jap":
            cursor.execute(insertDefLangDb,(CallbackQuery.from_user.id, "JA"))
            cnx.commit()
        elif CallbackQuery.data == "def_chi":
            cursor.execute(insertDefLangDb,(CallbackQuery.from_user.id, "ZH"))
            cnx.commit()
        
    except mysql.connector.errors.IntegrityError:
        await client.edit_message_text(chat_id= CallbackQuery.from_user.id,
                                       message_id= CallbackQuery.message.id+1,
                                       text=utils.lang_error)
    
# take the user message 
async def take_message(client, message):
    if message.text == "/start":
            await client.delete_messages(chat_id=message.from_user.id,
                                         message_ids=message.id)
            await start_bot(client, message)    
    elif message.text == "/modify":
        await mod_default_lang(client, message)
    else:
        await translate(client, message)
        
        
async def translate(client, message):
    text_message["message_text"] = message.text
    try:
        translation = await translate_text(client, message)
        await client.delete_messages(chat_id=message.from_user.id,
                                    message_ids=message.id-1) 
        await client.send_message(message.from_user.id, 
                                  text=f"**Traduzione: {translation}**")
    except KeyError:
        await message.reply_text("**You have not chosen a language.\n\n__Use '/start'__**")
    
# choose default language
async def default_lang(client, message):
    await client.send_message(message.from_user.id, "Choose the default language:", reply_markup=utils.default_button)        
    
# command '/modify'     
async def mod_default_lang(client, message):
    cursor.execute(query_mod.format(message.from_user.id))
    cnx.commit()
    await default_lang(client=client, message=message)
    
# translator 
async def translate_text(client, message):
    text = text_message["message_text"]
    target_lang= callback_query_id["lang"]
    result = translator.translate_text(text=text, target_lang=target_lang, source_lang= await select_default_lang(client, message))
    result = result.text
    return result
  
# select the default language in DB
async def select_default_lang(client, message):
    cursor.execute(query_tran.format(message.from_user.id))
    result = cursor.fetchone()
    x = result[0]
    return x
    

async def start_bot(client, message):
    cursor.execute(query_regist_log.format(message.from_user.id))
    result = cursor.fetchone()
    
    if result:
        await client.send_message(chat_id= message.from_user.id,
                text= utils.start_text.format(message.from_user.mention, result[0]),
                reply_markup= utils.languages_button)
    elif not result:
        await default_lang(client, message)
        