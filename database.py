import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='JFTranslator')

cursor = cnx.cursor(buffered=True)

# inserisce all'interno del DB la lingua di default (comando /language)
insertDefLangDb = "INSERT INTO def_lang (user_id, default_language) VALUES (%s, %s)"

# seleziona all'interno del DB la linuga di default (comando traduzione)
query_tran = str("SELECT default_language FROM def_lang  WHERE user_id = {}")

# elimina all'interno del DB la lingua di default (comando /modify)
query_mod = "DELETE FROM def_lang WHERE user_id = {}"


query_regist_log = "SELECT default_language FROM def_lang WHERE user_id = {}"