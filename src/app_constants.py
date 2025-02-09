import sys
import os


if getattr(sys, 'frozen', False):
    # If frozen, get the path where cx_Freeze extracted the files
    try: 
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
else:
    # Running in development mode (local)
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


app_title = 'Become Citizen'

window_size = '500x500'

assets_dir = os.path.join(base_path, 'assets')

logo_path = os.path.join(assets_dir, 'become-citizen-brand.png')
favicon_path = os.path.join(assets_dir, 'become-citizen-favicon.ico')
