from discord.ext import commands

def guild_owner_only():
    async def predicate(source):
        if isinstance(source, commands.Context):
            guild = source.guild
            user = source.author
        else:
            guild = source.guild
            user = source.user
        return guild is not None and user == guild.owner
    return commands.check(predicate)