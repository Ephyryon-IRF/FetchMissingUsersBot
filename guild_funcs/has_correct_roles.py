from discord.ext import commands
from discord import app_commands
import discord

## has_correct_roles: This is a incredibly useful function. You can use this within a command and it will check if the user has any of the "Authorized" roles within registered_guilds. If not the command is killed.
def has_correct_roles(registered_guilds):
    async def predicate(source):
        # Determine if the source is a Context or Interaction
        if isinstance(source, discord.Interaction):
            guild = source.guild
            user = source.user
        else:
            guild = source.guild
            user = source.author
    
        if guild is None:
            return False

        # Get the guild ID as a string
        guild_id = str(guild.id)
        
        # Retrieve the set of role IDs associated with the guild from registered_guilds
        raw_ids = set(registered_guilds.get(guild_id, {}).get("role_perms", []))
        role_ids = {int(r) for r in raw_ids}
        
        # Get the set of role IDs that the user has
        if not hasattr(user, 'roles'):
            return False
        user_roles = {role.id for role in user.roles}
        
        # Check if the user has any of the correct roles
        return not role_ids.isdisjoint(user_roles)
    
    def decorator(func):
        func = commands.check(predicate)(func)
        func = app_commands.check(predicate)(func)
        return func


    return decorator