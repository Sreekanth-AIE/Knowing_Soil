import os
from Soil_Types import logger
from Soil_Types.entity.config_entity import DataIngestionConfig
            

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        logger.info("understanding the directory structure for the given data source")
        for root_path,dirs,_ in os.walk(config.root_dir, topdown=True): 
            if dirs:
                logger.info(f"{root_path} -> {dirs}")
