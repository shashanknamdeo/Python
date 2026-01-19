
# __init__.py
# -----------

# Creating __init__.py means you are turning a folder into a Python package so its files can be imported and reused in other Python code.

# __init__.py means
#     When you create an __init__.py file inside a folder, you are telling Python:
#     “This folder should be treated as a Python package (module).”

# Example:

# my_project/
# │
# ├── math_utils/
# │   ├── __init__.py
# │   ├── add.py
# │   └── subtract.py


# Here:
#     math_utils is a package
#     add.py and subtract.py are modules inside that package
#     Because __init__.py exists, Python allows:

import math_utils
from math_utils import add

# -------------------------------------------------

# inside __init__.py

# It can be:
#     Empty (just to mark the folder as a package)
#     Used to initialize package-level code
#     Used to control what gets imported

# Example:

# math_utils/__init__.py
from .add import add_numbers
from .subtract import subtract_numbers

# Now you can do:

from math_utils import add_numbers

