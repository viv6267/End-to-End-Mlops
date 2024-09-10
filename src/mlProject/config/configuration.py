import os
import urllib.request as request
import zipfile
from src.mlProject.logging import logger
from src.mlProject.utils.common import get_size
from src.mlProject.constants import *
from src.mlProject.utils.common import read_yaml,create_directories
from dataclasses import dataclass
from pathlib import Path
from src.mlProject.entity.config_entity import DataInjectionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig, Data_Evaluation_Config

class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH,schema_file_path=SCHEMA_FILE_PATH,para_file_path=PARAMS_FILE_PATH):

        self.config = read_yaml(config_file_path)
        self.schema = read_yaml(schema_file_path)
        self.params = read_yaml(para_file_path)

        create_directories([self.config.artifacts_root])


    def get_data_injection_config(self)->DataInjectionConfig:
        
        config=self.config.data_injections

        create_directories([config.root_dir])

        data_injection_config= DataInjectionConfig(
        root_dir=config.root_dir,
        source_URL=config.source_URL,
        local_data_file=config.local_data_file,
        unzip_dir=config.unzip_dir
        )

        return data_injection_config
    
    def get_data_validation_config(self)->DataValidationConfig:
        
        config=self.config.data_validation
        schema=self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config= DataValidationConfig(
        root_dir=config.root_dir,
        STATUS_FILE=config.STATUS_FILE,
        unzip_dir=config.unzip_dir,
        all_schema=schema,
        )

        return data_validation_config
    

    def data_transformation_config(self):

        config=self.config.data_transformations
        create_directories([config.root_dir])
        transformation_config = DataTransformationConfig(
            root_dir=Path(self.config.data_transformations.root_dir),
            unzip_dir=Path(self.config.data_transformations.unzip_dir)
        )
        return transformation_config
    
    def get_model_trainer_config(self)->ModelTrainerConfig:

        config=self.config.model_trainer
        params=self.params.XGB_MODEL
        schema=self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        return ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            n_estimators=params.n_estimators,
            learning_rate=params.learning_rate,
            max_depth=params.max_depth,
            target_column=schema.name
        )
    
    def get_risk_evaluation_config(self)->Data_Evaluation_Config:

        create_directories([self.config.model_evaluation.root_dir])

        return Data_Evaluation_Config(root_dir=self.config.model_evaluation.root_dir,
                                      test_data_path=self.config.model_evaluation.test_data_path,
                                      model_path=self.config.model_evaluation.model_path,
                                      metrics_file_name=self.config.model_evaluation.metrics_file_name,
                                      all_params=self.params.XGB_MODEL,
                                      target_columns=self.schema.TARGET_COLUMN.name
                                      )

    


