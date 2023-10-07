import sys
from cx_Freeze import setup, Executable

setup(
    name = "AHHull",
    version = "1.0",
    description = "A OFFSET DATA TABLE TO DXF MAKER.",
    executables = [Executable("_main.py", base = "Win32GUI")])