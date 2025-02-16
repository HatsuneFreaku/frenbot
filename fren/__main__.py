import os
import crescent, hikari
from keep_alive import keep_alive

bot = hikari.GatewayBot(os.environ["TOKEN"], intents = hikari.Intents.ALL)
client = crescent.Client(bot)

if __name__ == "__main__":
    if os.name != "nt":
        import asyncio




keep_alive()
bot.run()