import os
from src.mlProject.logging import logger
from src.mlProject.utils.common import get_size
from src.mlProject.entity.config_entity import DataTransformationConfig
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split



class DataTransformation:

    def __init__(self,config:DataTransformationConfig):

        self.config = config

    """
    # Note you can perform different transformation techniques such as scaler, pca, etc
    # You can also perform all the kind of EDA transformations
    
    """
    def train_test_spliting(self):
        df=pd.read_csv(self.config.unzip_dir)
        train,test=train_test_split(df)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)
        logger.info('Splitted data into training and test sets')
        logger.info(train.shape)
        print("Train Shape: ", train.shape)
        logger.info(test.shape)
        print("Test Shape: ", test.shape)