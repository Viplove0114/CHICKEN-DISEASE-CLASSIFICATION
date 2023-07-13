import os
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO, format= '[%(asctime)s] %(message)s:')

project_name = "chicken_classfier"
'''
#we need this for deployment, i will be writing all the ci cd related commands,
#like main.yaml file will be created here.
#if you just commit any empty folder to github so you should have present something in the folder
#in future when creating main.yaml file i will remove this .gitkeep
'''
list_of_files = [

    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml", # because we are using dvc(ml oops tool)
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info (f"Empty file created: {filepath}")

    else:
        logging.info (f"{filename} is already exists")