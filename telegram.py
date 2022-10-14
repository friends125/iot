import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop
red = 35
now = datetime.datetime.now()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#LED Red
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, 0) #Off initially
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Received: %s' % command)
    if 'on' in command:
        message = "on"
        if 'red' in command:
            message = message + "red "
            GPIO.output(red, 1)
        telegram_bot.sendMessage (chat_id, message)
        
    if 'off' in command:
        message = "off "
        if 'red' in command:
            message = message + "red "
            GPIO.output(red, 0)
        telegram_bot.sendMessage (chat_id, message)
        
telegram_bot = telepot.Bot('5540204096:AAFvNcOSa2Q532aKeq_HldWs9jsoL1oBYbE')
print (telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')
while 1:
    time.sleep(5)
