import rg


class Robot:
    flag = False
    def act(self, game):
        l = list(rg.locs_around(self.location, filter_out=('invalid', 'obstacle')))
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:

                if rg.dist(loc, self.location) <= 1:
                    if game.robots[loc].hp <= 10:
                        return ['move', l[0]]
        if self.hp <=11:
            for loc, bot in game.robots.iteritems():
                if bot.player_id != self.player_id:
                    if rg.dist(loc, self.location) <= 1:
                        return ['suicide']
        # if there are enemies around, attack them
        count = 0
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                     count+=1
        if count >=3 and self.hp <=31:
            return ['suicide']
        if count >=2 and self.hp <=21:
            return ['suicide']

        locs = []
        count = 0
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                locs.append(loc)
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 2:
                    if self.flag:
                        if rg.dist(loc, self.location) <= 1:
                            return ['attack', rg.toward(self.location, loc)]
                        self.flag = False
                        return['move', rg.toward(self.location, rg.CENTER_POINT)]
                    self.flag = True
                    return ['attack', rg.toward(self.location, loc)]

        for loc, bot in game.robots.iteritems():
            if bot.player_id == self.player_id:
                if rg.dist(loc, self.location) <= 3:
                     count+=1
        if count >=4:
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]

        closest = min(locs)

        return ['move', rg.toward(self.location, closest)]