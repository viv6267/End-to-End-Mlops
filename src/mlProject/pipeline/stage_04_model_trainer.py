from src.mlProject.components.model_trainer import ModelTrainer
from src.mlProject.logging import logger
from src.mlProject.config.configuration import ConfigurationManager


STAGE_NAME = "MODEL_TRAINER_PIPELINE"

class ModelTrainerPipeline:

    def __init__(self):
        pass

    
    def main(self):
        # Load_configuration
        config_manager = ConfigurationManager()
        model_trainer_config=config_manager.get_model_trainer_config()
        model_trainer=ModelTrainer(model_trainer_config)
        model_trainer.train_model()
        

if __name__ == "__main__":

    # Initialize logging
    logger.info(f"################Starting {STAGE_NAME} pipeline ################")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.main()
    logger.info(f"################### Finished {STAGE_NAME} pipeline##############")


    