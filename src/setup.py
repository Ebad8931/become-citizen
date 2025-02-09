from cx_Freeze import setup, Executable
import sys
import os

from app_constants import assets_dir


# Ensure it runs as a GUI application (not a console one)
base = "Win32GUI" if sys.platform == "win32" else None

script_path = os.path.join(os.path.dirname(__file__), "app.py")  # Points to src/app.py
output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../releases"))  # Places .exe in Project-Root/Releases
app_name = 'Become-Citizen'

# Define the executable file
executables = [
    Executable(
        script=script_path,
        base=base,
        target_name=f"{app_name}.exe",  # Name of the generated .exe
    )
]

# Define the setup configuration
setup(
    name=app_name,
    version="1.0",
    description="""
        Become-Citizen app helps users prepare for the U.S. naturalization test 
        with Listening and Speaking practice.
    """,
    executables=executables,
    options={
        "build_exe": {
            "build_exe": output_path,                       # Output folder
            "includes": [],                                 # Add dependencies if needed
            "excludes": ["tkinter.test", "unittest"],       # Exclude unnecessary modules
            "include_files": [(assets_dir, "assets")],      # include assets
            "include_msvcr": True,                          # include dll files (msvcr.dll and Python DLLs)
            "optimize": 2
        }
    },
)