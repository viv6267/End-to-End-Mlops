from src.mlProject.logging import logger

from src.mlProject.pipeline.stage_01_data_injection import DataInjectionTrainingPipeline
from src.mlProject.pipeline.stage_02_data_validation import Data_Validation_Pipeline
from src.mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from src.mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline




# STAGE_NAME="Data Injection Stage"

# try:
#         logger.info(f"Starting {STAGE_NAME}")
#         pipeline=DataInjectionTrainingPipeline()
#         pipeline.main()
#         logger.info(f"{STAGE_NAME} completed successfully") 
# except Exception as e:
#         logger.error(f"An error occurred in {STAGE_NAME}: {str(e)}")
#         raise e



STAGE_NAME="Data Validation Stage"
try:
    logger.info(f">>>>>>>>>> stage{STAGE_NAME} started <<<<<<<<<<<")
    data_validation_object=Data_Validation_Pipeline()
    data_validation_object.main()
    logger.info(f">>>>>>>>>> stage{STAGE_NAME} completed successfully <<<<<<<<<<<")
except Exception as e:
    logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e


STAGE_NAME="Data Transformation Stage"
try:
    logger.info(f">>>>>>>>>> stage{STAGE_NAME} started <<<<<<<<<<<")
    data_transform_object=DataTransformationPipeline()
    data_transform_object.data_transformation_main()
    logger.info(f">>>>>>>>>> stage{STAGE_NAME} completed successfully <<<<<<<<<<<")
except Exception as e:
    logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e


STAGE_NAME="Model Trainer Pipeline Stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    model_trainer_object=ModelTrainerPipeline()
    model_trainer_object.main()
    logger.info(f">>>>>>>>>> stage  {STAGE_NAME} completed successfully <<<<<<<<<<<")
except Exception as e:
    logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e

STAGE_NAME ="Model Evaluation STAGE"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    model_eval_obj=ModelEvaluationPipeline()
    model_eval_obj.main()
    logger.info(f">>>>>>>>>> stage  {STAGE_NAME} completed successfully <<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
