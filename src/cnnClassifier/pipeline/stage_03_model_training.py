from cnnClassifier.components.model_training import Training
from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager


STAGE_NAME = "MODEL_TRAINING"



class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            training_config = config.get_training_config()
            training = Training(training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
        except Exception as e:
            logger.error(e)
            raise e
    
def model_training_main_function():
    try:
        logger.info(f"{'*' * 80}")
        logger.info(f">>>>>>  STAGE : {STAGE_NAME}  Started <<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>  STAGE : {STAGE_NAME}  Completed <<<<<<<\n\n {'x'*80}")
    except Exception as e:
        logger.exception(e)
        raise e
    
if __name__ == "__main__":
    model_training_main_function()