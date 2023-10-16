from ._anvil_designer import contact_usTemplate
from anvil import *

class contact_us(contact_usTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')

