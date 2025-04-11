BotToken = "YourBotToken"
#replace with your bot token
User_ID = 0
#replace with the user ID of the player you want to track (the user ID is number in roblox.com/users/0000000000)
User_ID2 = 0
#keep this unchanged if the player you want to track doesn't have a second account
name=("The player") 
#replace with the name of the player you want to track
import requests
from telegram.ext import Updater, CommandHandler
ROBLOX_USER_IDS = [User_ID, User_ID2]
def get_status():
    url = "https://presence.roblox.com/v1/presence/users"
    payload = {"userIds": ROBLOX_USER_IDS}
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        for user_data in data["userPresences"]:
            user_id = user_data["userId"]
            status = user_data["userPresenceType"]
            if status == 1 or status == 2:
                return name + " is playing Roblox."
        return name + " is not playing Roblox."
    except Exception as e:
        return name + " is not playing Roblox."
def roblox(update, context):
    msg = get_status()
    update.message.reply_text(msg)
def set_bot_commands(bot):
    commands = [
        {"command": "roblox", "description": "Check if the player is playing Roblox"}
    ]
    try:
        bot.set_my_commands(commands)
    except Exception as e:
        print(f"Error setting bot commands: {e}")
def main():
    updater = Updater(BotToken, use_context=True)
    dp = updater.dispatcher
    bot = updater.bot
    set_bot_commands(bot)
    dp.add_handler(CommandHandler("roblox", roblox)) 
    updater.start_polling()
    print("Bot is running. Press Ctrl+C to stop.")
    updater.idle()
if __name__ == "__main__":
    main()
