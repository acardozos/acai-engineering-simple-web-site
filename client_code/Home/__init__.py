from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def my_method(self, name):
    # alert(f"Hello, {name}")
    print(f"Hello, {name}")
    return 42