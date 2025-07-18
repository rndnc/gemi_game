import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Snack Catcher")
        pyxel.load("assets.pyxres") # Load the resource file
        self.reset_game()
        pyxel.run(self.update, self.draw)

    def reset_game(self):
        self.player_x = 60
        self.player_y = 100
        self.score = 0
        self.carrots = []
        self.bombs = []
        self.time_left = 30
        self.game_over = False

    def update(self):
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.reset_game()
            return

        # Player movement
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 2, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)

        # Generate carrots
        if pyxel.frame_count % 30 == 0:
            self.carrots.append([pyxel.rndi(0, pyxel.width - 8), 0])

        # Generate bombs
        if pyxel.frame_count % 50 == 0:
            self.bombs.append([pyxel.rndi(0, pyxel.width - 8), 0])

        # Update carrots
        for carrot in self.carrots[:]:
            carrot[1] += 1
            if (self.player_x < carrot[0] + 8 and self.player_x + 16 > carrot[0] and
                self.player_y < carrot[1] + 8 and self.player_y + 16 > carrot[1]):
                self.score += 10
                self.carrots.remove(carrot)
            elif carrot[1] > pyxel.height:
                self.carrots.remove(carrot)

        # Update bombs
        for bomb in self.bombs[:]:
            bomb[1] += 1
            if (self.player_x < bomb[0] + 8 and self.player_x + 16 > bomb[0] and
                self.player_y < bomb[1] + 8 and self.player_y + 16 > bomb[1]):
                self.score -= 10
                self.bombs.remove(bomb)
            elif bomb[1] > pyxel.height:
                self.bombs.remove(bomb)

        # Update timer
        if pyxel.frame_count % 30 == 0 and self.time_left > 0:
            self.time_left -= 1
            if self.time_left == 0:
                self.game_over = True

    def draw(self):
        pyxel.cls(12) # Light blue background

        # Draw player (bear from Image 0)
        # blt(x, y, img, u, v, w, h, [colkey])
        # Using color 13 (magenta) as the transparent color.
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 16, 16, 13)

        # Draw carrots (from Image 1)
        for carrot in self.carrots:
            pyxel.blt(carrot[0], carrot[1], 1, 0, 0, 8, 8, 13)

        # Draw bombs (from Image 2)
        for bomb in self.bombs:
            pyxel.blt(bomb[0], bomb[1], 2, 0, 0, 8, 8, 13)

        # Draw UI
        pyxel.text(5, 5, f"Score: {self.score}", 7)
        pyxel.text(5, 15, f"Time: {self.time_left}", 7)

        if self.game_over:
            pyxel.text(60, 50, "Game Over", 0)
            pyxel.text(45, 60, "Press Enter", 0)

App()
