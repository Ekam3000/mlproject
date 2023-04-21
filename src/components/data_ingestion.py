import os
import sys #bcoz we will be using our custom exception

from src.exception import CustomException #importing CustomException function from exception file
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass#used to create class variables 
#from src.components.data_transformation import DataTransformation
#from src.components.data_transformation import DataTransformationConfig
#from src.components.model_trainer import ModelTrainerConfig
#from src.components.model_trainer import ModelTrainer


@dataclass # with this , we will be directly able to define your class variable
class DataIngestionConfig:
    #any input which i require , i will give particularly through this DataIngestionConfig
    train_data_path: str=os.path.join('artifacts',"train.csv") # the path for saving training data is artifacts folder , train.csv is the input which we are giving to data_ingestion.py 
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

#if we are defining only variables , then we can use @dataclass for a class, but if we have some other functions inside the class i would suggest u go ahead with the __init__(self) 
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() # ingestion_config is the variable defined using __init__
    def initiate_data_ingestion(self):
        # if my data is stored in some databases, i will write my code  over here
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv') # here in actually i can give path of any mongodb file , mysql file if it exists
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) #making a directory for storing traing data

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            # line specifies the location and name of the CSV file to be created by passing the value of self.ingestion_config.raw_data_path to the to_csv method.

            #the index parameter is set to False, which means that the row index labels of the DataFrame will not be included in the output file.

            #. The header parameter is set to True, which means that the column headers of the DataFrame will be included in the output file.
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

                # this information is required for the data_transformation file 
            )
        except Exception as e:
            raise CustomException(e,sys)
if __name__=="__main__": # initiating and running the file
    obj=DataIngestion()
    obj.initiate_data_ingestion()
    #data_transformation=DataTransformation()
    #train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
    #modeltrainer=ModelTrainer()
    #print(modeltrainer.initiate_model_trainer(train_arr,test_arr))



# after running this file artifacts folder will be created and log file will be created 



# running this file python src/components/data_ingestion.py