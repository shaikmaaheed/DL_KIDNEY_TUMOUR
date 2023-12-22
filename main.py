from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import data_ingestion_main_function


try:
    data_ingestion_main_function()
except Exception as e:
        raise e