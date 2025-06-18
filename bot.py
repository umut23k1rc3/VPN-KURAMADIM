import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

# --- Ekstra görev için sınıf ---
class Car:
    def __init__(self, renk, marka):
        self.renk = renk
        self.marka = marka

    def info(self):
        return f"Araba Markası: {self.marka}, Renk: {self.renk}"

# --- Basit Komut: /repeat ---
@bot.command()
async def repeat(ctx, tekrar_sayisi: int, *, mesaj):
    await ctx.send((mesaj + '\n') * tekrar_sayisi)

# --- Gelişmiş Komut: /car ---
@bot.command()
async def car(ctx, renk, marka):
    araba = Car(renk, marka)
    await ctx.send(araba.info())

# Botu çalıştır (TOKEN kısmını kendi token’ınla değiştir)
bot.run("YOUR_BOT_TOKEN")
