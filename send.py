import sys
import discord

from ruamel import yaml

settings = yaml.load(open(sys.argv[1], 'r'))
client = discord.Client()


@client.event
async def on_ready():
    for uid in settings['recipients']:
        user = client.get_user(uid)
        if user is None:
            print(f'Could not get user with id {uid}')
            continue

        try:
            await user.send('This is a weekly backup archive.')
        except discord.Forbidden:
            print(f'Could not send to {user}')
            continue

        for fname in settings['files']:
            try:
                await user.send(file=discord.File(open(fname, 'rb')))
            except discord.Forbidden:
                print(f'Could not send {fname}')
                await user.send(
                    f'Could not send {fname}. Please `sftp` into the VPS and manually retrieve the file.'
                )
            else:
                print(f'Successfully sent {fname}')

    await client.logout()

client.run(settings['token'])
