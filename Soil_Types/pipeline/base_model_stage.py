from Soil_Types import logger
from components.base_model_component import BuildBaseModel
from Soil_Types.config.configuration import ConfigurationManager


class BuildBaseModelPipeline:
    STAGE_NAME = "Building base model"

    def execute_stage(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = BuildBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()