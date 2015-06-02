import Tkinter
import random
import yaml
from functools import partial
import random,re
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
    self.text.pack()

  def do_roll(self, roll):
    result = re.sub(r'd(\d+)', lambda match: "(" + str(random.randint(1, int(match.group(1)))) + ")", roll)
    # weee wooo weee wooo eval
    self.text.insert(Tkinter.INSERT, "\n" + roll + " = "+ result + " = " + str(eval(result)))


if __name__ == "__main__":
  app = nat20_tk(None)
  app.title('Nat 20')
  app.mainloop()
