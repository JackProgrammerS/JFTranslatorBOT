from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import callback

default_button = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton(text="IT 🇮🇹", callback_data="def_ita"),
        InlineKeyboardButton(text="EN 🇬🇧", callback_data="def_eng"),
        InlineKeyboardButton(text="DE 🇩🇪", callback_data="def_de"),

    ],[
        InlineKeyboardButton(text="ES 🇪🇸", callback_data="def_esp"),
        InlineKeyboardButton(text="JA 🇯🇵", callback_data="def_jap"),
        InlineKeyboardButton(text="ZH 🇨🇳", callback_data="def_chi"),
    ]]
    
)

languages_button = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton(text="IT 🇮🇹", callback_data="ita"),
        InlineKeyboardButton(text="EN 🇬🇧", callback_data="eng"),
        InlineKeyboardButton(text="DE 🇩🇪", callback_data="de"),

    ],[
        InlineKeyboardButton(text="ES 🇪🇸", callback_data="esp"),
        InlineKeyboardButton(text="JA 🇯🇵", callback_data="jap"),
        InlineKeyboardButton(text="ZH 🇨🇳", callback_data="chi"),
    ]]
    
)


start_text = """
Hello **{0}**.
__Welcome to **JackForme BOT Translator**.__

**Step:**
**1-** __Choose the translation language by pressing a button.__
**2-** __Insert a message.__

__Information about the bot and the developer [here](https://t.me/JFTranslatorInfo).__
(**PS: Your default language is: {1}**)
"""



lang_error = "**You already have a default language.**\n\n__Write '/modify' to change your default language.__"