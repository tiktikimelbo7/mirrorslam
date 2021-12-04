from telegram.ext import CommandHandler
from bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from bot import LOGGER, dispatcher
from bot.helper.telegram_helper.message_utils import *
from bot.helper import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands



def list_folder(update,context):
    try:
        search = update.message.text.split(' ',maxsplit=1)[1]
    except IndexError:
        sendMessage(f'<b><i>Send A Keyword Along With Search Command</i></b>', context.bot, update)
        return
   
    reply = sendMessage(f'<b>Searching...🔎</b>', context.bot, update)

    LOGGER.info(f"Searching: {search}")
        
    gdrive = GoogleDriveHelper(None)
    msg, button = gdrive.drive_list(search)

    editMessage(msg,reply,button)

look_handler = CommandHandler(BotCommands.LookCommand, list_folder,filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(look_handler)
