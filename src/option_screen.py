from guizero import Box, PushButton, Slider, Text, CheckBox

class OptionScreen(Box):

  def __init__(self, master, visible=True):
    super().__init__(master=master, visible=visible)

    self.roundTimerLabel = Text(self, text="Set the seconds of each round")
    self.roundTimerSlider = Slider(self)

    self.twoPlayerLabel = Text(self, text="Two Player Game?")
    self.twoPlayerCheckBox = CheckBox(self)

    self.boardSizeLabel = Text(self, text="Set the board Size")
    self.boardSizeSlider = Slider(self, end=30)

    self.backToMainMenuButton = PushButton(self, text="Back")