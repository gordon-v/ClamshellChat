import asyncio
import discord
import responses
import creds
import python_client

#Method that sends message in the channel, or in DMs
async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message) #The response is calculated in responses.py
        if response == '':
            return
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
    #connect to the server
    
    global text_gogi
    
    TOKEN = creds.TOKEN
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    client = discord.Client(intents=intents)
    gogi = client.get_user(creds.gogi_id)

    @client.event
    async def on_ready():
        

        print(f'BOT: {client.user} is now running.')
        

        #ADD A THREAD THAT RUNS AND LISTENS FOR MESSAGES IN THIS METHOD (CAUSE ITS ASYNC)

        python_client.init_client("BOT Client")
        python_client.recieve_thread.start()

    #Prints all the incoming messages, calls reply function
    @client.event
    async def on_message(message):
        
        if message.author == client.user: #if bot sent the message -> ignore message
            return

        username = str(message.author)

        channel = str(message.channel)
        
        user_message = str(message.content)
        
       

        print(f'BOT: {username} said: {user_message} in {channel}')

        try:

            if user_message[0] == '?' and username == 'tedi#8858':
                user_message=user_message[1:]
                await send_message(message, user_message, is_private=True)
            else:
                await send_message(message, user_message, is_private=False) #calculate reply and send accordingly
                msg_log = f'{username} said "{user_message}"'
                python_client.write(msg_log)    #print to console the message and who sent it

                await client.get_user(creds.gogi_id).send(msg_log)  #send to DMS the message and who sent it
        except:
                print("SERVER: The message is probably not ASCII encodable. Or some other error occured.")
                return


    async def text_gogi_async(msg):
        await client.get_user(creds.gogi_id).send(msg)


    client.run(TOKEN)
    