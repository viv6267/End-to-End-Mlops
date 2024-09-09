from src.mlProject.constants import *
from src.mlProject.utils.common import read_yaml,create_directories
from src.mlProject.logging import logger
import numpy as np
import pandas as pd
from src.mlProject.logging import logger
from xgboost import XGBRegressor
import joblib
import os
from src.mlProject.config.configuration import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)

        train_x=train_data.drop([self.config.target_column],axis=1)
        test_x=test_data.drop([self.config.target_column],axis=1)
        train_y=train_data[self.config.target_column]
        test_y=test_data[self.config.target_column]

        xgb_lr=XGBRegressor(n_estimators=self.config.n_estimators,learning_rate=self.config.learning_rate,max_depth=self.config.max_depth)

        xgb_lr.fit(train_x,train_y)
        logger.info("Model trained successfully")
        
        joblib.dump(xgb_lr, os.path.join(self.config.root_dir, self.config.model_name))

        


