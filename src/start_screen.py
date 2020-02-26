from guizero import Box, PushButton

class StartScreen(Box):

  def __init__(self, master, visible=True):
    super().__init__(master=master, visible=visible)

    self.startNewGameButton = PushButton(self, text="Start New Game")
    self.gameOptionsButton = PushButton(self, text="Options")
    self.showLeaderboardButton = PushButton(self, text="Leaderboard")
    self.exitGameButton = PushButton(self, text="Exit")