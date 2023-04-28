#request -> for capturing any post request.
#render_template -> for the html css pages 
from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler # for working on input data 
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__) # will the entry point

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
#get -> getting the result
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else: 
        # post -> capturing the data,do the standard scaling then doing the prediction
        data=CustomData( # custom data -> the class which is creted in predict pipeline
            
            # when we do the post , this request.form will have the  entire information
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df) # predict fucntion of PredictPipeline class 
        print("after Prediction")
        return render_template('home.html',results=results[0])  # bcoz in the list format so results[0] 
    

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)        

#host="0.0.0.0" will map with 127.0.0.1


# run -> python app.py

# search on chrome 127.0.0.1:5000
# then 127.0.0.1:5000/predictdata
