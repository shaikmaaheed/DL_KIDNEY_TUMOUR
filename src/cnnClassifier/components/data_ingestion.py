from zipfile import ZipFile
from cnnClassifier import logger
import os
import gdown
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.entity.config_entity import (DataIngestionConfig)



class DataIngestion:

    def __init__(self, config:DataIngestionConfig) -> None:
        self.config = config

    def download_data(self):
        try:
            URL = self.config.source_URL
            prefix = "https://drive.google.com/uc?/export=download&id="
            file_code = URL.split("/")[-2]
            gdown.download(prefix+file_code, self.config.local_data_file)
            logger.info(f"Dowmloaded data from {URL} into {self.config.local_data_file}")
        except Exception as e :
            raise e
        



    def unzip_file(self):
        # try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)
        # except Exception as e:
        #     raise e
