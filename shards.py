import discord

client = discord.AutoShardedClient(shard_count=3)

'''
@client.event
async def on_shard_ready(shard):
    print(client.guilds)
    await client.change_presence(game=discord.Game(name=str(shard)), shard_id=shard)
'''
@client.event
async def on_ready():
    print(client.guilds)
    await client.change_presence(game=discord.Game(name='HTSTEM'), shard_id=0)
    try:
        await client.change_presence(game=discord.Game(name='HTC'), shard_id=2)
    except KeyError:
        print('Failed')
    
client.run('token')
