from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.card_1.visible = False
    self.card_2.visible = False
    self.card_3.visible = False
    self.card_4.visible = False
    self.card_5.visible = False
    self.card_6.visible = False

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.card_1.visible = True
    self.card_2.visible = False
    self.card_3.visible = False
    self.card_4.visible = False
    self.card_5.visible = False
    self.card_6.visible = False
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.card_2.visible = True
    self.card_1.visible = False
    self.card_3.visible = False
    self.card_4.visible = False
    self.card_5.visible = False
    self.card_6.visible = False
    pass

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.card_3.visible = True
    self.card_2.visible = False
    self.card_1.visible = False
    self.card_4.visible = False
    self.card_5.visible = False
    self.card_6.visible = False
    pass

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.card_4.visible = True
    self.card_2.visible = False
    self.card_3.visible = False
    self.card_1.visible = False
    self.card_5.visible = False
    self.card_6.visible = False
    pass

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.card_5.visible = True
    self.card_2.visible = False
    self.card_3.visible = False
    self.card_4.visible = False
    self.card_1.visible = False
    self.card_6.visible = False
    pass

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.card_6.visible = True
    self.card_2.visible = False
    self.card_3.visible = False
    self.card_4.visible = False
    self.card_5.visible = False
    self.card_1.visible = False
    pass






    

  