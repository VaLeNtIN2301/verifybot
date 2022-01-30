import discord
from discord.ext import commands
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import command, cooldown
import random
import time
import datetime
import asyncio
import json




class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_role("verify+")
    async def verify(self, ctx, member: discord.Member=False):
        if member == False:
            help = "verify"
            emb = await self.bot.cogs["Help"].mesaj_help(ctx, help)
            await ctx.send(embed=emb)
        else:

            await member.add_roles(discord.utils.get(member.guild.roles, name="verify"))
            await ctx.send("Ok")


    @commands.command()
    @commands.cooldown(2, 8, commands.BucketType.user)
    async def ping(self, ctx):
        now = time.time_ns()/1e6
        msg = await ctx.send("🏓")
        send_time = time.time_ns()/1e6
        embed = discord.Embed(title = '🏓Pong!', description = (f'Bot latency:{round(self.bot.latency * 1000)} ms\nREST latency:{round(send_time - now)} ms'),color = 0x62016f)
        await msg.edit(content=None, embed=embed)



def setup(bot):
    bot.add_cog(Verify(bot))
