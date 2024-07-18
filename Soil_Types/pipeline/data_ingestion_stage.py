from components.data_ingestion_component import DataIngestion
from Soil_Types.config.configuration import ConfigurationManager
from Soil_Types import logger


class DataIngestionPipeline:
    STAGE_NAME = "Data Ingestion"
    
    def execute_stage(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        DataIngestion(config=data_ingestion_config)