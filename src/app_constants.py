import sys
import os


if getattr(sys, 'frozen', False):
    # Running as a bundled executable
    base_path = sys._MEIPASS
else:
    # Running in development mode (local)
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


app_title = 'Become Citizen'

window_size = '500x500'

logo_path = os.path.join(base_path, 'assets/become-citizen-brand.png')
favicon_path = os.path.join(base_path, 'assets/become-citizen-favicon.ico')