from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_validation import DataValidation
from src.mlProject.logging import logger

STAGE_NAME="Data Validation Stage"

class Data_Validation_Pipeline:

    def __init__(self):
        pass

    def main(self):
        
        config_manager = ConfigurationManager()
        data_validation_config = config_manager.get_data_validation_config()
        data_validation=DataValidation(data_validation_config)
        data_validation.validate_all_columns()
        logger.info(f"{STAGE_NAME} completed successfully.")

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage{STAGE_NAME} started <<<<<<<<<<<")
        data_validation_object=data_validation_pipeline()
        data_validation_object.main()
        logger.info(f">>>>>>>>>> stage{STAGE_NAME} completed successfully <<<<<<<<<<<")
    except Exception as e:
        logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
        raise e
