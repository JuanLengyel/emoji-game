import os
import random
import math
from guizero import Box, PushButton, Picture, Text, TextBox

class Game(Box):

  def timerCountdown(self):
    if self.config["two_players"]:
      if self.player1Turn:
        self.player1Timer = self.player1Timer - 1
        self.timerText.value = str(self.player1Timer)
      else:
        self.player2Timer = self.player2Timer - 1
        self.timerText.value = str(self.player2Timer)

      if (self.player1Timer <= 0) and (self.player2Timer <= 0):
        self.showGameOver()
      elif self.player1Timer == 0:
        self.timerText.value = self.player2Timer
        self.player1Turn = False
        self.player1Timer = -1
        self.generateNewBoard()
      elif self.player2Timer == 0:
        self.timerText.value = self.player1Timer
        self.player1Turn = True
        self.player2Timer = -1
        self.generateNewBoard()

    else:
      self.timerText.value = int(self.timerText.value) - 1
      if self.timerText.value == "0":
        self.showGameOver()

  def is_correct_guess(self, pushButton):
    if self.config["two_players"]:
      if self.player1Turn:
        if self.same_image == pushButton.image:
          self.player1ScoreText.value = int(self.player1ScoreText.value) + 1
        else:
          self.player1ScoreText.value = int(self.player1ScoreText.value) - 1
        
        if (self.player2Timer > 0):
          self.timerText.value = self.player2Timer
          self.player1Turn = False
        
        self.generateNewBoard()

      else:
        if self.same_image == pushButton.image:
          self.player2ScoreText.value = int(self.player2ScoreText.value) + 1
        else:
          self.player2ScoreText.value = int(self.player2ScoreText.value) - 1

        if (self.player1Timer > 0):
          self.timerText.value = self.player1Timer
          self.player1Turn = True
        
        self.generateNewBoard()

    else:
      if self.same_image == pushButton.image:
        self.player1ScoreText.value = int(self.player1ScoreText.value) + 1
        self.generateNewBoard()
      else:
        self.player1ScoreText.value = int(self.player1ScoreText.value) - 1

  def generateNewBoard(self):

    if self.emojiShowBox != None:
      self.emojiShowBox.destroy()
    if self.emojiGuessBox != None:
      self.emojiGuessBox.destroy()

    self.emojiShowBox = Box(self, layout="grid")
    self.emojiGuessBox = Box(self, layout="grid")

    emojis_path = os.listdir("images")

    show_images = []
    guess_images = []

    # Get random images for both boxes
    for i in range(0, self.config["board_size"] - 1):
      show_images.append("images/" + emojis_path.pop(random.randint(0, len(emojis_path) - 1)))
      guess_images.append("images/" + emojis_path.pop(random.randint(0, len(emojis_path) - 1)))

    # Get image that is equal between both boxes
    rand_index = random.randint(0, len(emojis_path) - 1)
    self.same_image = "images/" + emojis_path[rand_index]
    show_images.append(self.same_image)
    guess_images.append(self.same_image)

    random.shuffle(show_images)
    random.shuffle(guess_images)

    board_size_rows = math.floor(math.sqrt(self.config["board_size"]))

    for i in range(0, self.config["board_size"]):
      x = i // board_size_rows
      y = i % board_size_rows

      picture = Picture(self.emojiShowBox, grid=[x, y], image=show_images[i])

      pushButton = PushButton(self.emojiGuessBox, grid=[x, y], image=guess_images[i])
      pushButton.update_command(command=self.is_correct_guess, args=[pushButton])

  def showGameOver(self):
    self.emojiShowBox.destroy()
    self.emojiGuessBox.destroy()
    self.cancel(self.timerCountdown)
    self.timerText.destroy()

    Text(self, text="Game Over")
    self.mainMenuButton.visible = True

    if not self.config["two_players"]:
      self.nameForLeaderBoard.visible = True
      self.submitScoreButton.visible = True

  def __init__(self, master, config):
    super().__init__(master=master)

    self.config = config

    self.emojiShowBox = None
    self.emojiGuessBox = None

    self.timerText = Text(self, text=self.config["round_timer"])
    
    self.playerScoreBox = Box(self, align="left")

    self.player1ScoreLabel = Text(self.playerScoreBox, text="Player 1 Score")
    self.player1ScoreText = Text(self.playerScoreBox, text="0")

    self.player1Turn = True

    if (self.config["two_players"]):
      self.player2ScoreLabel = Text(self.playerScoreBox, text="Player 2 Score")
      self.player2ScoreText = Text(self.playerScoreBox, text="0")

      self.player1Timer = self.config["round_timer"]
      self.player2Timer = self.config["round_timer"]

    self.same_image = ""

    self.mainMenuButton = PushButton(self, text="Main Menu", visible=False)

    self.nameForLeaderBoard = TextBox(self, text="Enter your name:", visible=False)
    self.submitScoreButton = PushButton(self, text="Submit", visible=False)

    self.generateNewBoard()

    self.repeat(1000, self.timerCountdown)