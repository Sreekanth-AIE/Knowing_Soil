import os
import logging
from pathlib import Path

# instantiating or initializing logging.
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# setting the main directory where all the imp and working code resides.
main_code_directory = "Soil_Types"

# structure of any and average professional ML or Data Science project with flask app and may be cloud deployment.
# if you good at UI/UX please also add "static" dir for flask and any other necessary dir/files for other purposes.
template_structure = ["data/README.md",
                      "notebooks/research.ipynb",
                      ".github/workflows/.gitkeep",
                      f"{main_code_directory}/__init__.py",
                      f"{main_code_directory}/components/__init__.py",
                      f"{main_code_directory}/utils/__init__.py",
                      f"{main_code_directory}/config/__init__.py",
                      f"{main_code_directory}/config/configuration.py",
                      f"{main_code_directory}/pipeline/__init__.py",
                      f"{main_code_directory}/entity/__init__.py",
                      f"{main_code_directory}/constants/__init__.py",
                      "config/config.yaml",
                      "templates/index.html",
                      "requirements.txt",
                      "setup.py"]

# generating /building the above Structure
for file_path in template_structure:
    file_dir, filename = os.path.split(Path(file_path))

    # creating the directories first and logging the process
    if file_dir:
        os.makedirs(file_dir, exist_ok=True)
        
        # logging or printing to understand the flow (logging is better though) 
        logging.info(f"Creating only directory: *{file_dir}* for the file: *{filename}*")

    # creating a new file if it is not existing or re-create the same file if the file has no data or file-size is "0 MB".
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "x") as f:
            logging.info(f"Creating empty file: {file_path}")
    # the file already exists with some data in it.
    else:
        logging.info(f"{filename} is already exists")