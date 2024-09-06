from src.mlProject.logging import logger

from src.mlProject.pipeline.stage_01_data_injection import DataInjectionTrainingPipeline


STAGE_NAME="Data Injection Stage"

try:
        logger.info(f"Starting {STAGE_NAME}")
        pipeline=DataInjectionTrainingPipeline()
        pipeline.main()
        logger.info(f"{STAGE_NAME} completed successfully") 
except Exception as e:
        logger.error(f"An error occurred in {STAGE_NAME}: {str(e)}")
        raise e