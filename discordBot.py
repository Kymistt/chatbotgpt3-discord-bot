import discord
import openai

openai.api_key = ""

client = discord.Client()




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------------')
    
async def bot_response(message):
    response = openai.Completion.create(
        prompt=message.content,
        model="text-davinci-002",
        temperature=0.5,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
    )
    channel = client.get_channel()
    try:
        embed=discord.Embed(description=message.content, color=0x34cfeb)
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="Response", value=response.choices[0].text, inline=False)
        await channel.send(embed=embed)
    except:
        embed=discord.Embed(description=message.content, color=0xff4230)
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="Response", value="I'm sorry, I don't understand the question.", inline=False)
        await channel.send(embed=embed)


@client.event
async def on_message(message):
    print(message.channel.id)
    if message.author != client.user and message.channel.id == :
        print(message.content)
        await bot_response(message)


client.run("")
