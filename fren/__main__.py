import os
import crescent, hikari

bot = hikari.GatewayBot(os.environ["TOKEN"], intents = hikari.Intents.ALL)
client = crescent.Client(bot)

if __name__ == "__main__":
    if os.name != "nt":
        import asyncio





bot.run()