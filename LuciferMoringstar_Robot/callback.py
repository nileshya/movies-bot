# MIT License 
  
 # Copyright (c) 2022 Muhammed 
  
 # Permission is hereby granted, free of charge, to any person obtaining a copy 
 # of this software and associated documentation files (the "Software"), to deal 
 # in the Software without restriction, including without limitation the rights 
 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
 # copies of the Software, and to permit persons to whom the Software is 
 # furnished to do so, subject to the following conditions: 
  
 # The above copyright notice and this permission notice shall be included in all 
 # copies or substantial portions of the Software. 
  
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
 # SOFTWARE. 
  
 # Telegram Link : https://telegram.dog/Mo_Tech_Group 
 # Repo Link : https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot 
 # License Link : https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot/blob/LuciferMoringstar-Robot/LICENSE 
  
 import asyncio  
 from pyrogram import Client as lucifermoringstar_robot, enums 
 from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
 from pyrogram.errors import UserIsBlocked, PeerIdInvalid, UserNotParticipant, MessageNotModified 
 from LuciferMoringstar_Robot import temp, CUSTOM_FILE_CAPTION, AUTH_CHANNEL, SUPPORT, CREATOR_NAME, CREATOR_USERNAME, SAVE_FILES, GET_FILECHANNEL, ADMINS, START_MESSAGE 
 from LuciferMoringstar_Robot.functions import get_size, get_settings, save_group_settings, is_subscribed 
 from LuciferMoringstar_Robot.modules import autofilter_text, connection_text, spellcheck_text, welcome_text, misc_text, filecaption_text 
 from LuciferMoringstar_Robot.translation import HELP_MESSAGE, ABOUT_MESSAGE, STATUS_MESSAGE, GETFILE_TEXT, USAGE_MESSAGE, NOT_SUB 
 from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, make_inactive 
 from database.autofilter_mdb import Media, get_file_details 
 from database.chats_users_mdb import db 
  
 @lucifermoringstar_robot.on_callback_query() 
 async def cb_handler(bot, update): 
  
     try: 
         userID = update.message.reply_to_message.from_user.id 
     except: 
         userID = update.from_user.id 
  
     if userID == update.from_user.id:         
  
         if update.data == "close": 
             await update.message.delete() 
  
         elif update.data.startswith("nextgroup"): 
             mrk, index, keyword = update.data.split("_") 
             try: 
                 data = temp.BUTTONS[keyword] 
             except KeyError: 
                 await update.answer("𝚃𝙷𝙸𝚂 𝙼𝚈 𝙾𝙻𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚂𝙾 𝙿𝙻𝙴𝙰𝚂𝙴 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙰𝙶𝙰𝙸𝙽 🙏",show_alert=True) 
                 return 
  
             if int(index) == int(data["total"]) - 2: 
                 buttons = data['buttons'][int(index)+1].copy() 
                 buttons.append( 
                     [InlineKeyboardButton("🔙", callback_data=f"backgroup_{int(index)+1}_{keyword}"), 
                      InlineKeyboardButton(f"📃 {int(index)+2}/{data['total']}", callback_data="pages"), 
                      InlineKeyboardButton("🗑️", callback_data="close")] 
                 ) 
                 buttons.append( 
                     [InlineKeyboardButton(text="🤖 𝙲𝙷𝙴𝙲𝙺 𝙼𝚈 𝙿𝙼 🤖", url=f"https://telegram.dog/{temp.Bot_Username}")] 
                 ) 
                 await update.edit_message_reply_markup(  
                     reply_markup=InlineKeyboardMarkup(buttons) 
                 ) 
                 return 
             else: 
                 buttons = data['buttons'][int(index)+1].copy() 
                 buttons.append( 
                     [InlineKeyboardButton("🔙", callback_data=f"backgroup_{int(index)+1}_{keyword}"), 
                      InlineKeyboardButton(f"📃 {int(index)+2}/{data['total']}", callback_data="pages"), 
                      InlineKeyboardButton("🗑️", callback_data="close"), 
                      InlineKeyboardButton("➡", callback_data=f"nextgroup_{int(index)+1}_{keyword}")] 
                 ) 
                 buttons.append( 
                     [InlineKeyboardButton(text="🤖 𝙲𝙷𝙴𝙲𝙺 𝙼𝚈 𝙿𝙼 🤖", url=f"https://telegram.dog/{temp.Bot_Username}")] 
                 ) 
                 await update.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))                 
                 return 
          
         elif update.data.startswith("backgroup"): 
             mrk, index, keyword = update.data.split("_") 
             try: 
                 data = temp.BUTTONS[keyword] 
             except KeyError: 
                 await update.answer("𝚃𝙷𝙸𝚂 𝙼𝚈 𝙾𝙻𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚂𝙾 𝙿𝙻𝙴𝙰𝚂𝙴 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙰𝙶𝙰𝙸𝙽 🙏",show_alert=True) 
                 return 
             if int(index) == 1: 
                 buttons = data['buttons'][int(index)-1].copy() 
                 buttons.append( 
                     [InlineKeyboardButton(f"📃 {int(index)}/{data['total']}", callback_data="pages"), 
                      InlineKeyboardButton("🗑️", callback_data="close"), 
                      InlineKeyboardButton("➡", callback_data=f"nextgroup_{int(index)-1}_{keyword}")] 
                 ) 
                 buttons.append( 
                     [InlineKeyboardButton(text="🤖 𝙲𝙷𝙴𝙲𝙺 𝙼𝚈 𝙿𝙼 🤖", url=f"https://telegram.dog/{temp.Bot_Username}")] 
                 ) 
                 await update.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))                 
                 return    
             else: 
                 buttons = data['buttons'][int(index)-1].copy() 
                 buttons.append( 
                     [InlineKeyboardButton("🔙", callback_data=f"backgroup_{int(index)-1}_{keyword}"), 
                      InlineKeyboardButton(f"📃 {int(index)}/{data['total']}", callback_data="pages"), 
                      InlineKeyboardButton("🗑️", callback_data="close"), 
                      InlineKeyboardButton("➡", callback_data=f"nextgroup_{int(index)-1}_{keyword}")] 
                 ) 
                 buttons.append( 
                     [InlineKeyboardButton(text="🤖 𝙲𝙷𝙴𝙲𝙺 𝙼𝚈 𝙿𝙼 🤖", url=f"https://telegram.dog/{temp.Bot_Username}")] 
                 ) 
                 await update.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))                 
                 return 
  
         elif update.data.startswith("nextbot"): 
             mrk, index, keyword = update.data.split("_") 
             try: 
                 data = temp.BUTTONS[keyword] 
             except KeyError: 
                 await update.answer("𝚃𝙷𝙸𝚂 𝙼𝚈 𝙾𝙻𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚂𝙾 𝙿𝙻𝙴𝙰𝚂𝙴 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙰𝙶𝙰𝙸𝙽 🙏",show_alert=True) 
                 return 
             if int(index) == int(data["total"]) - 2: 
                 buttons = data['buttons'][int(index)+1].copy() 
                 buttons.append( 
                     [InlineKeyboardButton("🔙", callback_data=f"backbot_{int(index)+1}_{keyword}"), 
                      InlineKeyboardButton(f"📃 {int(index)+2}/{data['total']}", callback_data="pages"), 
                      InlineKeyboardButton("🗑️", callback_data="close")] 
                 ) 
  
                 await update.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))                 
                 return 
             else: 
                 buttons = data['buttons'][int(index)+1].copy() 
                 buttons.append( 
                     [InlineKeyboardButton("🔙", callback_data=f"backbot_{int(index)+1}_{keyword}"), 
                      InlineKeyboardButton(f"📃 {int(index)+2}/{data['total']}", callback_data="pages"), 
                      InlineKeyboardButton("🗑️", callback_data="close"), 
                      InlineKeyboardButton("➡", callback_data=f"nextbot_{int(index)+1}_{keyword}")] 
                 ) 
  
                 await update.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))                 
                 return 
  
         elif update.data.startswith("backbot"): 
             mrk, index, keyword = update.data.split("_") 
             try: 
                 data = temp.BUTTONS[keyword] 
             except KeyError: 
                 await update.answer("𝚃𝙷𝙸𝚂 𝙼𝚈 𝙾𝙻𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚂𝙾 𝙿𝙻𝙴𝙰𝚂𝙴 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙰𝙶𝙰𝙸𝙽 🙏",show_alert=True) 
                 return 
             if int(index) == 1: 
                 buttons = data['buttons'][int(index)-1].copy() 
                 buttons.append( 
                     [InlineKeyboardButton(f"📃 {int(index)}/{data['total']}", callback_data="pages"), 
                      InlineKeyboardButton("🗑️", callback_data="close"), 
                      InlineKeyboardButton("➡", callback_data=f"nextbot_{int(index)-1}_{keyword}")] 
                 ) 
  
                 await update.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))                 
                 return    
             else: 
                 buttons = data['buttons'][int(index)-1].copy() 
                 buttons.append( 
                     [InlineKeyboardButton("🔙", callback_data=f"backbot_{int(index)-1}_{keyword}"), 
                      InlineKeyboardButton(f"📃 {int(index)}/{data['total']}", callback_data="pages"), 
                      InlineKeyboardButton("🗑️", callback_data="close"), 
                      InlineKeyboardButton("➡", callback_data=f"nextbot_{int(index)-1}_{keyword}")] 
                 ) 
                 await update.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))                 
                 return 
  
         elif update.data.startswith("settings"): 
             mrk, set_type, status, grp_id = update.data.split("#") 
             grpid = await active_connection(str(update.from_user.id)) 
             if str(grp_id) != str(grpid): 
                 await update.message.edit("𝙸𝙰𝙼 𝙽𝙾𝚃 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙴𝙳 𝙰𝙽𝚈 𝙶𝚁𝙾𝚄𝙿..!\n   𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 /connect 𝙰𝙽𝙳 𝙲𝙾𝙽𝙽𝙴𝙲𝚃 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃") 
             if status == "True": 
                 await save_group_settings(grpid, set_type, False) 
             else: 
                 await save_group_settings(grpid, set_type, True) 
             settings = await get_settings(grpid) 
             if settings is not None: 
                 pr0fess0r_99 = [[ 
                  InlineKeyboardButton('𝙵𝙸𝙻𝚃𝙴𝚁 𝙱𝚄𝚃𝚃𝙾𝙽', callback_data=f'settings#button#{settings["button"]}#{str(grp_id)}'),         
                  InlineKeyboardButton('𝚂𝙸𝙽𝙶𝙻𝙴' if settings["button"] else '𝙳𝙾𝚄𝙱𝙻𝙴', callback_data=f'settings#button#{settings["button"]}#{str(grp_id)}') 
                  ],[ 
                  InlineKeyboardButton('𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝙼𝚂𝙶', callback_data=f'settings#welcome#{settings["welcome"]}#{str(grp_id)}'), 
                  InlineKeyboardButton('𝙾𝙽' if settings["welcome"] else '𝙾𝙵𝙵', callback_data=f'settings#welcome#{settings["welcome"]}#{str(grp_id)}')            
                  ],[   
                  InlineKeyboardButton('𝚂𝙿𝙴𝙻𝙻 𝙲𝙷𝙴𝙲𝙺', callback_data=f'settings#spellmode#{settings["spellmode"]}#{str(grp_id)}'), 
                  InlineKeyboardButton('𝙾𝙽' if settings["spellmode"] else '𝙾𝙵𝙵', callback_data=f'settings#spellmode#{settings["spellmode"]}#{str(grp_id)}')            
                  ],[ 
                  InlineKeyboardButton('𝙱𝙾𝚃 𝙿𝙾𝚂𝚃𝙴𝚁', callback_data=f'settings#photo#{settings["photo"]}#{str(grp_id)}'), 
                  InlineKeyboardButton('𝙾𝙽' if settings["photo"] else '𝙾𝙵𝙵', callback_data=f'settings#photo#{settings["photo"]}#{str(grp_id)}')            
                  ],[ 
                  InlineKeyboardButton('𝚂𝙰𝚅𝙴 𝙵𝙸𝙻𝙴𝚂', callback_data=f'settings#savefiles#{settings["savefiles"]}#{str(grp_id)}'), 
                  InlineKeyboardButton('𝙾𝙽' if settings["savefiles"] else '𝙾𝙵𝙵', callback_data=f'settings#savefiles#{settings["savefiles"]}#{str(grp_id)}')            
                  ],[ 
                  InlineKeyboardButton('𝙵𝙸𝙻𝙴 𝙼𝙾𝙳𝙴', callback_data=f'settings#filemode#{settings["filemode"]}#{str(grp_id)}'), 
                  InlineKeyboardButton('𝙿𝙼' if settings["filemode"] else '𝙲𝙷𝙰𝙽𝙽𝙴𝙻', callback_data=f'settings#filemode#{settings["filemode"]}#{str(grp_id)}')            
                  ]] 
                 pr0fess0r_99 = InlineKeyboardMarkup(pr0fess0r_99) 
                 await update.message.edit_reply_markup(reply_markup=pr0fess0r_99) 
  
         elif update.data.startswith("luciferGP"): 
             mrk, file_id = update.data.split("#") 
             file_details_pr0fess0r99 = await get_file_details(file_id) 
             settings = await get_settings(update.message.chat.id) 
             if not file_details_pr0fess0r99: 
                 return await update.answer('𝙵𝙸𝙻𝙴 𝙽𝙾𝚃 𝙵𝙾𝚄𝙽𝙳...!') 
             files = file_details_pr0fess0r99[0] 
             title = files.file_name 
             size = get_size(files.file_size) 
  
             if not await db.is_user_exist(update.from_user.id): 
                 dellogs=await update.message.reply_text(f"""<b>𝙷𝙴𝚈 {update.from_user.mention} 𝚈𝙾𝚄𝚁 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙵𝙸𝙻𝙴 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈<b>\n\n• **𝚃𝙸𝚃𝙻𝙴** : <code>{title}</code>\n\n• **𝚂𝙸𝚉𝙴** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-ho-tech-group-{file_id}") ]] )) 
                 await asyncio.sleep(30) 
                 await dellogs.delete() 
                 return 
             if AUTH_CHANNEL and not await is_subscribed(bot, update): 
                 dellogs=await update.message.reply_text(f"""<b>𝙷𝙴𝚈 {update.from_user.mention} 𝚈𝙾𝚄𝚁 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙵𝙸𝙻𝙴 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈<b>\n\n• **𝚃𝙸𝚃𝙻𝙴** : <code>{title}</code>\n\n• **𝚂𝙸𝚉𝙴** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-ho-tech-group-{file_id}") ]] )) 
                 await asyncio.sleep(30) 
                 await dellogs.delete() 
                 return 
  
             FILE_CAPTION = settings["caption"] 
             caption = FILE_CAPTION.format(mention=update.from_user.mention, file_name=title, size=size, caption=files.caption) 
             buttons = [[ InlineKeyboardButton("⚜️ 𝚂𝙷𝙰𝚁𝙴 𝙼𝙴 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁 𝙵𝚁𝙸𝙴𝙽𝙳𝚂 ⚜️", url=f"https://t.me/share/url?url=Best%20AutoFilter%20Bot%20%0A%40Charlie_the_king_Robot%0A@{temp.Bot_Username}") ]] 
             if settings["savefiles"]: 
                 protect_content = True 
             else: 
                 protect_content = False
  
             try: 
                 if settings["filemode"]: 
                     try: 
                         await bot.send_cached_media(chat_id=update.from_user.id, file_id=file_id, caption=caption, reply_markup=InlineKeyboardMarkup(buttons), protect_content=protect_content) 
                         await update.answer("""𝙲𝙷𝙴𝙲𝙺 𝙿𝙼, 𝙸 𝙷𝙰𝚅𝙴 𝚂𝙴𝙽𝚃 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝙿𝙼\n𝙲𝙻𝙸𝙲𝙺 𝙲𝙷𝙴𝙲𝙺 𝙿𝙼 𝙱𝚄𝚃𝚃𝙾𝙽""", show_alert=True)    
                     except Exception as e: 
                         await update.message.reply(f"{e}")                   
                         dellogs=await update.message.reply_text(f"""<b>𝙷𝙴𝚈 {update.from_user.mention} 𝚈𝙾𝚄𝚁 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙵𝙸𝙻𝙴 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈<b>\n\n• **𝚃𝙸𝚃𝙻𝙴** : <code>{title}</code>\n\n• **𝚂𝙸𝚉𝙴** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-ho-tech-group-{file_id}") ]] )) 
                         await asyncio.sleep(30) 
                         await dellogs.delete() 
                 else: 
                     try: 
                         invite_link = await bot.create_chat_invite_link(GET_FILECHANNEL)       
                         dlFile = await bot.send_cached_media(chat_id=GET_FILECHANNEL, file_id=file_id, caption=caption, reply_markup=InlineKeyboardMarkup(buttons)) 
                         dlReply = await update.message.reply_text(GETFILE_TEXT.format(mention=update.from_user.mention, file_name=title, file_size=size), reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("📥 🅳︎🅾︎🆆︎🅽︎🅻︎🅾︎🅰︎🅳︎ 📥", url=dlFile.link) ],[ InlineKeyboardButton("⚠️𝙲𝙾𝙽'𝚃 𝙰𝙲𝙲𝙴𝚂𝚂 𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴⚠️", url=invite_link.invite_link) ]] )) 
                         await asyncio.sleep(1000) 
                         await dlFile.delete() 
                         await dlReply.delete() 
                     except Exception as e: 
                         await update.message.reply(f"**(1)**» {e}") 
                         dellogs=await update.message.reply_text(f"""<b>𝙷𝙴𝚈 {update.from_user.mention} 𝚈𝙾𝚄𝚁 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙵𝙸𝙻𝙴 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈<b>\n\n• **𝚃𝙸𝚃𝙻𝙴** : <code>{title}</code>\n\n• **𝚂𝙸𝚉𝙴** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-ho-tech-group-{file_id}") ]] )) 
                         await asyncio.sleep(30) 
                         await dellogs.delete() 
             except UserIsBlocked: 
                 await update.answer('Unblock the bot mahn !', show_alert=True) 
             except PeerIdInvalid: 
                 dellogs=await update.message.reply_text(f"""<b>𝙷𝙴𝚈 {update.from_user.mention} 𝚈𝙾𝚄𝚁 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙵𝙸𝙻𝙴 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈<b>\n\n• **𝚃𝙸𝚃𝙻𝙴** : <code>{title}</code>\n\n• **𝚂𝙸𝚉𝙴** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-ho-tech-group-{file_id}") ]] )) 
                 await asyncio.sleep(30) 
                 await dellogs.delete() 
             except Exception as e: 
                 await update.message.reply(f"**(2)**» {e}") 
                 dellogs=await update.message.reply_text(f"""<b>𝙷𝙴𝚈 {update.from_user.mention} 𝚈𝙾𝚄𝚁 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙵𝙸𝙻𝙴 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈<b>\n\n• **𝚃𝙸𝚃𝙻𝙴** : <code>{title}</code>\n\n• **𝚂𝙸𝚉𝙴** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-ho-tech-group-{file_id}") ]] )) 
                 await asyncio.sleep(30) 
                 await dellogs.delete() 
                  
         elif update.data.startswith("luciferPM"): 
             mrk, file_id = update.data.split("#") 
             # if not await db.is_user_exist(update.from_user.id): 
                 # dellogs=await update.message.reply_text(f"""<b>𝙷𝙴𝚈 {update.from_user.id} 𝚈𝙾𝚄𝚁 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙵𝙸𝙻𝙴 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈<b>\n\n• **𝚃𝙸𝚃𝙻𝙴** : <code>{title}</code>\n\n• **𝚂𝙸𝚉𝙴** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-ho-tech-group-{file_id}") ]] )) 
                 # await asyncio.sleep(30) 
                 # await dellogs.delete() 
                 # return 
             if AUTH_CHANNEL and not await is_subscribed(bot, update): 
                 await update.answer(NOT_SUB, show_alert=True) 
                 # dellogs=await update.message.reply_text(f"""<b>𝙷𝙴𝚈 {update.from_user.id} 𝚈𝙾𝚄𝚁 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙵𝙸𝙻𝙴 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈<b>\n\n• **𝚃𝙸𝚃𝙻𝙴** : <code>{title}</code>\n\n• **𝚂𝙸𝚉𝙴** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-ho-tech-group-{file_id}") ]] )) 
                 # await asyncio.sleep(30) 
                 # await dellogs.delete() 
                 return 
             file_details_pr0fess0r99 = await get_file_details(file_id) 
             if not file_details_pr0fess0r99: 
                 return await update.answer('𝙵𝙸𝙻𝙴 𝙽𝙾𝚃 𝙵𝙾𝚄𝙽𝙳...!') 
             files = file_details_pr0fess0r99[0] 
             title = files.file_name 
             size = get_size(files.file_size) 
             caption = CUSTOM_FILE_CAPTION.format(mention=update.from_user.mention, file_name=title, size=size, caption=files.caption) 
             buttons = [[ InlineKeyboardButton("⚜️ 𝚂𝙷𝙰𝚁𝙴 𝙼𝙴 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁 𝙵𝚁𝙸𝙴𝙽𝙳𝚂 ⚜️", url=f"https://t.me/share/url?url=Best%20AutoFilter%20Bot%20%0A%40Charlie_the_king_Robot%0A@{temp.Bot_Username}") ]] 
             try: 
                 await bot.send_cached_media(chat_id=update.from_user.id, file_id=file_id, caption=caption, reply_markup=InlineKeyboardMarkup(buttons), protect_content=SAVE_FILES)             
             except Exception as e: 
                 print(f"{e}") 
                 dellogs=await update.message.reply_text(f"""<b>𝙷𝙴𝚈 {update.from_user.id} 𝚈𝙾𝚄𝚁 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙵𝙸𝙻𝙴 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈<b>\n\n• **𝚃𝙸𝚃𝙻𝙴** : <code>{title}</code>\n\n• **𝚂𝙸𝚉𝙴** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-ho-tech-group-{file_id}") ]] )) 
                 await asyncio.sleep(30) 
                 await dellogs.delete() 
                 return 
                
         elif update.data == "start": 
             buttons = [[ InlineKeyboardButton("× 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ×", url=f"http://t.me/{temp.Bot_Username}?startgroup=true") ], 
                       [ InlineKeyboardButton("𝚂𝚄𝙿𝙿𝙾𝚁𝚃 💬", url=f"t.me/{SUPPORT}"), InlineKeyboardButton("𝚄𝙿𝙳𝙰𝚃𝙴𝚂 📢", url="t.me/HO_Tech_YT") ], 
                       [ InlineKeyboardButton("ℹ️ 𝙷𝙴𝙻𝙿", callback_data="help"), InlineKeyboardButton("𝙰𝙱𝙾𝚄𝚃 🤠", callback_data="about") ]]  
             await update.message.edit(START_MESSAGE.format(mention=update.from_user.mention, name=temp.Bot_Name, username=temp.Bot_Username), reply_markup=InlineKeyboardMarkup(buttons)) 
  
         elif update.data == "help": 
             try: 
                 buttons = [[ InlineKeyboardButton("𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁𝚂", callback_data="autofilter"), InlineKeyboardButton("𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽𝚂", callback_data="connection"), InlineKeyboardButton("𝙲𝙰𝙿𝚃𝙸𝙾𝙽", callback_data="filecaption")  ], 
                           [ InlineKeyboardButton("𝚆𝙴𝙻𝙲𝙾𝙼𝙴", callback_data="welcome"), InlineKeyboardButton("𝚂𝙿𝙴𝙻𝙻𝙲𝙷𝙴𝙲𝙺", callback_data="spellcheck"), InlineKeyboardButton("𝙼𝙸𝚂𝙲", callback_data="misc") ], 
                           [ InlineKeyboardButton("𝚂𝚃𝙰𝚃𝚄𝚂", callback_data="status"), InlineKeyboardButton("𝙷𝙾𝙼𝙴", callback_data="start") ]]                      
                 await update.message.edit(HELP_MESSAGE.format(mention=update.from_user.mention, name=temp.Bot_Name, username=temp.Bot_Username), reply_markup=InlineKeyboardMarkup(buttons)) 
             except MessageNotModified: 
                 pass 
         elif update.data == "about": 
             try: 
                 buttons = [[ InlineKeyboardButton("📦 𝚂𝙾𝚄𝚁𝙲𝙴 📦", url="https://github.com/nileshya/movies-bot")], 
                       [ InlineKeyboardButton("𝙷𝙾𝙼𝙴", callback_data="start"), InlineKeyboardButton("𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴", callback_data="usage"), InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data="close") ]]                      
                 await update.message.edit(ABOUT_MESSAGE.format(name=CREATOR_NAME, username=CREATOR_USERNAME, py3_version=temp.PY3_VERSION, pyro_version=temp.PYRO_VERSION, version=temp.BOT_VERSION, source="https://github.com/nileshya/movies-bot"), reply_markup=InlineKeyboardMarkup(buttons)) 
             except MessageNotModified: 
                 pass 
         elif update.data == "usage": 
             try: 
                 buttons = [[ InlineKeyboardButton("⇇ 𝙱𝙰𝙲𝙺 ⇇", callback_data="about") ]] 
                 await update.message.edit(USAGE_MESSAGE.format(CREATOR_NAME, CREATOR_USERNAME), reply_markup=InlineKeyboardMarkup(buttons)) 
             except MessageNotModified: 
                 pass 
         elif update.data == "status": 
             try: 
                 files = await Media.count_documents() 
                 users = await db.total_users_count() 
                 chats = await db.total_chat_count() 
                 buttons = [[ InlineKeyboardButton("⇇ 𝙱𝙰𝙲𝙺", callback_data="help"), InlineKeyboardButton("𝚁𝙴𝙵𝚁𝙴𝚂𝙷", callback_data="status"), InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴 ×", callback_data="close") ]]                                  
                 await update.message.edit(STATUS_MESSAGE.format(bot_name=temp.Bot_Name, users=users, files=files, chats=chats), reply_markup=InlineKeyboardMarkup(buttons)) 
             except MessageNotModified: 
                 pass 
  
         elif update.data == "files_delete": 
             await Media.collection.drop() 
             try: 
                 await update.message.edit('𝚂𝚄𝙲𝙲𝙴𝚂𝙵𝚄𝙻𝙻𝚈 𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝙰𝙻𝙻 𝚃𝙷𝙴 𝙸𝙽𝙳𝙴𝚇𝙴𝙳 𝙵𝙸𝙻𝙴𝚂..') 
             except MessageNotModified: 
                 pass         
         elif update.data == "autofilter": 
             try: 
                 await update.message.edit(autofilter_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("⇇ 𝙱𝙰𝙲𝙺 ⇇", callback_data="help") ]] )) 
             except MessageNotModified: 
                 pass 
         elif update.data == "connection": 
             try: 
                 await update.message.edit(connection_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("⇇ 𝙱𝙰𝙲𝙺 ⇇", callback_data="help") ]] )) 
             except MessageNotModified: 
                 pass 
         elif update.data == "spellcheck": 
             try: 
                 await update.message.edit(spellcheck_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("⇇ 𝙱𝙰𝙲𝙺 ⇇", callback_data="help") ]] )) 
             except MessageNotModified: 
                 pass 
         elif update.data == "welcome": 
             try: 
                 await update.message.edit(welcome_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("⇇ 𝙱𝙰𝙲𝙺 ⇇", callback_data="help") ]] )) 
             except MessageNotModified: 
                 pass 
         elif update.data == "misc": 
             try: 
                 await update.message.edit(misc_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("⇇ 𝙱𝙰𝙲𝙺 ⇇", callback_data="help") ]] )) 
             except MessageNotModified: 
                 pass 
         elif update.data == "filecaption": 
             try: 
                 await update.message.edit(filecaption_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("⇇ 𝙱𝙰𝙲𝙺 ⇇", callback_data="help") ]] )) 
             except MessageNotModified: 
                 pass 
  
         elif update.data == "backcb": 
             await update.answer() 
             userid = update.from_user.id 
             groupids = await all_connections(str(userid)) 
             if groupids is None: 
                 await update.message.edit("𝚃𝙷𝙴𝚁𝙴 𝙰𝚁𝙴 𝙽𝙾 𝙰𝙲𝚃𝙸𝚅𝙴 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽𝚂..! 𝙲𝙾𝙽𝙽𝙴𝙲𝚃 𝚃𝙾 𝚂𝙰𝙼𝙴 𝙶𝚁𝙾𝚄𝙿𝚂 𝙵𝙸𝚁𝚂𝚃") 
             return await update.answer('Piracy Is Crime') 
             buttons = [] 
             for groupid in groupids: 
                 try: 
                     mrk = await bot.get_chat(int(groupid)) 
                     title = mrk.title 
                     active = await if_active(str(userid), str(groupid)) 
                     act = " - ACTIVE" if active else "" 
                     buttons.append([InlineKeyboardButton(f"{title}{act}", callback_data=f"groupcb:{groupid}:{act}")])                 
                 except: 
                     pass 
             if buttons: 
                 await update.message.edit("""𝚈𝙾𝚄𝚁 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙴𝙳 𝙶𝚁𝙾𝚄𝙿 𝙳𝙴𝚃𝙰𝙸𝙻𝚂:\n\n""", reply_markup=InlineKeyboardMarkup(buttons)) 
              
         elif "deletecb" in update.data: 
             await update.answer() 
             user_id = update.from_user.id 
             group_id = update.data.split(":")[1] 
             delcon = await delete_connection(str(user_id), str(group_id)) 
             if delcon: 
                 await update.message.edit("𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽")            
             else: 
                 await update.message.edit(f"𝚂𝙾𝙼𝙴 𝙴𝚁𝚁𝙾𝚁 𝙾𝙲𝙲𝚄𝚁𝚁𝙴𝙳..!") 
             return  
  
         elif "disconnect" in update.data: 
             await update.answer() 
             group_id = update.data.split(":")[1] 
             mrk = await bot.get_chat(int(group_id)) 
             title = mrk.title 
             user_id = update.from_user.id 
             mkinact = await make_inactive(str(user_id)) 
             if mkinact: 
                 await update.message.edit(f"𝙳𝙸𝚂𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙴𝙳 𝙵𝚁𝙾𝙼 **{title}**") 
             else: 
                 await update.message.edit(f"𝚂𝙾𝙼𝙴 𝙴𝚁𝚁𝙾𝚁 𝙾𝙲𝙲𝚄𝚁𝚁𝙴𝙳..!") 
              
         elif "connectcb" in update.data: 
             await update.answer() 
             group_id = update.data.split(":")[1] 
             mrk = await bot.get_chat(int(group_id)) 
             title = mrk.title 
             user_id = update.from_user.id 
             mkact = await make_active(str(user_id), str(group_id)) 
             if mkact: 
                 await update.message.edit(f"𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙴𝙳 𝚃𝙾 **{title}**")             
             else: 
                 await update.message.edit_text('Some error occurred!!') 
             return 
  
         elif "groupcb" in update.data: 
             await update.answer() 
             group_id = update.data.split(":")[1] 
             act = update.data.split(":")[2] 
             mrk = await bot.get_chat(int(group_id)) 
             title = mrk.title 
             user_id = update.from_user.id 
  
             if act == "": 
                 stat = "🅲︎🅾︎🅽︎🅽︎🅴︎🅲︎🆃︎" 
                 cb = "connectcb" 
             else: 
                 stat = "🅳︎🅸︎🆂︎🅲︎🅾︎🅽︎🅽︎🅴︎🅲︎🆃︎" 
                 cb = "disconnect" 
  
             pr0fess0r_99 = [[ InlineKeyboardButton(f"{stat}", callback_data=f"{cb}:{group_id}") ], 
                             [ InlineKeyboardButton("𝙳𝙴𝙻𝙴𝚃𝙴", callback_data=f"deletecb:{group_id}"), InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backcb") ]]          
             pr0fess0r_99 = InlineKeyboardMarkup(pr0fess0r_99) 
             await update.message.edit("""𝙶𝚁𝙾𝚄𝙿 𝙽𝙰𝙼𝙴: **{title}**\n 𝙶𝚁𝙾𝚄𝙿 𝙸𝙳: `{group_id}`""", reply_markup=pr0fess0r_99)         
             return 
  
         elif update.data == "delallconfirm": 
             userid = update.from_user.id 
             chat_type = update.message.chat.type 
             if chat_type == enums.ChatType.PRIVATE: 
                 grpid = await active_connection(str(userid)) 
                 if grpid is not None: 
                     grp_id = grpid 
                     try: 
                         chat = await bot.get_chat(grpid) 
                         title = chat.title 
                     except: 
                         await update.message.edit("𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝙸'𝙼 𝙿𝚁𝙴𝚂𝙴𝙽𝚃 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿..!", quote=True) 
                         return  
                 else: 
                     await update.message.edit("𝙸𝙰𝙼 𝙽𝙾𝚃 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙴𝙳 𝚃𝙾 𝙰𝙽𝚈 𝙶𝚁𝙾𝚄𝙿..!\n 𝙲𝙷𝙴𝙲𝙺 /connections 𝙾𝚁 𝙲𝙾𝙽𝙽𝙴𝙲𝚃 𝚃𝙾 𝙰𝙽𝚈 𝙶𝚁𝙾𝚄𝙿𝚂", quote=True) 
                     return 
             elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]: 
                 grp_id = update.message.chat.id 
                 title = update.message.chat.title 
             else: 
                 return 
             st = await bot.get_chat_member(grp_id, userid) 
             if (st.status == enums.ChatMemberStatus.OWNER) or (str(userid) in ADMINS): 
                 await del_all(update.message, grp_id, title) 
             else: 
                 await update.answer("𝚈𝙾𝚄 𝙽𝙴𝙴𝙳 𝚃𝙾 𝙱𝙴 𝙶𝚁𝙾𝚄𝙿 𝙾𝚆𝙽𝙴𝚁 𝙾𝚁 𝙰𝙽 𝙰𝙳𝙼𝙸𝙽𝚂 𝚃𝙾 𝙳𝙾 𝚃𝙷𝙰𝚃.!", show_alert=True) 
  
         elif update.data == "delallcancel": 
             userid = update.from_user.id 
             chat_type = update.message.chat.type 
             if chat_type == enums.ChatType.PRIVATE: 
                 await update.message.reply_to_message.delete() 
                 await update.message.delete() 
             elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]: 
                 grp_id = update.message.chat.id 
                 st = await bot.get_chat_member(grp_id, userid) 
                 if (st.status == enums.ChatMemberStatus.OWNER) or (str(userid) in ADMINS): 
                     await update.message.delete() 
                     try: 
                         await update.message.reply_to_message.delete() 
                     except: 
                         pass 
                 else: 
                     await update.answer("𝚃𝙷𝙰𝚃𝚂'𝚂 𝙽𝙾𝚃 𝙵𝙾𝚁 𝚈𝙾𝚄..!", show_alert=True) 
     else: 
         await update.answer("𝚃𝙷𝙰𝚃𝚂'𝚂 𝙽𝙾𝚃 𝙵𝙾𝚁 𝚈𝙾𝚄..!", show_alert=True) 
 
