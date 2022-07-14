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
  
 import random, asyncio 
 from pyrogram import Client as lucifermoringstar_robot , filters, enums 
 from LuciferMoringstar_Robot import temp, SUPPORT, PICS, ADMINS, CREATOR_USERNAME, CREATOR_NAME, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, SAVE_FILES, START_MESSAGE 
 from LuciferMoringstar_Robot.translation import SETTINGS_MESSAGE, ADMIN_CMD_MESSAGE, ABOUT_MESSAGE, USAGE_MESSAGE 
 from LuciferMoringstar_Robot.functions import get_settings, save_group_settings 
 from LuciferMoringstar_Robot.admins.broadcast import send_broadcast 
 from LuciferMoringstar_Robot.functions import send_msg 
 from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
 from pyrogram.errors import UserNotParticipant 
 from database.connections_mdb import active_connection 
 from database.chats_users_mdb import db 
 from database.autofilter_mdb import get_file_details 
 from LuciferMoringstar_Robot.functions import get_size 
  
 @lucifermoringstar_robot.on_message(filters.command(["start"]) & filters.private, group=1) 
 async def start(bot: lucifermoringstar_robot, update): 
  
     if not await db.is_user_exist(update.from_user.id): 
         await db.add_user(update.from_user.id) 
  
     if update.text.startswith("/start muhammedrk"): 
         if AUTH_CHANNEL: 
             invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL)) 
             try: 
                 user = await bot.get_chat_member(int(AUTH_CHANNEL), update.from_user.id) 
                 if user.status == enums.ChatMemberStatus.RESTRICTED: 
                     await bot.send_message(chat_id=update.from_user.id, text="""𝚂𝙾𝚁𝚁𝚈 𝚂𝙸𝚁, 𝚈𝙾𝚄 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴""", disable_web_page_preview=True)                   
                     return 
             except UserNotParticipant: 
                 mrk, file_id = update.text.split("-mo-tech-group-") 
                 FORCES = ["https://telegra.ph/file/b2acb2586995d0e107760.jpg"] 
                 invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL)) 
                 pr0fess0r_99 = [[ InlineKeyboardButton("🔰 𝙹𝙾𝙸𝙽 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 🔰", url=invite_link.invite_link) ], 
                                 [ InlineKeyboardButton("🔄 𝚃𝚁𝚈 𝙰𝙶𝙰𝙸𝙽 🔄", callback_data=f"luciferPM#{file_id}") ]] 
                 pr0fess0r_99 = InlineKeyboardMarkup(pr0fess0r_99) 
                 await update.reply_photo(photo=random.choice(FORCES), caption=f"""<i><b>𝙷𝙴𝙻𝙻𝙾 {update.from_user.mention}. \n 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 <a href="{invite_link.invite_link}"> 𝙽𝙾𝚃 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴𝙳</a> 𝚃𝙾 <a href="{invite_link.invite_link}">𝙼𝚈 𝚄𝙿𝙳𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻</a>.𝚂𝙾 𝚈𝙾𝚄 𝙳𝙾 𝙽𝙾𝚃 𝙶𝙴𝚃 𝚃𝙷𝙴 𝙵𝙸𝙻𝙴𝚂 𝙾𝙽 𝙱𝙾𝚃 𝙿𝙼 𝙾𝚁 𝙶𝚁𝙾𝚄𝙿 (𝙵𝙸𝙻𝚃𝙴𝚁)</i></b>""", reply_markup=pr0fess0r_99)                 
                 return 
         try: 
             mrk, file_id = update.text.split("-mo-tech-group-") 
             file_details_pr0fess0r99 = await get_file_details(file_id) 
             for mrk in file_details_pr0fess0r99: 
                 title = mrk.file_name 
                 size = get_size(mrk.file_size) 
                 await bot.send_cached_media(chat_id=update.from_user.id, file_id=file_id, caption=CUSTOM_FILE_CAPTION.format(mention=update.from_user.mention, file_name=title, size=size, caption=mrk.caption), protect_content=SAVE_FILES) 
         except Exception as error: 
             await update.reply_text(f"𝚂𝙾𝙼𝙴𝚃𝙷𝙸𝙽𝙶 𝚆𝙴𝙽𝚃 𝚆𝚁𝙾𝙽𝙶.!\n\n𝙴𝚁𝚁𝙾𝚁:`{error}`") 
  
     if len(update.command) ==2 and update.command[1] in ["subscribe"]: 
         FORCES = ["https://telegra.ph/file/b2acb2586995d0e107760.jpg"] 
         invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL)) 
         pr0fess0r_99 = [[ InlineKeyboardButton("🔔 SUBSCRIBE 🔔", url=invite_link.invite_link) ]] 
         pr0fess0r_99 = InlineKeyboardMarkup(pr0fess0r_99) 
         await update.reply_photo(photo=random.choice(FORCES), caption=f"""<i><b>𝙷𝙴𝙻𝙻𝙾 {update.from_user.mention}. \n 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 <a href="{invite_link.invite_link}"> 𝙽𝙾𝚃 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴𝙳</a> 𝚃𝙾 <a href="{invite_link.invite_link}">𝙼𝚈 𝚄𝙿𝙳𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻</a>.𝚂𝙾 𝚈𝙾𝚄 𝙳𝙾 𝙽𝙾𝚃 𝙶𝙴𝚃 𝚃𝙷𝙴 𝙵𝙸𝙻𝙴𝚂 𝙾𝙽 𝙱𝙾𝚃 𝙿𝙼, 𝚅𝙸𝙰 𝙰𝙽𝙳 𝙶𝚁𝙾𝚄𝙿 (𝙵𝙸𝙻𝚃𝙴𝚁)</i></b>""", reply_markup=pr0fess0r_99) 
         return 
  
     if len(update.command) != 2: 
         pr0fess0r_99 = [[ InlineKeyboardButton("× 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ×", url=f"http://t.me/{temp.Bot_Username}?startgroup=true") ], 
                         [ InlineKeyboardButton("𝚂𝚄𝙿𝙿𝙾𝚁𝚃 💬", url=f"t.me/{SUPPORT}"), InlineKeyboardButton("𝚄𝙿𝙳𝙰𝚃𝙴𝚂 📢", url="t.me/Mo_Tech_YT") ], 
                         [ InlineKeyboardButton("ℹ️ 𝙷𝙴𝙻𝙿", callback_data="help"), InlineKeyboardButton("𝙰𝙱𝙾𝚄𝚃 🤠", callback_data="about") ]]  
         await bot.send_photo(photo=random.choice(PICS), chat_id=update.chat.id, caption=START_MESSAGE.format(mention=update.from_user.mention, name=temp.Bot_Name, username=temp.Bot_Username), reply_markup=InlineKeyboardMarkup(pr0fess0r_99)) 
  
 @lucifermoringstar_robot.on_message(filters.command(["admin", "admins"]) & filters.user(ADMINS) & filters.private, group=2) 
 async def admin(bot: lucifermoringstar_robot, update): 
     await bot.send_photo(photo=random.choice(PICS), chat_id=update.chat.id, caption=ADMIN_CMD_MESSAGE, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("× 𝙲𝙻𝙾𝚂𝙴 ×", callback_data="close") ]] )) 
  
 @lucifermoringstar_robot.on_message(filters.command(["about"]) & filters.private, group=3) 
 async def about(bot: lucifermoringstar_robot, update): 
     pr0fess0r_99 = [[ InlineKeyboardButton("📦 𝚂𝙾𝚄𝚁𝙲𝙴 📦", url="https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot") ], 
                     [ InlineKeyboardButton("𝙷𝙾𝙼𝙴", callback_data="start"), InlineKeyboardButton("𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴", callback_data="usage"), InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data="close") ]]                      
     await bot.send_photo(photo=random.choice(PICS), chat_id=update.chat.id, caption=ABOUT_MESSAGE.format(name = CREATOR_NAME, username = CREATOR_USERNAME, py3_version = temp.PY3_VERSION, pyro_version = temp.PYRO_VERSION, version = temp.BOT_VERSION, source = "https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot"), reply_markup=InlineKeyboardMarkup(pr0fess0r_99)) 
  
 @lucifermoringstar_robot.on_message(filters.command(["usage"]) & filters.private, group=4) 
 async def usage(bot: lucifermoringstar_robot, update): 
     pr0fess0r_99 = [[ InlineKeyboardButton("🗑️ 𝙳𝙴𝙻𝙴𝚃𝙴 🗑️", callback_data="close") ]] 
     await bot.send_photo(photo=random.choice(PICS), chat_id=update.chat.id, caption=USAGE_MESSAGE.format(CREATOR_NAME, CREATOR_USERNAME), reply_markup=InlineKeyboardMarkup(pr0fess0r_99)) 
  
 @lucifermoringstar_robot.on_message(filters.command(["broadcast"]) & filters.user(ADMINS) & filters.private, group=5) 
 async def broadcast(bot: lucifermoringstar_robot, update): 
     await send_broadcast(bot, update, db, send_msg, temp) 
  
 @lucifermoringstar_robot.on_message((filters.private | filters.group) & filters.command('settings'), group=5) 
 async def settings(bot, update): 
     userid = update.from_user.id if update.from_user else None 
     if not userid: 
         return await update.reply_text(f"𝚈𝙾𝚄𝚁 𝙰𝚁𝙴 𝙰𝙽𝙾𝙽𝚈𝙼𝙾𝚄𝚂 𝙰𝙳𝙼𝙸𝙽. /connect {update.chat.id} 𝙸𝙽 𝙿𝙼") 
     chat_type = update.chat.type 
     if chat_type == enums.ChatType.PRIVATE: 
         grpid = await active_connection(str(userid)) 
         if grpid is not None: 
             grp_id = grpid 
             try: 
                 chat = await bot.get_chat(grpid) 
                 title = chat.title 
             except: 
                 await update.reply_text("𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝙸𝙰𝙼 𝙿𝚁𝙴𝚂𝙴𝙽𝚃 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿..!", quote=True) 
                 return 
         else: 
             await update.reply_text("𝙸𝙰𝙼 𝙽𝙾𝚃 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙴𝙳 𝙰𝙽𝚃 𝙶𝚁𝙾𝚄𝙿..!", quote=True) 
             return 
  
     elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]: 
         grp_id = update.chat.id 
         title = update.chat.title 
     else: 
         return 
  
     mrk = await bot.get_chat_member(grp_id, userid) 
     if (mrk.status != enums.ChatMemberStatus.ADMINISTRATOR and mrk.status != enums.ChatMemberStatus.OWNER and userid not in ADMINS): 
         return 
  
     settings = await get_settings(grp_id) 
  
     if settings is not None: 
         buttons = [[ InlineKeyboardButton('𝙵𝙸𝙻𝚃𝙴𝚁 𝙱𝚄𝚃𝚃𝙾𝙽', callback_data=f'settings#button#{settings["button"]}#{grp_id}'), InlineKeyboardButton('𝚂𝙸𝙽𝙶𝙻𝙴' if settings["button"] else '𝙳𝙾𝚄𝙱𝙻𝙴', callback_data=f'settings#button#{settings["button"]}#{grp_id}') ], 
                    [ InlineKeyboardButton('𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝙼𝚂𝙶', callback_data=f'settings#welcome#{settings["welcome"]}#{grp_id}'), InlineKeyboardButton('𝙾𝙽' if settings["welcome"] else '𝙾𝙵𝙵', callback_data=f'settings#welcome#{settings["welcome"]}#{grp_id}') ],          
                    [ InlineKeyboardButton('𝚂𝙿𝙴𝙻𝙻 𝙲𝙷𝙴𝙲𝙺', callback_data=f'settings#spellmode#{settings["spellmode"]}#{grp_id}'), InlineKeyboardButton('𝙾𝙽' if settings["spellmode"] else '𝙾𝙵𝙵', callback_data=f'settings#spellmode#{settings["spellmode"]}#{grp_id}') ],           
                    [ InlineKeyboardButton('𝙱𝙾𝚃 𝙿𝙾𝚂𝚃𝙴𝚁', callback_data=f'settings#photo#{settings["photo"]}#{grp_id}'), InlineKeyboardButton('𝙾𝙽' if settings["photo"] else '𝙾𝙵𝙵', callback_data=f'settings#photo#{settings["photo"]}#{grp_id}') ], 
                    [ InlineKeyboardButton('𝚂𝙰𝚅𝙴 𝙵𝙸𝙻𝙴𝚂', callback_data=f'settings#savefiles#{settings["savefiles"]}#{grp_id}'), InlineKeyboardButton('𝙾𝙽' if settings["savefiles"] else '𝙾𝙵𝙵', callback_data=f'settings#savefiles#{settings["savefiles"]}#{grp_id}') ], 
                    [ InlineKeyboardButton('𝙵𝙸𝙻𝙴 𝙼𝙾𝙳𝙴', callback_data=f'settings#filemode#{settings["filemode"]}#{grp_id}'), InlineKeyboardButton('𝙿𝙼' if settings["filemode"] else '𝙲𝙷𝙰𝙽𝙽𝙴𝙻', callback_data=f'settings#filemode#{settings["filemode"]}#{grp_id}') ]] 
         reply_markup = InlineKeyboardMarkup(buttons) 
         await update.reply_text(text=SETTINGS_MESSAGE.format(title=title), reply_markup=reply_markup, disable_web_page_preview=True, reply_to_message_id=update.id) 
          
 @lucifermoringstar_robot.on_message((filters.private | filters.group) & filters.command('set_temp'), group=6) 
 async def save_template(bot, update): 
     sts = await update.reply_text("⏳️") 
     await asyncio.sleep(0.3) 
     userid = update.from_user.id if update.from_user else None 
     if not userid: 
         return await update.reply_text(f"𝚈𝙾𝚄𝚁 𝙰𝚁𝙴 𝙰𝙽𝙾𝙽𝚈𝙼𝙾𝚄𝚂 𝙰𝙳𝙼𝙸𝙽. /connect {update.chat.id} 𝙸𝙽 𝙿𝙼") 
     chat_type = update.chat.type 
     if chat_type == enums.ChatType.PRIVATE: 
         grpid = await active_connection(str(userid)) 
         if grpid is not None: 
             grp_id = grpid 
             try: 
                 chat = await bot.get_chat(grpid) 
                 title = chat.title 
             except: 
                 await update.reply_text("𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝙸𝙰𝙼 𝙿𝚁𝙴𝚂𝙴𝙽𝚃 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿..!", quote=True) 
                 return 
         else: 
             await update.reply_text("𝙸𝙰𝙼 𝙽𝙾𝚃 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙴𝙳 𝙰𝙽𝚃 𝙶𝚁𝙾𝚄𝙿..!", quote=True) 
             return 
  
     elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]: 
         grp_id = update.chat.id 
         title = update.chat.title 
     else: 
         return 
  
     motechyt = await bot.get_chat_member(grp_id, userid) 
     if (motechyt.status != enums.ChatMemberStatus.ADMINISTRATOR and motechyt.status != enums.ChatMemberStatus.OWNER and userid not in ADMINS): 
         return 
  
     if len(update.command) < 2: 
         return await sts.edit("𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳..!", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴", callback_data="autofilter") ]] )) 
  
     pr0fess0r_99 = update.text.split(" ", 1)[1] 
     await save_group_settings(grp_id, 'template', pr0fess0r_99) 
     await sts.edit(f"""𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙲𝙷𝙰𝙽𝙶𝙴𝙳 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 (𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚃𝙴𝙼𝙿) 𝙵𝙾𝚁 {title} 𝚃𝙾\n\n{pr0fess0r_99}""", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("× 𝙲𝙻𝙾𝚂𝙴 ×", callback_data="close") ]] )) 
  
 @lucifermoringstar_robot.on_message((filters.private | filters.group) & filters.command('setwelcome'), group=7) 
 async def setwelcome(client, message): 
     sts = await message.reply("⏳️") 
     await asyncio.sleep(0.3) 
     userid = message.from_user.id if message.from_user else None 
     if not userid: 
         return await message.reply(f" 𝚈𝙾𝚄𝚁 𝙰𝚁𝙴 𝙰𝙽𝙾𝙽𝚈𝙼𝙾𝚄𝚂 𝙰𝙳𝙼𝙸𝙽. /connect {message.chat.id} 𝙸𝙽 𝙿𝙼") 
     chat_type = message.chat.type 
     if chat_type == enums.ChatType.PRIVATE: 
         grpid = await active_connection(str(userid)) 
         if grpid is not None: 
             grp_id = grpid 
             try: 
                 chat = await client.get_chat(grpid) 
                 title = chat.title 
             except: 
                 await message.reply_text("𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝙸𝙰𝙼 𝙿𝚁𝙴𝚂𝙴𝙽𝚃 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿..!", quote=True) 
                 return 
         else: 
             await message.reply_text("𝙸𝙰𝙼 𝙽𝙾𝚃 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙴𝙳 𝙰𝙽𝚃 𝙶𝚁𝙾𝚄𝙿..!", quote=True) 
             return 
  
     elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]: 
         grp_id = message.chat.id 
         title = message.chat.title 
  
     else: 
         return 
  
     member = await client.get_chat_member(grp_id, userid) 
     if (member.status != enums.ChatMemberStatus.ADMINISTRATOR and member.status != enums.ChatMemberStatus.OWNER and userid not in ADMINS): 
         return 
  
     if len(message.command) < 2: 
         return await sts.edit("𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳..!", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴", callback_data="welcome") ]] )) 
  
     pr0fess0r_99 = message.text.split(" ", 1)[1] 
     await save_group_settings(grp_id, 'welcometext', pr0fess0r_99) 
     await sts.edit(f"""𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙲𝙷𝙰𝙽𝙶𝙴𝙳 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙵𝙾𝚁 {title} 𝚃𝙾\n\n{pr0fess0r_99}""", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("× 𝙲𝙻𝙾𝚂𝙴 ×", callback_data="close") ]] )) 
  
  
 @lucifermoringstar_robot.on_message((filters.private | filters.group) & filters.command('setspell'), group=8) 
 async def setspell(client, message): 
     sts = await message.reply("⏳️") 
     await asyncio.sleep(0.3) 
     userid = message.from_user.id if message.from_user else None 
     if not userid: 
         return await message.reply(f" 𝚈𝙾𝚄𝚁 𝙰𝚁𝙴 𝙰𝙽𝙾𝙽𝚈𝙼𝙾𝚄𝚂 𝙰𝙳𝙼𝙸𝙽. /connect {message.chat.id} 𝙸𝙽 𝙿𝙼") 
     chat_type = message.chat.type 
     if chat_type == enums.ChatType.PRIVATE: 
         grpid = await active_connection(str(userid)) 
         if grpid is not None: 
             grp_id = grpid 
             try: 
                 chat = await client.get_chat(grpid) 
                 title = chat.title 
             except: 
                 await message.reply_text("𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝙸𝙰𝙼 𝙿𝚁𝙴𝚂𝙴𝙽𝚃 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿..!", quote=True) 
                 return 
         else: 
             await message.reply_text("𝙸𝙰𝙼 𝙽𝙾𝚃 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙴𝙳 𝙰𝙽𝚃 𝙶𝚁𝙾𝚄𝙿..!", quote=True) 
             return 
  
     elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]: 
         grp_id = message.chat.id 
         title = message.chat.title 
  
     else: 
         return 
  
     member = await client.get_chat_member(grp_id, userid) 
     if ( 
             member.status != enums.ChatMemberStatus.ADMINISTRATOR 
             and member.status != enums.ChatMemberStatus.OWNER 
             and userid not in ADMINS 
     ): 
         return 
  
     if len(message.command) < 2: 
         return await sts.edit("𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳..!", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴", callback_data="spellcheck") ]] )) 
  
     pr0fess0r_99 = message.text.split(" ", 1)[1] 
     await save_group_settings(grp_id, 'spelltext', pr0fess0r_99) 
     await sts.edit(f"""𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙲𝙷𝙰𝙽𝙶𝙴𝙳 𝚂𝙴𝚃 𝚂𝙿𝙴𝙻𝙻 𝙲𝙷𝙴𝙲𝙺 𝙵𝙾𝚁 {title} 𝚃𝙾\n\n{pr0fess0r_99}""", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("× 𝙲𝙻𝙾𝚂𝙴 ×", callback_data="close") ]] )) 
  
 @lucifermoringstar_robot.on_message((filters.private | filters.group) & filters.command('setcaption'), group=9) 
 async def filecap(client, message): 
     sts = await message.reply("⏳️") 
     await asyncio.sleep(0.3) 
     userid = message.from_user.id if message.from_user else None 
     if not userid: 
         return await message.reply(f" 𝚈𝙾𝚄𝚁 𝙰𝚁𝙴 𝙰𝙽𝙾𝙽𝚈𝙼𝙾𝚄𝚂 𝙰𝙳𝙼𝙸𝙽. /connect {message.chat.id} 𝙸𝙽 𝙿𝙼") 
     chat_type = message.chat.type 
     if chat_type == enums.ChatType.PRIVATE: 
         grpid = await active_connection(str(userid)) 
         if grpid is not None: 
             grp_id = grpid 
             try: 
                 chat = await client.get_chat(grpid) 
                 title = chat.title 
             except: 
                 await message.reply_text("𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝙸𝙰𝙼 𝙿𝚁𝙴𝚂𝙴𝙽𝚃 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿..!", quote=True) 
                 return 
         else: 
             await message.reply_text("𝙸𝙰𝙼 𝙽𝙾𝚃 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙴𝙳 𝙰𝙽𝚃 𝙶𝚁𝙾𝚄𝙿..!", quote=True) 
             return 
  
     elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]: 
         grp_id = message.chat.id 
         title = message.chat.title 
  
     else: 
         return 
  
     member = await client.get_chat_member(grp_id, userid) 
     if ( 
             member.status != enums.ChatMemberStatus.ADMINISTRATOR 
             and member.status != enums.ChatMemberStatus.OWNER 
             and userid not in ADMINS 
     ): 
         return 
  
     if len(message.command) < 2: 
         return await sts.edit("𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳..!", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴", callback_data="filecaption") ]] )) 
  
     pr0fess0r_99 = message.text.split(" ", 1)[1] 
     await save_group_settings(grp_id, 'caption', pr0fess0r_99) 
     await sts.edit(f"""𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙲𝙷𝙰𝙽𝙶𝙴𝙳 𝙵𝙸𝙻𝙴 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 𝙵𝙾𝚁 {title} 𝚃𝙾\n\n{pr0fess0r_99}""", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("× 𝙲𝙻𝙾𝚂𝙴 ×", callback_data="close") ]] ))
