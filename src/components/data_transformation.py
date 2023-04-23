import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
#the above two lines are imported bcoz we have also imported them in MODEL TRAINING notebook

from sklearn.impute import SimpleImputer # for the missing values 
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging

import os
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl") # if i am creating any model , then i have to save that into a pickle file 

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    def get_data_transformer_object(self): # to work upon the pickle files , this fn is created 
        '''
        This function is responsible for data transformation
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())
                ]
            )# this pipeline will run on training dataset
            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]
            )
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                #for combining num_pipeline and cat_pipeline i am using ColumnTransformer
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object() #will read preprocessor attribute from get_data_transformer_object() function

            target_column_name="math_score" #math_score is our target column

            

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1) #obtaining training table columns and rows

            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1) #obtaining testing table columns and rows
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            ) # applying preprocessing_onj means applying all SimpleImputer , OneHotEncoding, StandardSclar on training and testing
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)

            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ] 
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            logging.info(f"Saved preprocessing object.")
            save_object(
                #used for saving the pickle file in drive with help of utils -> save_object function
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                # this line tells uss i am obtaining path of artifacts/preprocessing.pkl
                obj=preprocessing_obj
            ) 
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
