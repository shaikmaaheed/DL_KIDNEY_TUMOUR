from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import data_ingestion_main_function
from cnnClassifier.pipeline.stage_02_prepare_base_model import prepare_base_model_main_function


try:
    data_ingestion_main_function()
    prepare_base_model_main_function()
except Exception as e:
        raise e