from src.mlProject.components.risk_evaluation import Risk_Evaluation
from src.mlProject.logging import logger
from src.mlProject.config.configuration import ConfigurationManager


STAGE_NAME ="Model Evaluation STAGE"

class ModelEvaluationPipeline:

    def __init__(self):

        pass

    def main(self):

        cm = ConfigurationManager()
        cm_config = cm.get_risk_evaluation_config()
        re = Risk_Evaluation(config=cm_config)
        re.save_result()

if __name__ == '__main__':
    logger.info(f"Starting {STAGE_NAME}")
    model_eval_obj=ModelEvaluationPipeline()
    model_eval_obj.main()
    logger.info(f"{STAGE_NAME} completed successfully")
