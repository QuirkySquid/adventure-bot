import discord, json, os
import config as config

client = discord.Client()
lock = False
path_to_json = "adventures/"


def json_load():
    global adventures, filename, database
    with open("user_database.json", "r") as file:
        database = json.load(file)
    for filename in os.listdir("adventures"):
        if filename.endswith(".json"):
            with open(os.path.join(path_to_json, filename), "r") as file:
                loaded_adventure = json.load(file)

def user_commands(client, message):
    if message.content.startswith(config.command_prefix):
        user_info = database[message.author.id][filename]
        command, *args = message.content[1:].split()
        print(command, args)
        if command.lower == "test":
            await client.send_message(message.channel, "Test confirmed:tm:")
        elif command == "adventure":
            if database[message.author.id][filename]:
                bot_msg = await client.send_message(
                    message.channel,
                    loaded_adventure[user_info[region]][description])
                for emoji in loaded_adventure[user_info[region]][to]:
                    await client.add_reaction(
                        message=bot_msg, emoji=":"+emoji+":")
            else:
                await client.send_message(message.channel,
                    "OH! It appears as though you are not in the database for\
                     this adventure yet! Adding you now! (Please run \
                     `!adventure` again)")
#            elif command.lower == "lets_wait":
#  can              msg = await client.send_message(message.channel, "test?")
#  be              await client.wait_for_reaction(
#  ignored                  emoji=
#                    )

def admin_commands(client, message):
    command, *args = message.content[1:].split()
    print(command, args)
    if command == "meta":
        if len(args) == 3:
            await client.send_message(
                message.channel,
                filename[args[0]][args[1]][args[2]])
        elif len(args) == 2:
            await client.send_message(
                message.channel,
                filename[args[0]][args[1]])
        elif len(args) == 1:
            await client.send_message(
                message.channel,
                filename[args[0]])




@client.event
async def on_ready():
    print("""Bot Name: {}\nBot ID: {}\n------------------------------""".format(
        client.user.name,
        client.user.id))
    json_load()

@client.event
async def on_message(message):
    if message.author.id != client.user.id:
        if message.server.id == "219893635439656961" or :
            if config.command_prefix != ">":
                if message.content.startswith(config.command_prefix):
                    user_commands(client, message)
                elif message.content.startswith(">"):
                    admin_commands(client, message)
            else:
                if message.content.startswith(config.command_prefix):
                    user_commands(client, message)
                elif message.content.startswith("%"):
                    admin_commands(client, message)
        else:
            user_commands(client, message)





client.run("MzE2NjkxMTA3NjE2MzkxMTY4.DAaQbQ.x3D-fPWdtDQ8RARFhaVxXJTCXVk")
