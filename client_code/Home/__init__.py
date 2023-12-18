from ._anvil_designer import HomeTemplate
from anvil import *

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def my_method(self, name):
    # alert(f"Hello, {name}")
    print(f"Hello, {name}")
    return 42