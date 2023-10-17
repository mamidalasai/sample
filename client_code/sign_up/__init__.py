from ._anvil_designer import sign_upTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class sign_up(sign_upTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.name.text
    email = self.email.text
    number = self.number.text
    password = self.password.text
    anvil.server.call('sign_up', name, number, email, password)


