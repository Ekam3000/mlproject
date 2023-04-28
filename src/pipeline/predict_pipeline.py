import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object # for loading our pickle file with help of utils

class PredictPipeline:
    def __init__(self): #the empty constructor
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','proprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path) # this function load_object will import the pickle and load the pickle file in short , this function should be creted in utils
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features) # transforming the features 
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)

class CustomData: # for mapping all the inputs that we are giving in the HTML to the backend 
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score
        #the values are coming from web application


    def get_data_as_data_frame(self): # it will return all my inputs in the form of dataframe , bcoz we train our model in the form of datframe
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            return pd.DataFrame(custom_data_input_dict) # from my website, whatever the inputs i am probably giving that same inputs will get assigned /mapped with this particular values 

        except Exception as e:
            raise CustomException(e, sys)

