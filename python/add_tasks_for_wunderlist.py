from datetime import datetime
from wunderpy import Wunderlist

w = Wunderlist()
w.login("username", "password")
w.update_lists() # you have to run this first, before you do anything else

w.add_list("test") # make a new list called "test"

print w.lists