import discord
import responses
import creds

#Method that sends message in the channel, or in DMs
async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message) #The response is calculated in responses.py
        if is_private:
            await message.author.send(response)
            # TODO: SEND THIS MESSAGE TO THE CLIENT via SERVER
        else:
            await message.channel.send(response)

    except Exception as e:
        print(e)
        
#Run the bot
def run_discord_bot():
    print("BOT: Launching Discord Bot")

    TOKEN = creds.TOKEN
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'BOT: {client.user} is now running.')

    #Prints all the incoming messages, calls reply function
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'BOT: {username} said: {user_message} in {channel}')

        if user_message[0] == '?' and username == 'tedi#8858':
            user_message=user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)