from datetime import datetime
import datetime as dtime
import asyncio, time

data = {} 

def create(msg):
    if str(msg.from_user.id) not in list(data.keys()):
        data.update({str(msg.from_user.id): {'timestamp': 0, 'proceed': False}})

async def send_cooldown(msg):
    user = msg.from_user
    try:await msg.delete()                  #delete the command when in a cooldown
    except:pass
    if data[str(user.id)]['proceed'] is True: #if true
        data[str(user.id)]['proceed'] = False #then enter this code and save it as False, save it as False will prevent entering this code if send a command again
        ids = await msg.reply(f"Sorry {user.mention}, this command is in cooldown, wait for {int(data[str(user.id)]['timestamp'] - time.time())} seconds to use this command again..")
        cond = True #condition
        while cond: #enter loop if cond var is True
            if int(data[str(user.id)]['timestamp'] - time.time()) == 0:
                await ids.edit_text(f"Alright {user.mention}, cooldown for this command is over.")
                await asyncio.sleep(1)
                await ids.delete() #after that delete the bot, message on the var ids
                cond = False       #if cooldown time is 0 then save cond var as False
                break              #then break the loop

def wait(seconds):
    def decorator(func):
        async def wrapper(_, msg):
            user = msg.from_user
            create(msg)
            if int(data[str(user.id)]['timestamp'] - time.time()) < 1:
                est = datetime.now() + dtime.timedelta(seconds=seconds)
                data[str(user.id)]['timestamp'] = est.timestamp()
                data[str(user.id)]['proceed'] = True #save cooldown status as True
                return await func(_, msg)
            else:
                await send_cooldown(msg)
        return wrapper
    return decorator