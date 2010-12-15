from distutils.core import setup
import py2exe
import os
from sys import path

path.insert(0, "src")
python_modules = []
dirs = ["src", "../../src", "../../utils"]
for dir in dirs:
    for filename in os.listdir(dir):
        try:
            extension = filename[-3:]
            core_filename = filename[:-3]
            if extension == ".py" and core_filename not in python_modules:
                python_modules.append(core_filename)
        except:
            pass
    
setup(console=['main_sim.py'], 
      options={
               "py2exe": {
                         "includes": python_modules,
                         "packages": ["cwm_data"]
                         }
               }
      )
qweqweasdas