from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger


STAGE_NAME = "Prepare Base Model"



class PrepareBaseModeLTrainingPipeline:
    def __init__(self) -> None:
        pass


    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.updated_base_model()

        except Exception as e:
            raise e


def prepare_base_model_main_function():
    try:
        logger.info(f"{'*' * 80}")
        logger.info(f">>>>>>  STAGE : {STAGE_NAME}  Started <<<<<<<")
        obj = PrepareBaseModeLTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>  STAGE : {STAGE_NAME}  Completed <<<<<<<\n\n {'x'*80}")
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == "__main__":
    prepare_base_model_main_function()