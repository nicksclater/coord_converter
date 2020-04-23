
from kivy.config import Config
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 200)
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
import numpy as np
import mgrs_funcs
from mgrs import MGRS
m = MGRS()


class UI(Widget):

  input_str = StringProperty()
  converted_pos = StringProperty()

  def clear_input(self):

    self.ids['input_pos'].text = ''
    self.ids['output_pos'].text = ''

  def select_format(self):
    
    if self.ids['input_pos'].text != '': 

      if self.ids['deg'].state == 'down':
        self.convert_deg()
      
      elif self.ids['dm'].state == 'down':
          self.convert_dm()
      
      elif self.ids['dms'].state == 'down':
        self.convert_dms()
      
      elif self.ids['mgrs'].state == 'down':
        self.convert_mgrs()
      
      elif self.ids['bng'].state == 'down':
        self.convert_bng()


  def convert_deg(self):

    input_str = str(self.ids['input_pos'].text)
    
    if ((input_str[0].isalpha() and input_str[1].isalpha()) or (input_str[0].isnumeric() and input_str[-1].isnumeric())):
      result = mgrs_funcs.convert_2_deg(input_str)
    
    else:
      result = mgrs_funcs.convert_dm_deg(input_str)
   
    try:
      self.converted_pos = str(np.round(result[0],4)) + '  ' + str(np.round(result[1], 4))
      self.ids['output_pos'].color=(1,1,1,1)
   
    except:
      self.converted_pos = str(result)
      self.ids['output_pos'].color=(1,1,1,1)


  def convert_dm(self):

    input_str = str(self.ids['input_pos'].text)
    
    if ((input_str[0].isalpha() and input_str[1].isalpha()) or (input_str[0].isnumeric() and input_str[-1].isnumeric())):
      result = mgrs_funcs.convert_deg_dm(mgrs_funcs.convert_2_deg(input_str))
    
    else:
      result = mgrs_funcs.convert_deg_dm(mgrs_funcs.convert_dm_deg(input_str))

    if isinstance(result,list):
      self.converted_pos = str(result[0]) + '  ' + str(result[1])
      self.ids['output_pos'].color=(1,1,1,1)
    
    else:
      self.converted_pos = str(result)
      self.ids['output_pos'].color=(1,1,1,1)


  def convert_dms(self):

    input_str = str(self.ids['input_pos'].text)
    
    if ((input_str[0].isalpha() and input_str[1].isalpha()) or (input_str[0].isnumeric() and input_str[-1].isnumeric())):
      result = mgrs_funcs.convert_deg_dms(mgrs_funcs.convert_2_deg(input_str))
    
    else:
      result = mgrs_funcs.convert_deg_dms(mgrs_funcs.convert_dm_deg(input_str))
    
    if isinstance(result, list):
      self.converted_pos = str(result[0]) + '  ' + str(result[1])
      self.ids['output_pos'].color=(1,1,1,1)
    
    else:
      self.converted_pos = str(result)
      self.ids['output_pos'].color=(1,1,1,1)

  def convert_mgrs(self):

    input_str = str(self.ids['input_pos'].text)
    
    if ((input_str[0].isalpha() and input_str[1].isalpha()) or (input_str[0].isnumeric() and input_str[-1].isnumeric())):
    
      result = mgrs_funcs.convert_deg_mgrs(mgrs_funcs.convert_2_deg(input_str))
    
    else:
      result = mgrs_funcs.convert_deg_mgrs(mgrs_funcs.convert_dm_deg(input_str))
    self.converted_pos = result
    

  
  def convert_bng(self):

    input_str = str(self.ids['input_pos'].text)
    
    if ((input_str[0].isalpha() and input_str[1].isalpha()) or (input_str[0].isnumeric() and input_str[-1].isnumeric())):
      result = str(mgrs_funcs.convert_deg_bng(mgrs_funcs.convert_2_deg(input_str)))
    
    else:
      result = mgrs_funcs.convert_deg_bng(mgrs_funcs.convert_dm_deg(input_str))
    
    self.converted_pos = result



class MgrsApp(App):
  def build(self):
    return UI()


if __name__ == '__main__':
  MgrsApp().run()



# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.label import Label
# from kivy.uix.togglebutton import ToggleButton
# from kivy.core.window import Window
# Window.size=(400, 200)
#Config.set('graphics', 'borderless', 1)


