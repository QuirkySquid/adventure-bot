import discord, json, os
import config as config

client = discord.Client()
lock = False
path_to_json = "adventures/"


def json_load():
    global adventures, filename, database, emojis, loaded_adventure
    with open("user_database.json", "r") as file:
        database = json.load(file)
    for filename in os.listdir("adventures"):
        if filename.endswith(".json"):
            with open(os.path.join(path_to_json, filename), "r") as file:
                loaded_adventure = json.load(file) #pylint: disable=W0612,W0621

def change_position(user, newpos):
    with open("user_database.json", "r") as file:
        json_data = json.load(file)
        json_data[user][filename] = newpos

    with open("user_database.json", "w") as file:
        file.write(json.dumps(json_data, indent=2))
        file.close

async def user_commands(client, message):
    if message.content.startswith(config.command_prefix):
        user_info = database[message.author.id][filename]
        command, *args = message.content[1:].split()
        print(command, args)
        if command.lower() == "test":
            await sendMessage(message.channel, "Test confirmed:tm:")
        elif command.lower() == "adventure":
            if database[message.author.id][filename]:
                bot_msg = await sendMessage(message.channel,
                                            loaded_adventure[user_info]["description"]) #pylint: disable=E1136,E0602
            else: #TODO: Automate this
                sendMessage(message.channel,
                            "OH! It appears as though you are not in the database for\
                            this adventure yet! Adding you now! (Please run \
                            `!adventure` again)")
#                for key in loaded_adventure[user_info]["to"].keys():                  #pylint: disable=E1136,E0602
#                    emoji = emojis[key][0:]
#                    print(emoji)
#                    await addReaction(bot_msg, emoji)
        elif command.lower() in loaded_adventure[user_info]["to"].keys():
            user_info = loaded_adventure[user_info]["to"][command.lower()]
            change_position(message.author.id, user_info)
            bot_msg = await sendMessage(message.channel,
                                        loaded_adventure[user_info]["description"]) #pylint: disable=E1136,E0602
#            elif command.lower == "lets_wait":
#  can              msg = sendMessage("test?")
#  be              await client.wait_for_reaction(
#  ignored                  emoji=
#                    )

async def admin_commands(client, message):
    command, *args = message.content[1:].split()
    print(command, args)
    if command == "meta":
        if len(args) == 3:
            sendMessage(message.channel,
                        filename[args[0]][args[1]][args[2]])
        elif len(args) == 2:
            sendMessage(message.channel,
                        filename[args[0]][args[1]])
        elif len(args) == 1:
            sendMessage(message.channel,
                        filename[args[0]])




@client.event
async def on_ready():
    print("""Bot Name: {}\nBot ID: {}\n------------------------------""".format(
        client.user.name,
        client.user.id))
    json_load()

@client.event
async def on_message(message):
    json_load()
    if message.author.id != client.user.id:
        if message.server.id == "219893635439656961":
            if config.command_prefix != ">":
                if message.content.startswith(config.command_prefix):
                    await user_commands(client, message)
                elif message.content.startswith(">"):
                    await admin_commands(client, message)
            else:
                if message.content.startswith(config.command_prefix):
                    await user_commands(client, message)
                elif message.content.startswith("%"):
                    await admin_commands(client, message)
        else:
            await user_commands(client, message)

async def sendMessage(channel, text):
    return await client.send_message(channel, text)

async def addReaction(message, emoji):
    await client.add_reaction(message, "")



client.run("MzE2NjkxMTA3NjE2MzkxMTY4.DAaQbQ.x3D-fPWdtDQ8RARFhaVxXJTCXVk")
