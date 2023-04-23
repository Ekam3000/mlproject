import os #os module in Python provides a way to interact with the operating system.
import sys #The sys module provides information about constants, 
#functions and methods of the Python interpreter
#also sys module bcoz we will be using our custom exception

from src.exception import CustomException #importing CustomException function from exception file
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
#used to create class variables 
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
#from src.components.model_trainer import ModelTrainerConfig
#from src.components.model_trainer import ModelTrainer


@dataclass #provides a way to define classes that are primarily used to store data.
# When applied, it automatically generates special methods like __init__, __repr__, and __eq__,  
# with this , we will be directly able to define your class variable
class DataIngestionConfig:
    #any input which i require , i will give particularly through this DataIngestionConfig

    #os.path.join(path1, path2, ...) : Joins two or more path components intelligently
    train_data_path: str=os.path.join('artifacts',"train.csv") # the path for saving training data is artifacts folder , train.csv is the input which we are giving to data_ingestion.py 
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

#if we are defining only variables , then we can use @dataclass for a class, but if we have some other functions inside the class i would suggest u go ahead with the __init__(self) 
class DataIngestion:
    #The __init__ method is a special method in Python classes that is used to initialize the object's attributes when it is created. It is also called a constructor method.

#When a new instance of a class is created, the __init__ method is automatically called, and any arguments passed to the class constructor are passed to __init__. The method can then assign values to instance variables (also called attributes) and set up the object's initial state.

#Here's an example:
#class MyClass:
      #def __init__(self, arg1, arg2):
       #self.attribute1 = arg1
        #self.attribute2 = arg2
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() # ingestion_config is the variable defined using __init__

    def initiate_data_ingestion(self):# will return u train, test data from artifacts folder . Train <test split is done here 

        # if my data is stored in some databases, i will write my code  over here
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv') # here in actually i can give path of any mongodb file , mysql file if it exists
            logging.info('Read the dataset as dataframe')


            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) #making a directory for storing traing data
            # if you have a file at C:\Users\JohnDoe\Documents\file.txt, calling os.path.dirname("C:\Users\JohnDoe\Documents\file.txt") will return "C:\Users\JohnDoe\Documents", which is the directory containing the file.
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) #artifacts me data.csv ki file bn jaye gi

            # line specifies the location and name of the CSV file to be created by passing the value of self.ingestion_config.raw_data_path to the to_csv method.

            #the index parameter is set to False, which means that the row index labels of the DataFrame will not be included in the output file.

            #. The header parameter is set to True, which means that the column headers of the DataFrame will be included in the output file.
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) #rtifacts me trian.csv ki file bn jaye gi

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True) #rtifacts me test.csv ki file bn jaye gi

            logging.info("Ingestion of the data iss completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                # this information is required for the data_transformation file 
            )
        except Exception as e:
            raise CustomException(e,sys)
        
# "if name == "main":" is a common construct in Python code that is used to determine if the current file is being executed as the main program or if it is being imported as a module into another program.

#When a Python script is run, Python sets the special "name" variable to "main" for the script that is being executed. If the script is being imported as a module into another program, the "name" variable will be set to the name of the module instead.

if __name__=="__main__": # initiating and running the file
    obj=DataIngestion()
    #obj.initiate_data_ingestion()
    train_data,test_data = obj.initiate_data_ingestion()
    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data) #train , test data is passed to initiate_data_transformation function of DataTransformation class 
    
    #modeltrainer=ModelTrainer()
    #print(modeltrainer.initiate_model_trainer(train_arr,test_arr))



# after running this file artifacts folder will be created and log file will be created 



# running this file python src/components/data_ingestion.py