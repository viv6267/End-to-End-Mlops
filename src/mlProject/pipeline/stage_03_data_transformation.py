from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_transformation import DataTransformation
from src.mlProject.logging import logger
from pathlib import Path


STAGE_NAME="DATA_TRANSFORMATION_STAGE"

class DataTransformationPipeline:

    def __init__(self):

        pass
      
    def data_transformation_main(self):

        try:
            with open(Path('artifacts/data_validation/status.txt') )as f:
                data_validation_result=f.read().split(" ")[-1]

                if data_validation_result== "yes":
                    print("Data validation verified.")
                    logger.info("Data schema validation verified.")
                    config_manager = ConfigurationManager()
                    config=config_manager.data_transformation_config()
                    data_transformation=DataTransformation(config)
                    data_transformation.train_test_spliting()

                else:
                    raise Exception("Data schema validation failed")
                
        except Exception as e:
            raise e
        
                    


if __name__ == "__main__":

    data_tran_obj=DataTransformationPipeline()
    data_tran_obj.data_transformation_main()
    logger.info("Data transformation pipeline completed.")

        
