import sys, os


os.environ['TCL_LIBRARY'] = 'c:/python38/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'c:/python38/tcl/tk8.6'
from cx_Freeze import setup, Executable

buildOptions = {"packages": ["os","PIL"]}
base = None
if sys.platform == 'Win32':
    base = 'Win32Gui'

print(sys.platform)

setup(
      name='ajout',
      version = '1.0',
      description = 'Package pour pouvoir jouer',
      options = {'build_exe': buildOptions},
      executables = [Executable('TkApp.py', base=base)])