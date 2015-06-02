import Tkinter

class nat20_tk(Tkinter.Tk):
  def __init__(self,parent):
    Tkinter.Tk.__init__(self,parent)
    self.parent = parent
    self.initialize()

  def initialize(self):
    pass 

if __name__ == "__main__":
  app = nat20_tk(None)
  app.title('Nat 20')
  app.mainloop()
