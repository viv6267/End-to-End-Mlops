import os
import urllib.request as request
import zipfile
from src.mlProject.logging import logger
from src.mlProject.utils.common import get_size
from src.mlProject.entity.config_entity import DataInjectionConfig
from pathlib import Path



class DataInjection:
    def __init__(self,config:DataInjectionConfig):

        self.config=config

    def download_file(self):

        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file 
                )
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            logger.info(f" File already exists of size:{ get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):

        """
        zip_file_path:str
        Extracts the zip file into the data directory
        function returns None

         """
        
        unzip_path=self.config.unzip_dir
        
        # Create the directory if it doesn't exist

        if not os.path.exists(unzip_path):
            try:
                os.makedirs(unzip_path,exist_ok=True)
                print(f"Directory '{unzip_path}' created successfully.")
            except PermissionError as e:
                print(f"Permission denied: {e}")
        
        try:
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                print("File extracted successfully.")
        except zipfile.BadZipFile:
            logger.info("Error: The file is not a valid zip file or is corrupted.")

        

