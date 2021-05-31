import os

py_exe_file = os.path.abspath("venv\Scripts\pythonw.exe")

main_file = os.path.abspath("scatterbrained.py")

os.system("{} {}".format(py_exe_file, main_file))

