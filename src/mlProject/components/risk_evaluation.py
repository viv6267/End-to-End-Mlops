import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error,r2_score
from pathlib import Path
import joblib
import json
from src.mlProject.utils.common import read_yaml,create_directories,save_json_data
from src.mlProject.config.configuration import ConfigurationManager


class Risk_Evaluation:
    def __init__(self,config:ConfigurationManager):
        self.config = config


    def evaluate_model(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return mae, rmse, r2
    
    def save_result(self):

        
        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_path)

        test_x=test_data.drop(self.config.target_columns,axis=1)
        test_y=test_data[self.config.target_columns]

        pred=model.predict(test_x)
        mae,rmse,r2=self.evaluate_model(test_y, pred)

        # Saving metrics as local

        scores={"rmse":rmse,"mae":mae, "r2":r2}

        save_json_data(path=Path(self.config.metrics_file_name), data=scores)
