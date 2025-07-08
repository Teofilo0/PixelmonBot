import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from keep_alive import keep_alive
keep_alive()


load_dotenv()

TOKEN = os.getenv("TOKEN")
ID_CANAL_DESTINO = int(os.getenv("ID_CANAL_DESTINO"))
ID_CARGO_MENCIONAR = int(os.getenv("ID_CARGO_MENCIONAR"))

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

PALAVRAS_CHAVE = ["Um", "lendário", "apareceu", "spawned", "has spawned", "Legendary"]

@bot.event
async def on_ready():
    print(f'✅ Bot online como {bot.user}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if any(palavra.lower() in message.content.lower() for palavra in PALAVRAS_CHAVE):
        canal_destino = bot.get_channel(ID_CANAL_DESTINO)
        if canal_destino:
            cargo_mention = f"<@&{ID_CARGO_MENCIONAR}>"
            embed = discord.Embed(
                title="⚠️ Lendário Spawnado!",
                description=f"{cargo_mention}\nMensagem detectada:\n```\n{message.content}\n```",
                color=discord.Color.gold()
            )
            await canal_destino.send(content=cargo_mention, embed=embed)

    await bot.process_commands(message)

bot.run(TOKEN)
