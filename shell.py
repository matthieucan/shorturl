import os
from pprint import pprint

import rlcompleter
import readline
readline.parse_and_bind("tab: complete")


from app import app

os.environ['PYTHONINSPECT'] = 'True'
