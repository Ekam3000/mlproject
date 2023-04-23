import logging # for the purpose that any execution that probably happens we should be able to log all those information the exeution everything in some files so that will be able to track if there is some errors even the custom exception error , we will try to log that into the text file
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH, # will create log files under logs folder acc to LOG_FILE mentioned path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("logging has started...")

# It Allows You to Execute Code When the File Runs as a Script, but Not When It's Imported as a Module. For most practical purposes, you can think of the conditional block that you open with if __name__ == "__main__" as a way to store code that should only run when your file is executed as a script.