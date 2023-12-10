from bot import Bot


class HelloBot(Bot):
    def run(self):
        self.chat("Ciao non sono un bot ok giuro non sono un bot")


bot = HelloBot(channel="#enkk")
bot.run()
