from bot import Bot

EMOTE = "picciOne"
points = {}


def ppPoints(p):
    sp = sorted(p.items(), key=lambda x: x[1], reverse=True)
    for k, v in sp:
        print(k, "->", v)


class LmaoBot(Bot):
    msg_counter = 0

    def action(self, username, msg):
        if EMOTE in msg:
            self.msg_counter += 1
            if username not in points.keys():
                points[username] = 0

            points[username] += 1

        if self.msg_counter == 50:
            print("-------------")
            ppPoints(points)
            self.msg_counter = 0


bot = LmaoBot(channel="#enkk")
bot.run()
