#Data ingestion pipeline intialization
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.constants import *
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger


STAGE_NAME = "DATA INGESTION STAGE"



class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            data_ingestion_config = ConfigurationManager(CONFIG_FILE_PATH, PARAMS_FILE_PATH).get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.unzip_file()
        except Exception as e:
            raise e
        


def data_ingestion_main_function():
    try:
        logger.info(f">>>>>>  STAGE : {STAGE_NAME}  Started <<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>  STAGE : {STAGE_NAME}  Completed <<<<<<<\n\n {'x'*80}")
    except Exception as e:
        raise e

if __name__ == "__main__":

    data_ingestion_main_function()









