import discord, json, os
import config as config

client = discord.Client()
lock = False
path_to_json = "adventures/"

def json_load():
    global adventures, filename
    for filename in os.listdir("adventures"):
        if filename.endswith(".json"):
            with open(os.path.join(path_to_json, filename), "r") as file:
                filename = json.load(file)
            print(filename)



@client.event
async def on_ready():
    print("""Bot Name: {}\nBot ID: {}\n------------------------------""".format(
        client.user.name,
        client.user.id))
    json_load()

@client.event
async def on_message(message):
    if message.server.id == "219893635439656961":
        if message.content.startswith(config.command_prefix):
            command, *args = message.content[1:].split()
            if command == "test":
                await client.send_message(message.channel, "Test confirmed:tm:")
            elif command.lower == "lets_wait":
                msg = await client.send_message(message.channel, "test?")
                await client.wait_for_reaction()
        elif message.content.startswith(">"):
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
            elif command == "":
    else:
        if message.content.startswith(config.command_prefix):
            command, *args = message.content[1:].split()
            if command.lower == "test":
                await client.send_message(message.channel, "Test confirmed:tm:")
#            elif command.lower == "lets_wait":
#  can              msg = await client.send_message(message.channel, "test?")
#  be              await client.wait_for_reaction(
#  ignored                  emoji=
#                    )





client.run("MzE2NjkxMTA3NjE2MzkxMTY4.DAaQbQ.x3D-fPWdtDQ8RARFhaVxXJTCXVk")
