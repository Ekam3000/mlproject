# whenever requirement is there we will try to create those files , we will try to create the functionalities(will have all the common things that we are trying tp import and use ) but excpetion and logger is definitely required


import os
import sys

import numpy as np 
import pandas as pd
import dill #help us to create pickle file
#import pickle
#from sklearn.metrics import r2_score
#from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

#the save_object from data_transformation file 
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            #pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
 