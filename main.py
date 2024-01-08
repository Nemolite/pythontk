from window import *
from db import *

db = DB()
db.create('people')

window = Window()
arr_people = db.select('people')
window.display_db_table(arr_people,'people')

