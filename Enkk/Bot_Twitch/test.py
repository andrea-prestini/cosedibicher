from bot import Bot
from time import sleep


class WellsBot(Bot):
    def run(self):
        while True:
            print("Ho detto ciao")
            self.chat("Ciao")
            sleep(5)


bot = WellsBot(channel="#enkk")
bot.run()
