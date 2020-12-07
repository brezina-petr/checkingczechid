# checkingczechid
checking czech id - Rodné číslo, IČO/IČ in Python 3

two simple functions:  verifyIC, verifyRC in czechid Python 3 module

# ic/ico verification , input number only - True ok, False not
def verifyIC(ic):

# rc/rodne cislo verification , input number only - True ok, False not
def verifyRC(rc):

-----------------------------------------
Example using in Python 3:

from czechid import verifyIC, verifyRC
...
ret = verifyRC("8810214897")
if ret:
  print "Valid"
else:
  print "Unvalid"
  
ret = verifyIC("25596641")
if ret:
  print "Valid"
else:
  print "Unvalid"
