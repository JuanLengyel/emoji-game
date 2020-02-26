from start_screen import StartScreen
from option_screen import OptionScreen
from game import Game
from guizero import App, Text, PushButton

config = {
  "round_timer": 30,
  "two_players": False,
  "board_size": 9
}

leaderboard = []

def start_new_game():
  startScreen.visible = False
  game = Game(app, config)
  game.mainMenuButton.update_command(backToMainMenu, [game])
  game.submitScoreButton.update_command(addScoreToLeaderboard, [game])

def show_option_menu():
  startScreen.visible = False
  optionScreen.visible = True

def exit_game():
  app.destroy()

def set_round_timer():
  config["round_timer"] = optionScreen.roundTimerSlider.value
  print(config["round_timer"])

def set_two_player_game():
  config["two_players"] = not optionScreen.twoPlayerCheckBox.value
  print(config["two_players"])

def set_board_size():
  config["board_size"] = optionScreen.boardSizeSlider.value
  print(config["board_size"])

def show_main_menu():
  startScreen.visible = True
  optionScreen.visible = False

def backToMainMenu(game):
  game.destroy()
  startScreen.visible = True

def addScoreToLeaderboard(game):
  leaderboard.append([game.nameForLeaderBoard.value, game.player1ScoreText.value])

  game.nameForLeaderBoard.visible = False
  game.submitScoreButton.visible = False

def show_leader_board():
  startScreen.visible = False
  leaderboardScreen.visible = True
  leaderboardScreen.value = '\n'.join(list(map(lambda l: l[0] + ' - ' + l[1], leaderboard)))
  backToMainMenuFromLeaderboardButton.visible = True

def leaderboarToMainMenu():
  startScreen.visible = True
  leaderboardScreen.visible = False
  backToMainMenuFromLeaderboardButton.visible = False

app = App()

startScreen = StartScreen(app)
startScreen.startNewGameButton.when_clicked = start_new_game
startScreen.gameOptionsButton.when_clicked = show_option_menu
startScreen.showLeaderboardButton.when_clicked = show_leader_board
startScreen.exitGameButton.when_clicked = exit_game

optionScreen = OptionScreen(app, visible=False)
optionScreen.roundTimerSlider.update_command(set_round_timer)
optionScreen.roundTimerSlider.value = config["round_timer"]
optionScreen.twoPlayerCheckBox.when_clicked = set_two_player_game
optionScreen.twoPlayerCheckBox.value = config["two_players"]
optionScreen.backToMainMenuButton.when_clicked = show_main_menu
optionScreen.boardSizeSlider.update_command(set_board_size)
optionScreen.boardSizeSlider.value = config["board_size"]

leaderboardScreen = Text(app, visible=False)
backToMainMenuFromLeaderboardButton = PushButton(app, text="Back", visible=False, command=leaderboarToMainMenu)

app.display()
