import requests,re
from hh import keep_alive
try:
    import telebot
except:
    import os
    os.system("pip install pyTelegramBotAPI")
from telebot import *
from GATEAU import Tele
from colorama import Fore
sto = {"stop":False}
token = "2127774305:AAGMgeytMWlZAeAjZop7VVbYp8voMF5KpeQ" 
id =  1490490774
ph = "https://j.top4top.io/m_2807oa5811.mp4"
bot=telebot.TeleBot(token,parse_mode="HTML")
@bot.message_handler(commands=["stop"])
def start(message):
    sto.update({"stop":True})
    bot.reply_to(message,'*- [#] DONE STOP BOT🌈🩶 .*', parse_mode = 'Markdown')
@bot.message_handler(commands=["start"])
def start(message):
 #bot.send_message(message.chat.id,"*- 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 BOT CHECK 🧾 .\n- [&] Premium @RKRKQ 🫴🏻 .\n- Stop Bot Check Commands : /stop .*", parse_mode = 'Markdown'.format(message.chat.first_name),reply_markup=telebot.types.InlineKeyboardMarkup())
 bot.send_video(message.chat.id,ph,caption=f"""*- 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 BOT CHECK 🧾 .\n- [$] Premium @RKRKQ 🫴🏻 .\n- Stop Bot Check Commands : /stop . *""",parse_mode="markdown")
@bot.message_handler(content_types=["document"])
def main(message):
 first_name = message.from_user.first_name
 last_name = message.from_user.last_name
 name=f"{first_name} {last_name}"
 risk=0
 bad=0
 nok=0
 ok = 0
 ko = (bot.reply_to(message,f"*- WELCOME {name} I WILL NOW START CHECK*", parse_mode = 'Markdown').message_id)
 ee=bot.download_file(bot.get_file(message.document.file_id).file_path)
 with open("combo.txt","wb") as w:
     w.write(ee)
 print(message.chat.id)
 sto.update({"stop":False})
 if message.chat.id == id:
   with open("combo.txt") as file:
       lino = file.readlines()
       lino = [line.rstrip() for line in lino]
       total = len(lino)
       for cc in lino:
           if sto["stop"] == False:
               pass
           else:
               break
           bin=cc[:6]
           url=f"https://lookup.binlist.net/{bin}"
           try:
           	req=requests.get(url).json()
           except:
           	pass
           try:
           	inf = req['scheme']
           except:
           	inf = "------------"
           try:
           	type = req['type']
           except:
           	type = "-----------"
           try:
           	brand = req['brand']
           except:
           	brand = '-----'
           try:
           	info = inf + '-' + type + '-' + brand
           except:
           	info = "-------"
           try:
           	ii = info.upper()
           except:
           	ii = "----------"
           try:
           	bank = req['bank']['name'].upper()
           except:
           	bank = "--------"
           try:
           	do = req['country']['name'] + ' ' + req['country']['emoji'].upper()
           except:
           	do = "-----------"
           mes = types.InlineKeyboardMarkup(row_width=1)
           GALD1 = types.InlineKeyboardButton(f"𓌹 {cc} 𓌺",callback_data='u8')
           #res = types.InlineKeyboardButton(f"• {last} •",callback_data='u1')
           GALD3 = types.InlineKeyboardButton(f"༄ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ : [ {ok} ] ࿑",callback_data='u2')
           GALD4 = types.InlineKeyboardButton(f"༄ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌  : [ {bad} ] ࿑",callback_data='u1')
           risk6 = types.InlineKeyboardButton(f"༄ 𝗥𝗜𝗦𝗞 🥲  : [ {risk} ] ࿑",callback_data='u1')
           GALD5 = types.InlineKeyboardButton(f"༄ 𝗧𝗢𝗧𝗔𝗟 👀✨  : [ {total} ] ࿑",callback_data='u1')
           btn = types.InlineKeyboardButton(f"༒aBo DiYaR #33࿐ ", url = 'https://t.me/RKRKQ')
           mes.add(GALD1,GALD3,GALD4,risk6,GALD5,btn)
           bot.edit_message_text(chat_id=message.chat.id,message_id=ko,text=f'''*HELLO {name}, PLEASE WAIT FOR CHECK COMBO AND SEND HIT 🪯.
    \n- Type : [ Premium ✅ ] Activity .*''',parse_mode='markdown',reply_markup=mes)
           
           try:
             last = str(Tele(cc))
           except Exception as e:
               print(e)
               try:
                  last = str(Tele(cc))
               except Exception as e:
                  print(e)
                  bot.reply_to(message,f"*CARD IS DEAD AND I SKIPPED >> {cc}*",parse_mode = 'Markdown')
           if "risk" in last:
           	risk += 1
           	print(Fore.YELLOW+cc+"->"+Fore.CYAN+last)
           elif "Insufficient Funds" in last:
               ok +=1
               respo = f'''
CC - ↯  {cc}
Status - ↯ #Approved ✅  
R/s - ↯ Approved (1000)
Gate - ↯ Braintree Auth ⛈️
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯  {ii} 
Country - ↯ {do}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Power Mode - ↯ [ ON ]
'''
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,respo)
               with open("hit.txt", "a") as f:
               	f.write(f'''
CC - ↯  {cc}
Status - ↯ #Approved ✅  
R/s - ↯ Approved (1000)
Gate - ↯ Braintree Auth ⛈️
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯  {ii} 
Country - ↯ {do}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Power Mode - ↯ [ ON ]
''')
           elif "Status code avs: Gateway Rejected: avs" in last or "Nice! New payment method added:" in last or "Status code 81724: Duplicate card exists in the vault." in last:
               ok += 1
               respo = (f'''
CC - ↯  {cc}
Status - ↯ #Approved ✅  
R/s - ↯ Approved (1000)
Gate - ↯ Braintree Auth ⛈️
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯  {ii} 
Country - ↯ {do}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Power Mode - ↯ [ ON ]
''')
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,respo)
               with open("hit.txt", "a") as f:
               	f.write(f'''
CC - ↯  {cc}
Status - ↯ #Approved ✅  
R/s - ↯ Approved (1000)
Gate - ↯ Braintree Auth ⛈️
- - - - - - - - - - - - - - - - - - - - -
Bin - ↯  {ii} 
Country - ↯ {do}
Bank - ↯ {bank}
- - - - - - - - - - - - - - - - - - - - -
Power Mode - ↯ [ ON ]
''')
           else:
                   bad +=1
                   print(Fore.YELLOW+cc+"->"+Fore.RED+last)
       if sto["stop"] == False:
           bot.reply_to(message,'*[$] Don Combo all cc .*', parse_mode = 'Markdown')
 else:
     bot.reply_to(message,'*THE BOT IS PREMIUM CALL ME \n @RKRKQ*', parse_mode = 'Markdown')
keep_alive()
print("STARTED BOT @RKRKQ ")
bot.infinity_polling()
