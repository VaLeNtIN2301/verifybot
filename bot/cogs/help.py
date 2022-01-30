import discord
from discord.ext import commands
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import command, cooldown
import random
import time
import datetime
import asyncio
import json




class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.d = {"ping": "Verifică latența bot-ului.",
                  "verify": "verifică un membru"}
        self.u = {
            "ping": f"{self.bot.prefix} ping",
            "verify": f"{self.bot.prefix} verify <id utilizator>"}

    async def mesaj_help(self, ctx, help):
         hmenu = discord.Embed()
         hmenu.set_author(name=f"{help.title()}", icon_url="https://images-ext-2.discordapp.net/external/HFSiDBLRBW9BJO19zinehjLZUfVT9f-9vVNwzWlLd7U/%3Ftoken%3Dexp%3D1637489574~hmac%3D1baa1ad67097e96e7be508283446a5e8/https/cdn-icons.flaticon.com/png/512/1687/premium/1687119.png")
         hmenu.set_thumbnail(url="https://images-ext-2.discordapp.net/external/8xee1w80vOxKWOsHOS6Y-Ug6u17gvPSAsAwE7TvnfQY/%3Ftoken%3Dexp%3D1637489574~hmac%3D8639937c0e4bf6a42c539d2a1f0a2fcd/https/cdn-icons.flaticon.com/png/512/2039/premium/2039807.png")
         hmenu.add_field(name="<:feedback:849702291426639953>Descriere:", value=self.d[help.lower()], inline=False)
         hmenu.add_field(name="<:qrcode:849702568292777994>Utilizare:", value=self.u[help.lower()], inline=False)
         await ctx.send(embed=hmenu)

    @commands.command()
    async def help(self, ctx):
        dior = self.bot.get_user(id=590963835548991508)
        embed = discord.Embed(title="Meniu de ajutor").add_field(name="ping", value=self.d["ping"]).add_field(name="verify", value=self.d["verify"])
        embed.set_footer(text=f"Developer : {dior}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
