class CardGame:

# First issue with this test is that the statement should read "if card.value == 1:".
# Second issue is that the if statement should run with the "else" having a colon at the end of it like "else:".
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# First issue with this test is that the test is not defined. it should read "def highest_card" not "dif".
# Second issue with this test is that the arguments are not seperated by a comma. it should read as 
# "(self, card1, card2):"
# Third problem with this test is that the if statment and return values are not indented thus causing 
# inevetable problems with the test running.
# Fourth problem with this test is that the first return value has not been specified with a specific card only "card".
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2

# First problem with this test is that the test definition is not indented within the Card Class thus the test will
# not run.
# Second test is that the total variable is not defined
def cards_total(self, cards):
    total = 0
    for card in cards:
        total += card.value
        return "You have a total of" + total