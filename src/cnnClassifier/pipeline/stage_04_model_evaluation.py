from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier import logger

STAGE_NAME = "Model Evaluation"


class EvaluationPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.log_into_mlflow()

        except Exception as e:
            # logger.error(e)
            raise e


def model_evaluation_main_function():
    try:
        logger.info(f"{'*' * 80}")
        logger.info(f">>>>>>  STAGE : {STAGE_NAME}  Started <<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>  STAGE : {STAGE_NAME}  Completed <<<<<<<\n\n {'x'*80}")
    except Exception as e:
        logger.exception(e)
        raise e
     

if __name__== "__main__":
    model_evaluation_main_function()