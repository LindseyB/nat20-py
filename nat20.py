import Tkinter
import random
import yaml
from functools import partial

class nat20_tk(Tkinter.Tk):
  def __init__(self,parent):
    Tkinter.Tk.__init__(self,parent)
    self.parent = parent
    self.initialize()

  def initialize(self):
    sheet_stream = open("sheet.yaml", 'r')
    sheet = yaml.load(sheet_stream)
    
    for character, rolls in sheet.iteritems():
      labelframe = Tkinter.LabelFrame(self, text=character)
      labelframe.pack(fill="both", expand="yes")
      for roll_text, roll in rolls.iteritems():
        roll_command = partial(self.do_roll, roll)
        button = Tkinter.Button(labelframe, text = roll_text + " Roll", command = roll_command)
        button.pack()

    text = Tkinter.Text(self)
    text.insert(Tkinter.INSERT, "Results:")
    text.pack()

  def do_roll(self, roll):
    print roll


if __name__ == "__main__":
  app = nat20_tk(None)
  app.title('Nat 20')
  app.mainloop()
