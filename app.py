from flask import Flask, render_template, request
import os
import numpy as np
import pandas as  pd
from src.mlProject.pipeline.prediction_pipeline import PredictionPipeline


app= Flask(__name__) # Intialize the Flask

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/train',methods=['GET'])
def training_pipeline():
    os.system('python main.py')
    return 'Training pipeline completed'

@app.route('/predict', methods=['POST','GET']) # route to show the prediction pipeline
def predict():

    try:
        if request.method == 'POST':
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH=float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            data=[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,
                  free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            
            data=np.array(data).reshape(1,11)
            
            prediction_pipeline = PredictionPipeline()
            prediction = prediction_pipeline.predict(data)

            return render_template('prediction_result.html', prediction=str(prediction))
    except Exception as e:
        print("The exception message: " + str(e))

            


if __name__ == '__main__':
    app.run(debug=True)