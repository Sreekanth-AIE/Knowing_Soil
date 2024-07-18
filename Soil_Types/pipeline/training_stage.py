from Soil_Types import logger
from components.training_component import Training
from components.callbacks_component import PrepareCallback
from Soil_Types.config.configuration import ConfigurationManager


class ModelTrainingPipeline:
    STAGE_NAME = "Training"

    def execute_stage(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_untrained_model()
        training.train_valid_data_generator()
        training.train(callback_list=callback_list)