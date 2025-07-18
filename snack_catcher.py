import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Snack Catcher")
        pyxel.load("assets.pyxres")
        self.reset_game()
        pyxel.run(self.update, self.draw)

    def reset_game(self):
        self.player_x = 60
        self.player_y = 100
        self.score = 0
        self.carrots = []
        self.bombs = []
        self.friends = [] # 仲間のリスト
        self.time_left = 30
        self.game_over = False
        self.powerup_timer = 0 # パワーアップの残り時間

    def update(self):
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.reset_game()
            return

        # パワーアップタイマーを減らす
        if self.powerup_timer > 0:
            self.powerup_timer -= 1

        # Player movement
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 2, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)

        # Determine spawn rates
        lemon_rate = 10 if self.powerup_timer > 0 else 30
        bug_rate = 15 if self.powerup_timer > 0 else 50

        # Generate carrots (lemons)
        if pyxel.frame_count % lemon_rate == 0:
            self.carrots.append([pyxel.rndi(0, pyxel.width - 8), 0])

        # Generate bombs (bugs)
        if pyxel.frame_count % bug_rate == 0:
            self.bombs.append([pyxel.rndi(0, pyxel.width - 8), 0])

        # Generate friends (golden bears) - very rarely
        if pyxel.rndi(0, 500) == 0: # 約8秒に1回くらいの確率
            self.friends.append([pyxel.rndi(0, pyxel.width - 16), 0])

        # Update carrots (lemons)
        for carrot in self.carrots[:]:
            carrot[1] += 1
            if (self.player_x < carrot[0] + 8 and self.player_x + 16 > carrot[0] and
                self.player_y < carrot[1] + 8 and self.player_y + 16 > carrot[1]):
                self.score += 10
                self.carrots.remove(carrot)
            elif carrot[1] > pyxel.height:
                self.carrots.remove(carrot)

        # Update bombs (bugs)
        for bomb in self.bombs[:]:
            bomb[1] += 1
            if (self.player_x < bomb[0] + 8 and self.player_x + 16 > bomb[0] and
                self.player_y < bomb[1] + 8 and self.player_y + 16 > bomb[1]):
                if self.powerup_timer <= 0: # パワーアップ中でなければスコアダウン
                    self.score -= 10
                self.bombs.remove(bomb)
            elif bomb[1] > pyxel.height:
                self.bombs.remove(bomb)

        # Update friends (golden bears)
        for friend in self.friends[:]:
            friend[1] += 1
            if (self.player_x < friend[0] + 16 and self.player_x + 16 > friend[0] and
                self.player_y < friend[1] + 16 and self.player_y + 16 > friend[1]):
                self.powerup_timer = 150 # 5秒間 (30fps * 5s)
                self.friends.remove(friend)
            elif friend[1] > pyxel.height:
                self.friends.remove(friend)

        # Update timer
        if pyxel.frame_count % 30 == 0 and self.time_left > 0:
            self.time_left -= 1
            if self.time_left == 0:
                self.game_over = True

    def draw(self):
        pyxel.cls(12) # Sky
        pyxel.rect(0, 0, 160, 40, 3) # Tree Canopy
        pyxel.rect(30, 40, 100, 80, 4) # Tree Trunk

        # Draw player (bear)
        player_u = 0
        # パワーアップ中は点滅させる
        if self.powerup_timer > 0 and pyxel.frame_count % 4 < 2:
            player_u = 16 # 金色のクマのスプライトを使う
        pyxel.blt(self.player_x, self.player_y, 0, player_u, 0, 16, 16, 0)

        # Draw lemons
        for carrot in self.carrots:
            pyxel.blt(carrot[0], carrot[1], 1, 0, 0, 8, 8, 0)

        # Draw bugs
        for bomb in self.bombs:
            pyxel.blt(bomb[0], bomb[1], 2, 0, 0, 8, 8, 0)

        # Draw friends
        for friend in self.friends:
            pyxel.blt(friend[0], friend[1], 0, 16, 0, 16, 16, 0)

        # Draw UI
        pyxel.text(5, 5, f"Score: {self.score}", 7)
        pyxel.text(5, 15, f"Time: {self.time_left}", 7)
        if self.powerup_timer > 0:
            pyxel.text(5, 25, "POWER UP!", pyxel.frame_count % 8 + 8)

        if self.game_over:
            pyxel.text(55, 50, "Time's Up!", 0)
            pyxel.text(50, 60, f"Final Score: {self.score}", 0)
            pyxel.text(35, 70, "Press Enter to Restart", 0)

App()
