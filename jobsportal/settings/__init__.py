# Configuration-folder/settings/__init__.py


try:
    from ._development_settings import *
except:
    from ._production_settings import *
