import os
from src.mlProject.logging import logger
from src.mlProject.utils.common import get_size
from src.mlProject.entity.config_entity import DataValidationConfig
from pathlib import Path
import pandas as pd
import numpy as np

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)->bool:
        try:
            validation_status=None

            data=pd.read_csv(self.config.unzip_dir)
            all_col=list(data.columns)

            all_schema=self.config.all_schema.keys()
            if all(col in all_col for col in all_schema):
                validation_status="yes"

                with open(self.config.STATUS_FILE,'w') as f:
                    f.write(f"Validation Status: %s" % validation_status)
            else:
                validation_status="Not all columns are present in the data"
                with open(self.config.STATUS_FILE,'w') as f:
                    f.write(f"Validation Status: %s" % validation_status)
                    missing_cols = [col for col in all_schema if col not in all_col]
                    f.write(f"\nMissing Columns: {missing_cols}")
            return validation_status
        
        except Exception as e:
            logger.INFO("Through Exception in Data Validation part %s", e)
            raise e


