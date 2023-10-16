from ._anvil_designer import chat_with_usTemplate
from anvil import *

class chat_with_us(chat_with_usTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')
    pass

