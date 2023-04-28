import telegram.ext
import telegram
import os
import time
import subprocess
import sys
async def help(update,context):
    await update.message.reply_text('''

    /torch_on 		---> torch on
    /open_google 	---> open google app
    call:number 	---> call the number you give
    msg:number text 	---> send text message on number

    NOTE:- don't give sapce after ':' colon
                                    ''')
async def torch_on(Update,Context):
	os.system("termux-torch on")
	await Update.message.reply_text("ok")
async def torch_off(update,context):
	os.system("termux-torch off")
	await update.message.reply_text("ok")
async def open_google(update,context):
	os.system("xdg-open https://google.com")
	await update.message.reply_text("ok")
async def msg(update,context):
    text=update.message.text
    if(text[:8]=="command:"):
        #print(update.message.text)
        command=text.split("command:")[1]
        output=subprocess.getoutput(command)
        await update.message.reply_text(output)
    elif(text[:5]=="call:"):
        number=text.split("call:")[1]
        output=subprocess.getoutput(f"termux-telephony-call {number}")
        if(output==""):
            await update.message.reply_text("calling start..")
        else:
            await update.message.reply_text(output)
    elif(text[:4]=="msg:"):
        number=text.split("msg:")[1]
        msg=number.split(" ")[1]
        output=subprocess.getoutput(f"termux-sms-send -n {number} '{msg}'")
        if(output==""):
            await update.message.reply_text("sending done.")
        else:
            await update.message.replay_text(output)
    else:
        await update.message.reply_text('''
        /torch_on 		---> torch on
        /open_google 	-	---> open google app
        call: number 		---> call the number you give
        msg: number text 	---> send text message on number
        NOTE:- don't give sapce after ':' colon
                                         ''')
try:
    TOKEN=sys.argv[1]
except Exception :
    print("\npython bot.py <telegram bot token>\n")
    sys.exit()
application=telegram.ext.ApplicationBuilder().token(TOKEN).build()
tele=telegram.ext.CommandHandler
application.add_handler(tele("torch_on",torch_on))
application.add_handler(tele("torch_off",torch_off))
application.add_handler(tele("open_google",open_google))
application.add_handler(tele("help", help))
#this function for normal message not for command
application.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.TEXT,msg))
print("")
print("\033[96;4mCREATER: HUI HOLA\033[0m\n")
time.sleep(1)
print("\033[92mbot server running...\033[0m\n")
application.run_polling()
