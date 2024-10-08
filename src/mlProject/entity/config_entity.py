from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataInjectionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_dir: Path
    STATUS_FILE: str
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    unzip_dir: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
   root_dir: Path
   train_data_path: Path
   test_data_path: Path
   model_name: str
   n_estimators: int
   learning_rate: float
   max_depth: int
   target_column: str

@dataclass(frozen=True)
class Data_Evaluation_Config:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metrics_file_name: Path
    all_params: dict
    target_columns: str