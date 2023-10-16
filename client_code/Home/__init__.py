from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.card_1.visible = True
    self.card_2.visible = False

  def link_14_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.card_1.visible = True
    self.card_2.visible = False
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('about_us')
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('create_account')
    pass

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('deposit')
    pass

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('withdraw')
    pass

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('check_balance')
    pass

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('contact_us')
    pass

  def link_13_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('chat_with_us')
    pass

  def link_12_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('chat_with_us')
    pass

  def link_11_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('create_account')
    pass

  def link_10_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('deposit')

  def link_9_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('withdraw')

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('check_balance')

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('contact_us')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('sign_up')

  def link_15_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.card_2.visible = True
    self.card_1.visible = False
    pass

  def home_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.card_2.visible = False
    self.card_1.visible = True







    










