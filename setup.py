import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but some modules need manual configuration
build_exe_options = {
    "packages": ["pytz", "pyautogui", "termcolor", "argparse", "Xlib"],
    "include_files": [],  # Include any additional files if needed
    "excludes": [],
}

# Base specifies the type of application (console or GUI)
base = None
if sys.platform == "win32":
    base = "Console"  # Use "Win32GUI" for GUI applications

setup(
    name="FastClicker",
    version="1.0",
    description="A script that automates a single mouse click at a specified time.",
    options={"build_exe": build_exe_options},
    executables=[Executable("fast_clicker.py", base=base)],
)
