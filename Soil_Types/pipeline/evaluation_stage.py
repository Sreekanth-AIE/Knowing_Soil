from Soil_Types import logger
from Soil_Types.config.configuration import ConfigurationManager
from Soil_Types.components.evaluation_component import Evaluation


class EvaluationPipeline:
    STAGE_NAME = "Evaluation"

    def execute_stage(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()