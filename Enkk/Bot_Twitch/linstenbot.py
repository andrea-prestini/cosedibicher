from bot import Bot


class ListenBot(Bot):

    def action(self, username, msg):
        print(username, " > ", msg)


bot = ListenBot(channel="#enkk")
bot.run()
