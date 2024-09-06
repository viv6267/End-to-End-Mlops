import os
import urllib.request as request
import zipfile
from src.mlProject.logging import logger
from src.mlProject.utils.common import get_size
from src.mlProject.constants import *
from src.mlProject.utils.common import read_yaml,create_directories
from dataclasses import dataclass
from pathlib import Path
from src.mlProject.entity.config_entity import DataInjectionConfig

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

