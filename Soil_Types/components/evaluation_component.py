import tensorflow as tf
from pathlib import Path
from Soil_Types.utils.common import save_json
from Soil_Types.entity.config_entity import EvaluationConfig


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    def _test_generator(self):

        # initializing the Image_data_generator instance
        test_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rescale = 1./255
            )

        # Executing the Data Acquisition process for training set
        self.test_set_generator_inst = test_datagenerator.flow_from_directory(
            directory=self.config.validation_data,
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            class_mode='categorical',
            shuffle=True,
            interpolation="bilinear"
        )

    
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        # acquiring the best saved checkpoint
        model = self.load_model(self.config.path_of_model)
        
        # acquiring test dataset
        self._test_generator()

        # evaluating the model on test dataset
        self.score = model.evaluate(self.test_set_generator_inst)

    
    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    

    