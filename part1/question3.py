################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

class MagicalOven:

  formulas = {
    "freeze": {
      ("water", "air"): "snow",
      # future formulas for freezing process   
    },
    "boil": {
      ("cheese", "dough", "tomato"): "pizza",
      ("lead", "mercury"): "gold",
      # future formulas for boiling process   
    }, 
    "wait": {}
    # future formulas for other processes
  }

  def __init__(self):
    self.ingredients = []
    self.magical_result = None

  def add(self, item):
    self.ingredients.append(item)

  def __combine_helper(self, process):
    for formula, result in MagicalOven.formulas[process].items():
      if formula == tuple(self.ingredients): 
        self.magical_result = result

  def freeze(self):
    self.__combine_helper("freeze")

  def boil(self):
    self.__combine_helper("boil")

  def wait(self):
    self.__combine_helper("wait")

  def get_output(self):
    if self.magical_result:
      return self.magical_result
    else:
      return "no result yet!"

# This function should return an oven instance!
def make_oven():
  return MagicalOven()

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()
