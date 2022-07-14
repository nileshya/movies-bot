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
  
 from pyrogram import Client as lucifermoringstar_robot , filters, enums 
 from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
 from LuciferMoringstar_Robot import ADMINS, CREATOR_USERNAME 
  
 @lucifermoringstar_robot.on_message((filters.group | filters.private) & filters.command('leave') & filters.user(ADMINS)) 
 async def leave_bot(bot, update): 
     if len(update.command) == 1: 
         return await update.reply_text("𝙶𝙸𝚅𝙴 𝙼𝙴 𝙰 𝙶𝚁𝙾𝚄𝙿 𝙸𝙳") 
     chat = update.command[1] 
     try: 
         chat = int(chat) 
     except: 
         chat = chat 
     try: 
         pr0fess0r_99 = [[ InlineKeyboardButton('𝙶𝙴𝚃 𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url=f'https://t.me/{CREATOR_USERNAME}') ]] 
         pr0fess0r_99 = InlineKeyboardMarkup(pr0fess0r_99) 
         await bot.send_message(chat_id=chat, text="𝙷𝙴𝙻𝙻𝙾 𝙵𝚁𝙸𝙴𝙽𝙳𝚂,\n𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝙷𝙰𝚂 𝚃𝙾𝙻𝙳 𝙼𝙴 𝚃𝙾 𝙻𝙴𝙰𝚅𝙴 𝙵𝚁𝙾𝙼 𝙶𝚁𝙾𝚄𝙿. 𝚂𝙾 𝙸 𝙶𝙾 😛. 𝙸𝙵 𝚈𝙾𝚄 𝚆𝙰𝙽𝙽𝙰 𝙰𝙳𝙳 𝙼𝙴 𝙰𝙶𝙰𝙸𝙽 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙼𝙴", reply_markup=pr0fess0r_99) 
         await bot.leave_chat(chat) 
         await update.reply(f"𝙻𝙴𝙵𝚃 𝚃𝙷𝙴 𝙲𝙷𝙰𝚃 `{chat}`") 
     except Exception as e: 
         await update.reply(f'𝙴𝚁𝚁𝙾𝚁 - {e}')
