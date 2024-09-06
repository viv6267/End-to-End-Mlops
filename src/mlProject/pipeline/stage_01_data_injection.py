from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_injection import DataInjection
from src.mlProject.logging import logger

STAGE_NAME="Data Injection Stage"

class DataInjectionTrainingPipeline:

    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        data_injection_config=config.get_data_injection_config()
        data_injection=DataInjection(config=data_injection_config)
        data_injection.download_file()
        data_injection.extract_zip_file()


if __name__=="__main__ ":

    try:
        logger.info(f"Starting {STAGE_NAME}")
        pipeline=DataInjectionTrainingPipeline()
        pipeline.main()
        logger.info(f"{STAGE_NAME} completed successfully") 
    except Exception as e:
        logger.error(f"An error occurred in {STAGE_NAME}: {str(e)}")
        raise e

    