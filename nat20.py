import Tkinter
import random
import yaml
from functools import partial
import random,re

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
      for index, (roll_text, roll) in enumerate(rolls.iteritems()):
        roll_command = partial(self.do_roll, roll)
        button = Tkinter.Button(labelframe, text = roll_text + " Roll", command = roll_command)
        button.grid(row=index/3, column=index%3)

    self.text = Tkinter.Text(self)
    self.text.insert(Tkinter.INSERT, "Results:")
    self.text.pack()

  def do_roll(self, roll):
    result = re.sub(r'd(\d+)', lambda match: "(" + str(random.randint(1, int(match.group(1)))) + ")", roll)
    # weee wooo weee wooo eval
    self.text.insert(Tkinter.INSERT, "\n" + roll + " = "+ result + " = " + str(eval(result)))


if __name__ == "__main__":
  app = nat20_tk(None)
  app.title('Nat 20')
  app.mainloop()
