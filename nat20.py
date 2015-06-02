import Tkinter
import random
import yaml
import time
import random,re
from functools import partial
from collections import OrderedDict

def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)


class nat20_tk(Tkinter.Tk):
  def __init__(self,parent):
    Tkinter.Tk.__init__(self,parent)
    self.parent = parent
    self.initialize()

  def initialize(self):
    sheet_stream = open("sheet.yaml", 'r')
    sheet = ordered_load(sheet_stream)

    for character, rolls in sheet.iteritems():
      labelframe = Tkinter.LabelFrame(self, text=character)
      labelframe.pack(fill="both", expand="yes")
      column_height = len(rolls)/3 + 1
      for index, (roll_text, roll) in enumerate(rolls.iteritems()):
        roll_command = partial(self.do_roll, roll)
        button = Tkinter.Button(labelframe, text = roll_text + " Roll", command = roll_command)
        button.grid(row=index%column_height, column=index/column_height, sticky=Tkinter.W)

    self.text = Tkinter.Text(self)
    self.text.insert(Tkinter.INSERT, "Results:")
    self.text.pack(fill=Tkinter.BOTH, expand=1)

    photo = Tkinter.PhotoImage(file="d20.gif")

    self.frames = []
    for frame in range(1, 21):
      self.frames.append(Tkinter.PhotoImage(file="d20.gif", format="gif -index " + str(frame)))

    self.d20 = Tkinter.Label(self, image=self.frames[0])
    self.d20.image = self.frames[0]


  def do_roll(self, roll):
    self.d20.place(relx=0.5, rely=0.5, anchor=Tkinter.CENTER)
    for frame in self.frames:
      time.sleep(0.1)
      self.d20.configure(image=frame)
      self.d20.image = frame
      self.update()

    result = re.sub(r'd(\d+)', lambda match: "(" + str(random.randint(1, int(match.group(1)))) + ")", roll)
    # weee wooo weee wooo eval
    self.text.insert(Tkinter.INSERT, "\n" + roll + " = "+ result + " = " + str(eval(result)))
    self.text.see(Tkinter.END)
    self.d20.place_forget()


if __name__ == "__main__":
  app = nat20_tk(None)
  app.title('Nat 20')
  app.mainloop()
