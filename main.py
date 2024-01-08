from window import *
from db import *

db = DB()
window = Window()
db.create('people')
window.display_db_table()

