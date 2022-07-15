import logging 
 from pyrogram import Client, emoji, filters 
 from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultCachedDocument 
  
 from database.autofilter_mdb import get_search_results 
 from LuciferMoringstar_Robot import CACHE_TIME, AUTH_USERS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION 
 from LuciferMoringstar_Robot.functions import get_size, is_subscribed 
  
 logger = logging.getLogger(__name__) 
 cache_time = 0 if AUTH_USERS or AUTH_CHANNEL else CACHE_TIME 
  
 @Client.on_inline_query(filters.user(AUTH_USERS) if AUTH_USERS else None) 
 async def answer(bot, update): 
  
     if AUTH_CHANNEL and not await is_subscribed(bot, update): 
         switch_pm_text="𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝚃𝙾 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙴 𝙱𝙾𝚃" # 𝙱𝚈 𝙻𝚄𝙲𝙸𝙵𝙴𝚁 
         await update.answer(results = [], cache_time = 0, switch_pm_text = switch_pm_text, switch_pm_parameter = "subscribe") 
         return 
  
     results = [] 
     if '|' in update.query: 
         string, file_type = update.query.split('|', maxsplit=1) 
         string = string.strip() 
         file_type = file_type.strip().lower() 
     else: 
         string = update.query.strip() 
         file_type = None 
  
     offset = int(update.offset or 0) 
     reply_markup = get_reply_markup(query=string) 
     files, next_offset, total_results = await get_search_results(string, file_type=file_type, max_results = 10, offset = offset) 
  
     for file in files: 
         title=file.file_name 
         size=get_size(file.file_size) 
         caption=CUSTOM_FILE_CAPTION.format(mention=update.from_user.mention, file_name=title, size=size, caption=file.caption) 
         results.append(InlineQueryResultCachedDocument(title = file.file_name, document_file_id = file.file_id, caption = caption, description = f"𝚂𝙸𝚉𝙴 : {get_size(file.file_size)}\n𝚃𝚈𝙿𝙴 : {file.file_type}", reply_markup = reply_markup)) 
  
     if results: 
         switch_pm_text = f"{emoji.FILE_FOLDER} 𝚁𝙴𝚂𝚄𝙻𝚃𝚂" 
         if string: 
             switch_pm_text += f" 𝙵𝙾𝚁 {string}" 
         try: 
             await update.answer(results = results, is_personal = True, cache_time = cache_time, switch_pm_text = switch_pm_text, switch_pm_parameter="start", next_offset = str(next_offset)) 
         except Exception as error: 
             logging.exception(str(error)) 
             await update.answer(results = [], is_personal = True, cache_time = cache_time, switch_pm_text = str(e)[:63], switch_pm_parameter = "error") 
     else: 
         switch_pm_text = f'{emoji.CROSS_MARK} No results' 
         if string: 
             switch_pm_text += f' for "{string}"' 
         await update.answer(results = [], is_personal = True, cache_time = cache_time, switch_pm_text = switch_pm_text, switch_pm_parameter = "okay") 
  
 def get_reply_markup(query): 
     buttons = [[ InlineKeyboardButton('🔍 Search Again 🔎', switch_inline_query_current_chat=query) ]] 
     return InlineKeyboardMarkup(buttons)
