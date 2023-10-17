from ._anvil_designer import create_accountTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random

class create_account(create_accountTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    acc_number = random.choice(range(10000000000, 99999999999))
    self.acc_number = acc_number

  def home_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.name.text
    email = self.email.text
    number = self.number.text
    pan_card = self.pan_card.text
    anvil.server.call('create_account', name, number, email, pan_card)
    print(self.acc_number)

